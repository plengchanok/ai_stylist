"""
Import product data from Google Sheets and convert to JSON format
"""
import pandas as pd
import json
import os
from dotenv import load_dotenv

load_dotenv()

def import_from_google_sheets():
    """Import data from Google Sheets using the public CSV export URL"""
    
    # Get Google Sheets ID and GID from environment variables
    sheets_id = os.getenv('GOOGLE_SHEETS_ID', '1G4cuYs_7qD1ft6OEhovLjj8zowQc92yYHQz2gSmLpp8')
    gid = os.getenv('GOOGLE_SHEETS_GID', '715689617')
    
    # Construct the CSV export URL
    csv_url = f"https://docs.google.com/spreadsheets/d/{sheets_id}/export?format=csv&gid={gid}"
    
    try:
        # Read the CSV data
        print(f"Importing data from Google Sheets...")
        df = pd.read_csv(csv_url)
        
        # Clean and process the data
        df = df.dropna(how='all')  # Remove completely empty rows
        
        # Convert to list of dictionaries
        products = df.to_dict('records')
        
        # Clean up any NaN values
        for product in products:
            for key, value in product.items():
                if pd.isna(value):
                    product[key] = ""
        
        # Save to JSON file
        with open('catalog.json', 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        
        print(f"Successfully imported {len(products)} products to catalog.json")
        print(f"Sample product keys: {list(products[0].keys()) if products else 'No products found'}")
        
        return products
        
    except Exception as e:
        print(f"Error importing from Google Sheets: {e}")
        print("Please make sure the Google Sheets is publicly accessible or provide the correct URL")
        
        # Create a sample catalog for testing
        sample_products = [
            {
                "name": "Airlift High-Waist Legging",
                "brand": "Alo Yoga",
                "price": "$88",
                "description": "Designed for movement and studio flow, with moisture-wicking, ultra-smooth fabric.",
                "image_url": "https://example.com/image1.jpg",
                "category": "Leggings",
                "color": "Black"
            },
            {
                "name": "Align Tank Top",
                "brand": "Lululemon",
                "price": "$58",
                "description": "Buttery-soft Nulu fabric with built-in bra for light support.",
                "image_url": "https://example.com/image2.jpg",
                "category": "Tops",
                "color": "White"
            },
            {
                "name": "Everywhere Belt Bag",
                "brand": "Lululemon",
                "price": "$38",
                "description": "Hands-free storage for your essentials with adjustable strap.",
                "image_url": "https://example.com/image3.jpg",
                "category": "Accessories",
                "color": "Black"
            }
        ]
        
        with open('catalog.json', 'w', encoding='utf-8') as f:
            json.dump(sample_products, f, indent=2, ensure_ascii=False)
        
        print(f"Created sample catalog with {len(sample_products)} products")
        return sample_products

if __name__ == "__main__":
    import_from_google_sheets()