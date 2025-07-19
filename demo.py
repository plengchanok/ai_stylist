"""
Demo script to showcase the AI stylist functionality
"""
from stylist_backend import AIStyler
import json

def demo_ai_stylist():
    """Demonstrate the AI stylist capabilities"""
    
    print("🎯 AI Fashion Stylist Demo")
    print("=" * 50)
    
    # Initialize the stylist
    stylist = AIStyler()
    
    print(f"📊 Loaded {len(stylist.products)} products")
    print()
    
    # Show available options
    print("🎨 Available Styles:")
    styles = stylist.get_available_styles()
    print(f"   {', '.join(styles) if styles else 'No styles available (run enrich_with_gpt.py first)'}")
    print()
    
    print("🎪 Available Occasions:")
    occasions = stylist.get_available_occasions()
    print(f"   {', '.join(occasions) if occasions else 'No occasions available (run enrich_with_gpt.py first)'}")
    print()
    
    print("🏷️ Available Brands:")
    brands = stylist.get_available_brands()
    print(f"   {', '.join(brands)}")
    print()
    
    print("📦 Available Categories:")
    categories = stylist.get_available_categories()
    print(f"   {', '.join(categories)}")
    print()
    
    # Demo recommendations
    print("🔍 Sample Recommendations:")
    print("-" * 30)
    
    # Get recommendations by brand
    lululemon_items = stylist.filter_by_brand(['Lululemon'])
    print(f"🍋 Lululemon items: {len(lululemon_items)}")
    for item in lululemon_items[:2]:
        print(f"   • {item['name']} - {item['price']}")
    print()
    
    # Get recommendations by category
    leggings = stylist.filter_by_category(['Leggings'])
    print(f"👖 Leggings: {len(leggings)}")
    for item in leggings[:3]:
        print(f"   • {item['name']} by {item['brand']} - {item['price']}")
    print()
    
    # Create a sample outfit
    print("👔 Sample Outfit Creation:")
    print("-" * 30)
    outfit = stylist.create_outfit(
        style_preference="casual",
        occasion="everyday",
        max_items=3
    )
    
    if outfit:
        print("✨ Your outfit for today:")
        for i, item in enumerate(outfit, 1):
            print(f"   {i}. {item['name']} by {item['brand']} - {item['price']}")
            print(f"      {item['description'][:60]}...")
    else:
        print("   No outfit could be created with current data")
    
    print()
    print("🚀 To see the full interactive experience, run:")
    print("   streamlit run app.py")

if __name__ == "__main__":
    demo_ai_stylist()