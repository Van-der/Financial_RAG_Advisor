# query.py
import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import Ollama

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR = os.path.join(SCRIPT_DIR, "faiss_index")

def query_rag(question: str):
    embeddings = SentenceTransformerEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        INDEX_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    docs = retriever.invoke(question)

    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
Answer the question using ONLY the context below.
If the answer is not present, say: Not found in documents.

Context:
{context}

Question:
{question}
"""

    llm = Ollama(model="ministral-3", temperature=0)
    return llm.invoke(prompt)

if __name__ == "__main__":
    while True:
        q = input("Query: ")
        print(query_rag(q))
        print("-" * 80)
