# 📄 RAG-Based PDF Question Answering Chatbot

This project is a simple **PDF-based question answering chatbot** built as part of my learning in Retrieval-Augmented Generation (RAG).
The goal is straightforward: upload a PDF, ask questions about it, and receive answers that are grounded in the document itself.

The application uses **Streamlit** for the interface, **LangChain** for managing the RAG pipeline,
**Milvus** for vector storage, and **Google Gemini** as the language model.

---

## 🧩 What This Project Does

- Allows users to upload a PDF document  
- Splits the document into smaller, meaningful text chunks  
- Converts text chunks into embeddings  
- Stores embeddings in a vector database  
- Retrieves relevant sections based on user questions  
- Generates answers using a large language model  

All interactions happen through a simple chat-style interface.

---

## 🔧 Technologies Used

- **Streamlit** – interactive web application  
- **LangChain** – document processing and retrieval logic  
- **Google Gemini (gemini-1.5-flash)** – answer generation  
- **HuggingFace Sentence Transformers** – text embeddings  
- **Milvus** – vector database  
- **PyPDFLoader** – PDF loading and parsing  

---

## 📁 Project Structure

```
RAG-PROJECT/
│
├── chromadb/          # Vector database directory (for embeddings storage)
├── Docker-Milvus/     # Docker setup and configuration files for Milvus
├── tempDir/           # Temporary folder to store uploaded PDF files
│
├── app.py             # Main Streamlit application (PDF upload + chat logic)
├── README.md          # Project documentation

```

---

## ⚙️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-Project1-RAG-based-AI-Chatbot.git
cd AI-Project1-RAG-based-AI-Chatbot
```

---

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
```

```bash
venv\Scripts\activate     # Windows
source venv/bin/activate   # macOS / Linux
```

---

### 3. Install Required Dependencies
```bash
pip install streamlit langchain langchain-milvus sentence-transformers langchain-google-genai pymilvus pypdf
```

---

### 4. Start Milvus

Milvus must be running locally on port `19530`.

Using Docker:
```bash
docker compose up -d
```

---

### 5. Set Google API Key

Set your API key as an environment variable.

```bash
export GOOGLE_API_KEY="your_api_key"   # macOS/Linux
set GOOGLE_API_KEY=your_api_key        # Windows
```

---

### 6. Run the Application
```bash
streamlit run app.py
```

Once the app starts, upload a PDF and begin chatting with it.

---

## 🧠 How It Works (High Level)

1. User uploads a PDF  
2. PDF is split into overlapping chunks  
3. Each chunk is converted into an embedding  
4. Embeddings are stored in Milvus  
5. Relevant chunks are retrieved for each question  
6. The language model generates an answer based on retrieved content  

---

## 🎨 Interface Overview

- Chat-style layout  
- User questions and model answers are visually separated  
- Chat history is preserved during the session  
- Loading indicators show when answers are being generated  

---

## 🔐 Security Notes

- API keys should not be hardcoded in real deployments  
- Environment variables or `.env` files are recommended  
- This project is intended mainly for learning and experimentation  

---

## 🔮 Possible Improvements

- Support for multiple PDFs  
- Showing source text along with answers  
- Cloud deployment  
- User authentication  
- Chat export functionality  

---

## 👨‍💻 Author

NANDAYALA VAMSI KRISHNA YADAV

AI & ML Engineer | B.Tech Computer Science and Engineering (AI & ML)
---

## 📜 Disclaimer

This project was created for **educational purposes** to understand and practice
Retrieval-Augmented Generation and document-based question answering.
