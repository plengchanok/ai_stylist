"""
Setup script to initialize the AI Stylist project
"""
import os
import json
from import_google_sheets import import_from_google_sheets

def setup_project():
    """Initialize the project with sample data and configuration"""
    
    print("🚀 Setting up AI Fashion Stylist...")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("📝 Creating .env file from template...")
        with open('.env.example', 'r') as template:
            content = template.read()
        with open('.env', 'w') as env_file:
            env_file.write(content)
        print("✅ .env file created. Please add your OpenAI API key.")
    
    # Import product data
    if not os.path.exists('catalog.json'):
        print("📊 Importing product data...")
        import_from_google_sheets()
    else:
        print("✅ Product catalog already exists.")
    
    # Check if enriched catalog exists
    if not os.path.exists('catalog_enriched.json'):
        print("🤖 To use AI features, run: python enrich_with_gpt.py")
        print("   (Make sure to set your OPENAI_API_KEY in .env first)")
    else:
        print("✅ Enriched catalog already exists.")
    
    print("\n🎉 Setup complete!")
    print("\nNext steps:")
    print("1. Add your OpenAI API key to .env file")
    print("2. Run: python enrich_with_gpt.py (to add AI tags)")
    print("3. Run: streamlit run app.py (to start the app)")
    print("\nOr run the app directly with: streamlit run app.py")

if __name__ == "__main__":
    setup_project()