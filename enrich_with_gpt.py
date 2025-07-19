"""
Enrich product catalog with GPT-4 generated style and occasion tags
"""
import json
import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

class ProductEnricher:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    def generate_tags(self, product_name, description, brand="", category=""):
        """Generate style and occasion tags for a product using GPT-4"""
        
        prompt = f"""
        Given this fashion product information:
        
        Product Name: {product_name}
        Brand: {brand}
        Category: {category}
        Description: {description}
        
        Analyze this product and assign appropriate style and occasion tags.
        
        Style tags should describe the aesthetic/vibe (e.g., "minimal", "athleisure", "sporty", "casual", "elegant", "boho", "edgy", "classic", "trendy", "vintage")
        
        Occasion tags should describe when/where to wear it (e.g., "gym", "yoga", "running", "work", "casual", "date night", "travel", "lounging", "outdoor", "studio")
        
        Return ONLY a valid JSON object in this exact format:
        {{
          "style_tags": ["tag1", "tag2"],
          "occasion_tags": ["tag1", "tag2"]
        }}
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a fashion expert who categorizes clothing items with style and occasion tags. Always respond with valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.3
            )
            
            # Parse the JSON response
            tags_json = response.choices[0].message.content.strip()
            tags = json.loads(tags_json)
            
            return tags
            
        except Exception as e:
            print(f"Error generating tags for {product_name}: {e}")
            # Return default tags if API fails
            return {
                "style_tags": ["casual"],
                "occasion_tags": ["everyday"]
            }
    
    def enrich_catalog(self, input_file='catalog.json', output_file='catalog_enriched.json'):
        """Enrich the entire product catalog with GPT-4 tags"""
        
        # Load the catalog
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                products = json.load(f)
        except FileNotFoundError:
            print(f"Error: {input_file} not found. Please run import_google_sheets.py first.")
            return
        
        print(f"Enriching {len(products)} products with GPT-4 tags...")
        
        enriched_products = []
        
        for i, product in enumerate(products):
            print(f"Processing product {i+1}/{len(products)}: {product.get('name', 'Unknown')}")
            
            # Generate tags
            tags = self.generate_tags(
                product_name=product.get('name', ''),
                description=product.get('description', ''),
                brand=product.get('brand', ''),
                category=product.get('category', '')
            )
            
            # Add tags to product
            enriched_product = product.copy()
            enriched_product.update(tags)
            enriched_products.append(enriched_product)
            
            # Add a small delay to avoid rate limiting
            time.sleep(1)
        
        # Save enriched catalog
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(enriched_products, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully enriched catalog saved to {output_file}")
        return enriched_products

def main():
    enricher = ProductEnricher()
    enricher.enrich_catalog()

if __name__ == "__main__":
    main()