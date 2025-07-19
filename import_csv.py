"""
Import product data from a CSV file (for when Google Sheets is not publicly accessible)
"""
import pandas as pd
import json
import sys

def import_from_csv(csv_file_path):
    """Import data from a CSV file and convert to JSON format"""
    
    try:
        # Read the CSV data
        print(f"Importing data from {csv_file_path}...")
        df = pd.read_csv(csv_file_path)
        
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
        print(f"Error importing from CSV: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_csv.py <csv_file_path>")
        print("Example: python import_csv.py products.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    import_from_csv(csv_file)