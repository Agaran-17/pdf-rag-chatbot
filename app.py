import os
import streamlit as st

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI
)



load_dotenv()

st.title("📚 PDF Chatbot using RAG")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)

if uploaded_file:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    loader = PyPDFLoader(uploaded_file.name)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

    vectorstore = FAISS.from_documents(
        docs,
        embeddings
    )

    question = st.text_input(
        "Ask a question from the PDF"
    )
    if question:

        matched_docs = vectorstore.similarity_search(
        question
    )

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.2
        )

        context = "\n\n".join(
            [doc.page_content for doc in matched_docs]
        )

        prompt = f"""
    Answer the question only using the provided context.

    Context:
    {context}

    Question:
    {question}
    """

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)