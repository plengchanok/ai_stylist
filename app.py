"""
Streamlit app for the AI Fashion Stylist
"""
import streamlit as st
import json
import os
from stylist_backend import AIStyler
from import_google_sheets import import_from_google_sheets
from enrich_with_gpt import ProductEnricher

# Page configuration
st.set_page_config(
    page_title="👗 AI Fashion Stylist",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .product-card {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #f9f9f9;
    }
    .product-name {
        font-weight: bold;
        font-size: 18px;
        color: #333;
    }
    .product-brand {
        color: #666;
        font-style: italic;
    }
    .product-price {
        color: #e74c3c;
        font-weight: bold;
        font-size: 16px;
    }
    .tags {
        margin-top: 10px;
    }
    .tag {
        background-color: #3498db;
        color: white;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 12px;
        margin: 2px;
        display: inline-block;
    }
    .occasion-tag {
        background-color: #e67e22;
    }
</style>
""", unsafe_allow_html=True)

def display_product(product):
    """Display a product in a nice card format"""
    with st.container():
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">{product.get('name', 'Unknown Product')}</div>
            <div class="product-brand">{product.get('brand', 'Unknown Brand')}</div>
            <div class="product-price">{product.get('price', 'Price not available')}</div>
            <p>{product.get('description', 'No description available')}</p>
        """, unsafe_allow_html=True)
        
        # Display image if available
        image_url = product.get('image_url', '')
        if image_url and image_url != '':
            try:
                st.image(image_url, width=200)
            except:
                st.write("📷 Image not available")
        
        # Display tags
        style_tags = product.get('style_tags', [])
        occasion_tags = product.get('occasion_tags', [])
        
        if style_tags or occasion_tags:
            st.markdown('<div class="tags">', unsafe_allow_html=True)
            
            if style_tags:
                st.write("**Style Tags:**")
                tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in style_tags])
                st.markdown(tags_html, unsafe_allow_html=True)
            
            if occasion_tags:
                st.write("**Occasion Tags:**")
                tags_html = "".join([f'<span class="tag occasion-tag">{tag}</span>' for tag in occasion_tags])
                st.markdown(tags_html, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

def main():
    st.title("👗 AI Fashion Stylist")
    st.markdown("*Your personal AI-powered fashion assistant*")
    
    # Initialize the stylist
    if 'stylist' not in st.session_state:
        st.session_state.stylist = AIStyler()
    
    stylist = st.session_state.stylist
    
    # Sidebar for data management
    with st.sidebar:
        st.header("📊 Data Management")
        
        # Check if we have data
        if not stylist.products:
            st.warning("No product data found!")
            if st.button("Import from Google Sheets"):
                with st.spinner("Importing data..."):
                    import_from_google_sheets()
                    st.session_state.stylist = AIStyler()
                    st.rerun()
        else:
            st.success(f"✅ {len(stylist.products)} products loaded")
        
        # Data enrichment
        if st.button("Enrich with AI Tags"):
            if not os.getenv('OPENAI_API_KEY'):
                st.error("Please set your OPENAI_API_KEY in the .env file")
            else:
                with st.spinner("Enriching products with AI tags..."):
                    enricher = ProductEnricher()
                    enricher.enrich_catalog()
                    st.session_state.stylist = AIStyler()
                    st.success("Products enriched with AI tags!")
                    st.rerun()
        
        # Display available options
        if stylist.products:
            st.subheader("Available Options")
            
            styles = stylist.get_available_styles()
            if styles:
                st.write(f"**Styles:** {', '.join(styles[:5])}{'...' if len(styles) > 5 else ''}")
            
            occasions = stylist.get_available_occasions()
            if occasions:
                st.write(f"**Occasions:** {', '.join(occasions[:5])}{'...' if len(occasions) > 5 else ''}")
            
            brands = stylist.get_available_brands()
            if brands:
                st.write(f"**Brands:** {', '.join(brands[:3])}{'...' if len(brands) > 3 else ''}")
    
    # Main content area
    if not stylist.products:
        st.info("👆 Please import your product data from Google Sheets using the sidebar to get started!")
        return
    
    # Create tabs for different features
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Style Recommendations", "👔 Create Outfit", "💬 AI Styling Advice", "🔍 Browse Catalog"])
    
    with tab1:
        st.header("🎯 Get Style Recommendations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Style preferences
            available_styles = stylist.get_available_styles()
            selected_styles = st.multiselect(
                "Select your style preferences:",
                available_styles,
                default=available_styles[:2] if available_styles else []
            )
            
            # Occasions
            available_occasions = stylist.get_available_occasions()
            selected_occasions = st.multiselect(
                "Select occasions:",
                available_occasions,
                default=available_occasions[:1] if available_occasions else []
            )
        
        with col2:
            # Categories
            available_categories = stylist.get_available_categories()
            selected_categories = st.multiselect(
                "Select categories (optional):",
                available_categories
            )
            
            # Brands
            available_brands = stylist.get_available_brands()
            selected_brands = st.multiselect(
                "Select brands (optional):",
                available_brands
            )
        
        # Number of recommendations
        max_items = st.slider("Number of recommendations:", 1, 12, 6)
        
        if st.button("Get Recommendations", type="primary"):
            recommendations = stylist.get_recommendations(
                style_preferences=selected_styles,
                occasions=selected_occasions,
                categories=selected_categories,
                brands=selected_brands,
                max_items=max_items
            )
            
            if recommendations:
                st.success(f"Found {len(recommendations)} recommendations for you!")
                
                # Display recommendations in columns
                cols = st.columns(2)
                for i, product in enumerate(recommendations):
                    with cols[i % 2]:
                        display_product(product)
            else:
                st.warning("No products found matching your criteria. Try adjusting your filters.")
    
    with tab2:
        st.header("👔 Create Complete Outfit")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            outfit_style = st.selectbox(
                "Choose outfit style:",
                stylist.get_available_styles() if stylist.get_available_styles() else ["casual"]
            )
            
            outfit_occasion = st.selectbox(
                "Choose occasion:",
                stylist.get_available_occasions() if stylist.get_available_occasions() else ["everyday"]
            )
            
            outfit_items = st.slider("Number of items in outfit:", 2, 5, 3)
        
        if st.button("Create Outfit", type="primary"):
            outfit = stylist.create_outfit(
                style_preference=outfit_style,
                occasion=outfit_occasion,
                max_items=outfit_items
            )
            
            if outfit:
                st.success(f"Here's your {outfit_style} outfit for {outfit_occasion}!")
                
                for i, item in enumerate(outfit):
                    st.subheader(f"Item {i+1}")
                    display_product(item)
            else:
                st.warning("Couldn't create an outfit with your criteria. Try different options.")
    
    with tab3:
        st.header("💬 AI Styling Advice")
        st.write("Ask me anything about fashion and styling!")
        
        user_question = st.text_area(
            "What would you like to know?",
            placeholder="e.g., 'What should I wear for a casual date night?' or 'How do I style athleisure for work?'"
        )
        
        if st.button("Get AI Advice", type="primary") and user_question:
            if not os.getenv('OPENAI_API_KEY'):
                st.error("Please set your OPENAI_API_KEY in the .env file to use AI advice feature.")
            else:
                with st.spinner("Getting personalized advice..."):
                    advice = stylist.get_ai_styling_advice(user_question)
                    st.markdown("### 💡 Styling Advice")
                    st.write(advice)
    
    with tab4:
        st.header("🔍 Browse Full Catalog")
        
        # Search functionality
        search_term = st.text_input("Search products:", placeholder="Enter product name, brand, or description...")
        
        # Filter products based on search
        if search_term:
            filtered_products = [
                p for p in stylist.products 
                if search_term.lower() in p.get('name', '').lower() 
                or search_term.lower() in p.get('brand', '').lower()
                or search_term.lower() in p.get('description', '').lower()
            ]
        else:
            filtered_products = stylist.products
        
        st.write(f"Showing {len(filtered_products)} products")
        
        # Display products in a grid
        if filtered_products:
            cols = st.columns(2)
            for i, product in enumerate(filtered_products[:20]):  # Limit to first 20 for performance
                with cols[i % 2]:
                    display_product(product)
            
            if len(filtered_products) > 20:
                st.info(f"Showing first 20 of {len(filtered_products)} products. Use search to narrow down results.")

if __name__ == "__main__":
    main()