# 👗 AI Fashion Stylist (GPT-4 + Streamlit)

An intelligent virtual stylist that recommends fashion items based on **user preferences**, **style**, and **occasion** using **GPT-4** for intelligent product tagging and recommendations.

This project creates a comprehensive virtual fashion assistant with a **fully functional Streamlit web interface** that includes:
- 🎯 **Style Recommendations** - Smart filtering by style, occasion, category, and brand
- 👔 **Create Outfit** - AI-powered complete outfit generation
- 💬 **AI Styling Advice** - Personalized fashion guidance using GPT-4
- 🔍 **Browse Catalog** - Search and explore the full product catalog
- 📊 **Data Management** - Import from Google Sheets or CSV with AI enrichment

---

## 🚀 Key Features

### 🎯 **Style Recommendations**
- Advanced filtering system by style (casual, formal, sporty), occasion (everyday, workout, date night), category, and brand
- Intelligent recommendation engine that finds matching products
- Clean grid layout with product images, prices, and AI-generated tags

### 👔 **Create Outfit**
- AI-powered outfit generation that creates complete 3-item looks
- Intelligent coordination of tops, bottoms, and accessories
- Multiple outfit variations with proper styling logic

### 💬 **AI Styling Advice**
- Conversational interface powered by GPT-4
- Personalized fashion advice based on user queries
- Context-aware recommendations using the product catalog

### 🔍 **Browse Catalog**
- Full product catalog with search functionality
- Filter by brand names (Nike, Lululemon, Alo Yoga, etc.)
- Product cards with images, descriptions, prices, and AI tags

### 📊 **Data Management**
- Import product data from Google Sheets or CSV files
- GPT-4 powered product enrichment with style and occasion tags
- Sample dataset included with 16 curated fashion products

---

## 🧠 Tech Stack

| Component        | Technology |
|------------------|------------|
| **Frontend**     | Streamlit |
| **Backend**      | Python |
| **AI/ML**        | OpenAI GPT-4 API |
| **Data Handling** | Pandas, JSON |
| **Data Sources** | Google Sheets, CSV |
| **Web Requests** | Requests, BeautifulSoup4 |
| **Environment**  | python-dotenv |

---

## 📁 Project Structure

```
ai_stylist/
├── app.py                    # Main Streamlit application
├── stylist_backend.py        # Core recommendation engine
├── enrich_with_gpt.py        # GPT-4 product enrichment
├── import_google_sheets.py   # Google Sheets data import
├── import_csv.py             # CSV data import
├── create_sample_data.py     # Sample dataset generator
├── setup.py                  # Environment setup utility
├── demo.py                   # Quick demo script
├── catalog.json              # Raw product data
├── catalog_enriched.json     # AI-enriched product data
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variables template
└── README.md                 # This file
```

---

## ⚙️ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/plengchanok/ai_stylist.git
cd ai_stylist
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment (Optional - for AI features)
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key for full AI functionality
```

### 4. Run the application
```bash
streamlit run app.py
```

The app will start at `http://localhost:8501` with a sample dataset of 16 fashion products ready to use!

---

## 🔧 Detailed Setup

### Environment Configuration

Create a `.env` file for full AI functionality:
```bash
# Required for AI Styling Advice feature
OPENAI_API_KEY=your-openai-api-key-here

# Optional: For Google Sheets import
GOOGLE_SHEETS_ID=your-google-sheets-id
GOOGLE_SHEETS_GID=your-sheet-gid
```

### Data Import Options

#### Option A: Use Sample Data (Recommended for testing)
The app comes with a pre-loaded sample dataset of 16 fashion products from major brands (Nike, Lululemon, Alo Yoga, etc.). No additional setup required!

#### Option B: Import from Google Sheets
```bash
python import_google_sheets.py
```

#### Option C: Import from CSV
```bash
python import_csv.py your_products.csv
```

### AI Enrichment (Optional)
Enhance your product catalog with GPT-4 generated style and occasion tags:
```bash
python enrich_with_gpt.py
```
*Note: Requires OpenAI API key*

---

## 📊 Using Your Google Sheets Data

