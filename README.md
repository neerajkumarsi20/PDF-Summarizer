# 📄 PDF Summarizer & Q&A Chatbot (LLM + Embeddings)

This is a full-stack AI-powered application that allows users to:
- ✅ Upload a PDF
- ✅ Generate a summary using Hugging Face models
- ✅ Ask questions about the PDF
- ✅ Receive answers with source context using cosine similarity & embeddings
- ✅ Choose from multiple summarization and Q&A models
- ✅ Control summary length (min and max)

Built with:
- 🔥 FastAPI (backend)
- ⚡ React (frontend)
- 🤗 Hugging Face Inference API
- 🧠 Sentence Transformers (for embeddings)
- 📚 PyMuPDF (PDF parsing)

---

## 🚀 Features

- 📥 Upload any PDF and extract its content
- 🧠 Generate AI-based summaries using models like:
  - `facebook/bart-large-cnn`
  - `google/pegasus-cnn_dailymail`
  - `sshleifer/distilbart-cnn-12-6`
  - `csebuetnlp/mT5_multilingual_XLSum`
  - `philschmid/bart-large-cnn-samsum`
  - `Falconsai/text_summarization`
- 🎛️ Control summary length using sliders
- ❓ Ask questions from the PDF using a sentence-transformer embedding-based retrieval system
- 🔍 Source context shown for every answer

---

## 🗂️ Directory Structure

```
PDF-Summarizer/
│
├── backend/                     # FastAPI backend
│   ├── __pycache__/
│   ├── embedder.py             # Embedding logic for PDF chunks
│   ├── main.py                 # FastAPI app entry point
│   ├── qa.py                   # Question-answering logic
│   ├── summarizer.py           # Summarization logic
│
├── frontend/
│   └── pdf-ui-react/           # React frontend
│       ├── public/             
│       │   ├── index.html
│       ├── src/                # React components and logic 
│       ├── package.json
│       ├── package-lock.json
│       ├── .gitignore
│       
│
├── requirements.txt            # Python dependencies
├── LICENSE.txt
├── .gitignore
└── README.md                   # Project documentation

```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/neerajkumarsi20/PDF-Summarizer
cd PDF-Summarizer
```

### ✅ 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### ✅ 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### ✅ 4. Add Your Hugging Face API Key

Create a `.env` file inside the `backend/` folder:

```env
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
```

> 🔒 Make sure `.env` is included in `.gitignore`

---

## ▶️ Run the App

### Step 1: Start the FastAPI backend

```bash
cd backend
uvicorn main:app --reload
```

### Step 2: Start the React frontend

```bash
cd frontend/pdf-ui-react
npm install
npm start
```

Now open `http://localhost:8501` to use the app.

---


