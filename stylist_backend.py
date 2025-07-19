"""
Backend logic for the AI stylist - filtering and recommendation engine
"""
import json
import random
from typing import List, Dict, Any
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class AIStyler:
    def __init__(self, catalog_file='catalog_enriched.json'):
        self.catalog_file = catalog_file
        self.products = self.load_catalog()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    def load_catalog(self):
        """Load the enriched product catalog"""
        try:
            with open(self.catalog_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {self.catalog_file} not found. Using basic catalog.")
            try:
                with open('catalog.json', 'r', encoding='utf-8') as f:
                    return json.load(f)
            except FileNotFoundError:
                return []
    
    def filter_by_style(self, style_preferences: List[str]) -> List[Dict]:
        """Filter products by style tags"""
        if not style_preferences:
            return self.products
        
        filtered = []
        for product in self.products:
            product_styles = product.get('style_tags', [])
            if any(style.lower() in [s.lower() for s in product_styles] for style in style_preferences):
                filtered.append(product)
        
        return filtered
    
    def filter_by_occasion(self, occasions: List[str]) -> List[Dict]:
        """Filter products by occasion tags"""
        if not occasions:
            return self.products
        
        filtered = []
        for product in self.products:
            product_occasions = product.get('occasion_tags', [])
            if any(occasion.lower() in [o.lower() for o in product_occasions] for occasion in occasions):
                filtered.append(product)
        
        return filtered
    
    def filter_by_category(self, categories: List[str]) -> List[Dict]:
        """Filter products by category"""
        if not categories:
            return self.products
        
        filtered = []
        for product in self.products:
            product_category = product.get('category', '').lower()
            if any(cat.lower() in product_category for cat in categories):
                filtered.append(product)
        
        return filtered
    
    def filter_by_brand(self, brands: List[str]) -> List[Dict]:
        """Filter products by brand"""
        if not brands:
            return self.products
        
        filtered = []
        for product in self.products:
            product_brand = product.get('brand', '').lower()
            if any(brand.lower() in product_brand for brand in brands):
                filtered.append(product)
        
        return filtered
    
    def get_recommendations(self, 
                          style_preferences: List[str] = None,
                          occasions: List[str] = None,
                          categories: List[str] = None,
                          brands: List[str] = None,
                          max_items: int = 6) -> List[Dict]:
        """Get product recommendations based on filters"""
        
        # Start with all products
        filtered_products = self.products.copy()
        
        # Apply filters
        if style_preferences:
            filtered_products = [p for p in filtered_products if p in self.filter_by_style(style_preferences)]
        
        if occasions:
            filtered_products = [p for p in filtered_products if p in self.filter_by_occasion(occasions)]
        
        if categories:
            filtered_products = [p for p in filtered_products if p in self.filter_by_category(categories)]
        
        if brands:
            filtered_products = [p for p in filtered_products if p in self.filter_by_brand(brands)]
        
        # Shuffle and limit results
        random.shuffle(filtered_products)
        return filtered_products[:max_items]
    
    def create_outfit(self, 
                     style_preference: str = "casual",
                     occasion: str = "everyday",
                     max_items: int = 3) -> List[Dict]:
        """Create a complete outfit recommendation"""
        
        # Try to get items from different categories for a complete outfit
        outfit_categories = ['tops', 'bottoms', 'accessories', 'shoes', 'outerwear']
        outfit = []
        
        for category in outfit_categories:
            if len(outfit) >= max_items:
                break
                
            items = self.get_recommendations(
                style_preferences=[style_preference],
                occasions=[occasion],
                categories=[category],
                max_items=1
            )
            
            if items:
                outfit.extend(items)
        
        # If we don't have enough items, fill with general recommendations
        if len(outfit) < max_items:
            additional_items = self.get_recommendations(
                style_preferences=[style_preference],
                occasions=[occasion],
                max_items=max_items - len(outfit)
            )
            
            # Avoid duplicates
            for item in additional_items:
                if item not in outfit:
                    outfit.append(item)
                    if len(outfit) >= max_items:
                        break
        
        return outfit
    
    def get_ai_styling_advice(self, user_input: str) -> str:
        """Get personalized styling advice using GPT-4"""
        
        # Get some sample products for context
        sample_products = random.sample(self.products, min(5, len(self.products)))
        product_context = "\n".join([
            f"- {p.get('name', 'Unknown')} by {p.get('brand', 'Unknown')} ({p.get('category', 'Unknown')}): {p.get('description', '')}"
            for p in sample_products
        ])
        
        prompt = f"""
        You are a professional fashion stylist. A user is asking for styling advice.
        
        User request: {user_input}
        
        Available products in our catalog include:
        {product_context}
        
        Provide helpful, personalized styling advice. Be specific about:
        1. Style recommendations
        2. How to mix and match items
        3. Occasion-appropriate suggestions
        4. Color coordination tips
        
        Keep your response conversational and helpful, around 2-3 paragraphs.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable and friendly fashion stylist who gives practical, personalized advice."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=400,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            return f"I'd love to help with styling advice! However, I'm having trouble accessing my AI assistant right now. Please make sure your OpenAI API key is configured correctly. Error: {e}"
    
    def get_available_styles(self) -> List[str]:
        """Get all available style tags from the catalog"""
        styles = set()
        for product in self.products:
            styles.update(product.get('style_tags', []))
        return sorted(list(styles))
    
    def get_available_occasions(self) -> List[str]:
        """Get all available occasion tags from the catalog"""
        occasions = set()
        for product in self.products:
            occasions.update(product.get('occasion_tags', []))
        return sorted(list(occasions))
    
    def get_available_categories(self) -> List[str]:
        """Get all available categories from the catalog"""
        categories = set()
        for product in self.products:
            category = product.get('category', '')
            if category:
                categories.add(category)
        return sorted(list(categories))
    
    def get_available_brands(self) -> List[str]:
        """Get all available brands from the catalog"""
        brands = set()
        for product in self.products:
            brand = product.get('brand', '')
            if brand:
                brands.add(brand)
        return sorted(list(brands))