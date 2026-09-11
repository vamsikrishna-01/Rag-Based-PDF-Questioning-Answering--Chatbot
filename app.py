# app.py
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
# from langchain.vectorstores import Chroma
from langchain_milvus import Milvus
from langchain_classic.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

# Set Google API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")

st.set_page_config(page_title="PDF Q&A Chat", page_icon="📄")
st.title("📘 Ask Your PDF - Chat")
st.write("Upload a PDF and chat with it!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    pdf_path = f"tempDir/{uploaded_file.name}"
    os.makedirs("tempDir", exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    # Load PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    chunks = text_splitter.split_documents(pages)
    st.info(f"PDF split into {len(chunks)} chunks.")

    # Embeddings & Vectorstore
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Milvus.from_documents(
        documents=chunks,
        embedding=embeddings,
        connection_args={"host": "localhost", "port": "19530"},
        collection_name="pdf_chunks",
        drop_old=True
    )
    retriever = vectorstore.as_retriever()
    st.success("Vectorstore ready!")

    # LLM
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0.7)
    chain = RetrievalQA.from_chain_type(retriever=retriever, llm=llm)

    # Scrollable chat container
    chat_container = st.container()

    # Function to handle user input
    def handle_query():
        query = st.session_state.query_input
        if query:
            with st.spinner("Generating answer..."):
                answer = chain.invoke(query)["result"]

            # Save chat
            st.session_state.messages.append({"role": "user", "content": query})
            st.session_state.messages.append({"role": "assistant", "content": answer})

            # Clear input box
            st.session_state.query_input = ""

    # Input box at bottom
    st.text_input(
        "Type your question here and press Enter:",
        key="query_input",
        on_change=handle_query
    )

    # Render chat history
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                # User message on right
                col1, col2 = st.columns([4,3])
                with col2:
                    st.markdown(
                        f"""
                        <div style='text-align:left; background-color:#E5E5EA; color:#000000; 
                                    padding:12px; border-radius:12px; margin:5px; display:inline-block; max-width:100%'>
                            {msg['content']}
                        </div>
                        """, unsafe_allow_html=True
                    )
            else:
                # Assistant message on left
                col1, col2 = st.columns([3,4])
                with col1:
                    st.markdown(
                        f"""
                        <div style='text-align:left; background-color:#34FF7A; color:#000000; 
                                    padding:12px; border-radius:12px; margin:5px; display:inline-block; max-width:100%; float:left'>
                            {msg['content']}
                        </div>
                        """, unsafe_allow_html=True
                    )

                    