# 👗 AI Fashion Stylist (GPT-4 + CLIP + Streamlit)

An intelligent virtual stylist that recommends fashion items based on **user preferences**, **style**, and **occasion** using **GPT-4** and optionally **CLIP-based image search**.

This project simulates a virtual fashion assistant for e-commerce or personal styling. It can:
- Scrape product catalogs from athleisure brands like Alo Yoga, Lululemon, etc.
- Use GPT-4 to enrich items with style and occasion tags
- Recommend outfits based on user inputs via a simple Streamlit interface
- (Optional) Accept an image and return similar products using CLIP image embeddings

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
git clone https://github.com/yourname/ai-stylist.git
cd ai-stylist

### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up environment
Create a .env file with your OpenAI key:
OPENAI_API_KEY=your-api-key-here

### 4. Scrape data
python scrape_catalog.py

### 5. Enrich catalog using GPT
python enrich_with_gpt.py

### 6. Run the Streamlit app
streamlit run app.py

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
