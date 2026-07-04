# 📚 PDF Chatbot using RAG

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content using Google's Gemini AI.

---

## 🚀 Features

- Upload PDF documents
- Extract and process PDF content
- Intelligent text chunking
- Vector embeddings using Gemini Embeddings
- Semantic search with FAISS
- AI-powered question answering
- Simple and interactive Streamlit UI

---

## 🏗️ Architecture

```text
PDF Upload
    ↓
PDF Loader
    ↓
Text Chunking
    ↓
Gemini Embeddings
    ↓
FAISS Vector Store
    ↓
Similarity Search
    ↓
Gemini LLM
    ↓
Answer Generation
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Google Gemini API
- PyPDF

---

## 📂 Project Structure

```text
pdf-rag-chatbot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Agaran-17/pdf-rag-chatbot.git
cd pdf-rag-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Demo

1. Upload a PDF document.
2. Enter a question related to the document.
3. Receive AI-generated answers based on the PDF content.

---

## 🎯 Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Document Processing
- Text Chunking
- Vector Embeddings
- Semantic Search
- Vector Databases
- LLM Integration
- Prompt Engineering

---

## 👨‍💻 Author

**Agaran**

B.Tech Artificial Intelligence & Data Science  
Velammal Engineering College

GitHub: https://github.com/Agaran-17
