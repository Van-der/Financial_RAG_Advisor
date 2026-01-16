# ingest.py
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data", "docs")
INDEX_DIR = os.path.join(SCRIPT_DIR, "faiss_index")

def ingest():
    documents = []

    for file in os.listdir(DATA_DIR):
        path = os.path.join(DATA_DIR, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(path, encoding="utf-8")
            documents.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_DIR)

    print(f"Indexed {len(chunks)} chunks")

if __name__ == "__main__":
    ingest()
