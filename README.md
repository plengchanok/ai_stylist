# 👗 AI Fashion Stylist (GPT-4 + Streamlit)

An intelligent virtual stylist that recommends fashion items based on **user preferences**, **style**, and **occasion** using **GPT-4** for intelligent product tagging and recommendations.

This project creates a virtual fashion assistant that can:
- Import product catalogs from Google Sheets or CSV files
- Use GPT-4 to enrich items with intelligent style and occasion tags
- Recommend outfits based on user inputs via an intuitive Streamlit interface
- Provide personalized AI styling advice
- Create complete outfit combinations

---

## 🚀 Features

- 🔎 **Web scraping** with Selenium and BeautifulSoup
- 💡 **Data enrichment** using GPT-4 for styling & occasion metadata
- 🎯 **Style-based filtering** for recommendations
- 💬 **Conversational interface** with Streamlit
- 🖼️ *(Optional)* CLIP-based image similarity for “shop the look” use case
- 🔧 Modular design for easy extension (e.g., chatbot, dashboards)

---

## 🧠 Tech Stack

| Layer            | Tools & Libraries |
|------------------|-------------------|
| Web Scraping     | Selenium, BeautifulSoup |
| Data Handling    | JSON, Pandas |
| LLM Integration  | OpenAI GPT-4 API |
| UI               | Streamlit |
| Image Matching   | (Optional) OpenAI CLIP via Hugging Face |
| Vector Search    | (Optional) FAISS |
| Hosting (UI)     | Streamlit Cloud, Hugging Face Spaces |

---

## 📁 Project Structure

ai_stylist_project/
├── scrape_catalog.py         # Scrape fashion products
├── enrich_with_gpt.py        # Add GPT-4 tags to products
├── stylist_backend.py        # Filtering logic
├── app.py                    # Streamlit UI
├── catalog.json              # Raw product data
├── catalog_enriched.json     # Enriched product data with tags
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/plengchanok/ai_stylist.git
cd ai_stylist
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment
Create a .env file with your OpenAI key:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
OPENAI_API_KEY=your-api-key-here
```

### 4. Import your product data

#### Option A: From Google Sheets (if publicly accessible)
```bash
python import_google_sheets.py
```

#### Option B: From CSV file
```bash
python import_csv.py your_products.csv
```

#### Option C: Use sample data for testing
```bash
python create_sample_data.py
```

### 5. Enrich catalog using GPT-4
```bash
python enrich_with_gpt.py
```

### 6. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 📊 Using Your Google Sheets Data

To use your existing Google Sheets data:

1. **Make your Google Sheets publicly accessible:**
   - Open your Google Sheets
   - Click "Share" → "Change to anyone with the link"
   - Set permission to "Viewer"

2. **Update the .env file with your sheet details:**
   ```
   GOOGLE_SHEETS_ID=1G4cuYs_7qD1ft6OEhovLjj8zowQc92yYHQz2gSmLpp8
   GOOGLE_SHEETS_GID=715689617
   ```

3. **Or export as CSV:**
   - File → Download → Comma-separated values (.csv)
   - Use `python import_csv.py your_file.csv`

### Expected Data Format
Your spreadsheet should have columns like:
- `name` - Product name
- `brand` - Brand name
- `price` - Price (e.g., "$88")
- `description` - Product description
- `category` - Product category (e.g., "Leggings", "Tops")
- `color` - Product color
- `image_url` - Product image URL (optional)
- `size` - Available sizes (optional)
- `material` - Material composition (optional)

---

## 🖼️ Optional: Image Search with CLIP

To allow users to upload an image and get similar outfits:

1. Encode all catalog images using CLIP
2. Store the image embeddings in FAISS
3. Accept user-uploaded image → encode → search similar embeddings

You can extend the backend with:
pip install faiss-cpu transformers torch

---

## 🧪 Sample Prompt for GPT-4 Tagging

Given this product name and description:
"Airlift High-Waist Legging. Designed for movement and studio flow, with moisture-wicking, ultra-smooth fabric."

Assign style and occasion tags in this format:
{
  "style_tags": ["minimal", "athleisure"],
  "occasion_tags": ["yoga", "gym"]
}

---

## ✨ Possible Extensions

- Add CLIP image similarity search
- Chatbot-style interface (e.g., LangChain + GPT-4)
- Integrate Braze / Mixpanel for behavioral styling
- Add weather + location awareness using APIs
- Build a LINE bot or Telegram bot stylist

---

## 📌 Example Use Cases

- **E-commerce**: Help users find relevant styles from product catalog
- **Personal stylist app**: User inputs preferences, gets outfit suggestions
- **Retail dashboard**: Style tag analytics, pricing trends, seasonality

---

## 📄 License
MIT License

---

## 👩‍💻 Maintainer
Built by [Pleng Witayaweerasak](https://www.linkedin.com/in/pimchanokw/)  
Feel free to reach out if you'd like to collaborate!