To use your existing Google Sheets data (like the example: https://docs.google.com/spreadsheets/d/1G4cuYs_7qD1ft6OEhovLjj8zowQc92yYHQz2gSmLpp8/edit?gid=715689617#gid=715689617):

### 1. Make your Google Sheets publicly accessible
- Open your Google Sheets
- Click "Share" → "Change to anyone with the link"
- Set permission to "Viewer"

### 2. Extract Sheet ID and GID from URL
From URL: `https://docs.google.com/spreadsheets/d/1G4cuYs_7qD1ft6OEhovLjj8zowQc92yYHQz2gSmLpp8/edit?gid=715689617`
- **Sheet ID**: `1G4cuYs_7qD1ft6OEhovLjj8zowQc92yYHQz2gSmLpp8`
- **GID**: `715689617`

### 3. Update .env file
```bash
GOOGLE_SHEETS_ID=1G4cuYs_7qD1ft6OEhovLjj8zowQc92yYHQz2gSmLpp8
GOOGLE_SHEETS_GID=715689617
```

### Expected Data Format
Your spreadsheet should include these columns:
- `name` - Product name
- `brand` - Brand name  
- `price` - Price (e.g., "$88")
- `description` - Product description
- `category` - Product category (e.g., "Leggings", "Tops")
- `color` - Product color
- `image_url` - Product image URL
- `size` - Available sizes (optional)
- `material` - Material composition (optional)

---

## 🎮 How to Use the App

### 1. **Browse Catalog Tab**
- View all products in a clean grid layout
- Search by brand name (try "Nike" or "Lululemon")
- See product images, prices, descriptions, and AI-generated tags

### 2. **Style Recommendations Tab**
- Filter by style: casual, formal, sporty
- Filter by occasion: everyday, workout, date night
- Filter by category: tops, bottoms, accessories
- Filter by brand: Nike, Lululemon, Alo Yoga, etc.
- Get intelligent product recommendations

### 3. **Create Outfit Tab**
- Generate complete 3-item outfits automatically
- Get coordinated looks with tops, bottoms, and accessories
- Create multiple outfit variations

### 4. **AI Styling Advice Tab**
- Chat with GPT-4 for personalized fashion advice
- Ask questions like "What should I wear for a casual date?"
- Get context-aware recommendations from your catalog
- *Requires OpenAI API key*

---

## 🧪 Sample Products Included

The app comes with 16 curated fashion products:

**Brands**: Alo Yoga, Lululemon, Athleta, Nike, Outdoor Voices, Hydro Flask, Manduka  
**Categories**: Leggings, Tops, Hoodies, Shoes, Accessories, Equipment  
**Price Range**: $35 - $118  
**All items include**: High-quality images, detailed descriptions, AI-generated style/occasion tags

---

## 🔮 AI-Powered Features

### GPT-4 Product Enrichment
Each product is automatically enhanced with:
- **Style tags**: casual, formal, sporty, minimal, etc.
- **Occasion tags**: everyday, workout, date night, office, etc.

### Intelligent Recommendations
- Context-aware filtering and matching
- Style compatibility analysis
- Occasion-appropriate suggestions

### Conversational Styling
- Natural language fashion advice
- Personalized recommendations
- Product-specific guidance

---

## 🚀 Deployment

### Local Development
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add your environment variables in the Streamlit Cloud dashboard
4. Deploy!

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🛠️ Development

### Adding New Features
The modular design makes it easy to extend:

- **New data sources**: Add importers in the style of `import_csv.py`
- **Enhanced AI**: Modify `enrich_with_gpt.py` for additional AI features
- **UI improvements**: Extend `app.py` with new Streamlit components
- **Recommendation logic**: Enhance `stylist_backend.py` algorithms

### Testing
```bash
# Test with sample data
python create_sample_data.py
python demo.py

# Test data import
python import_csv.py sample_data.csv

# Test AI enrichment (requires API key)
python enrich_with_gpt.py
```

---

## 📈 Future Enhancements

- 🖼️ **Image similarity search** with CLIP embeddings
- 🌤️ **Weather-aware recommendations** using weather APIs
- 📱 **Mobile-responsive design** improvements
- 🛒 **Shopping cart functionality** for e-commerce integration
- 📊 **Analytics dashboard** for style trends and insights
- 🤖 **Chatbot integration** for messaging platforms

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Pleng Witayaweerasak**  
- LinkedIn: [pimchanokw](https://www.linkedin.com/in/pimchanokw/)
- GitHub: [plengchanok](https://github.com/plengchanok)

Feel free to reach out for collaborations or questions!

---

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- Streamlit for the amazing web framework
- Fashion brands for product inspiration
- Open source community for tools and libraries

---

*Built with ❤️ and AI*