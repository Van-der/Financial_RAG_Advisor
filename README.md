# Grounded Financial Document Question Answering (RAG)

A **strictly grounded Retrieval-Augmented Generation (RAG)** system for answering factual questions over financial documents such as annual reports and regulatory filings.

The system is designed to **eliminate hallucinations** by enforcing a simple rule:

> **If an answer is not explicitly present in the documents, it will not be generated.**

---

## Overview

This project implements an end-to-end RAG pipeline that ingests financial documents, retrieves relevant context using semantic search, and generates answers using a **locally hosted large language model**.

All responses are grounded in retrieved document text.  
If the information required to answer a question is missing, the system refuses to answer.

The entire pipeline runs **fully offline**, without relying on external LLM APIs.

---

## Key Capabilities

- Financial document ingestion (PDF / TXT)
- Semantic chunking with overlap
- Dense vector embeddings and FAISS-based retrieval
- Local LLM inference using Ollama (Mistral)
- Strict grounding and refusal-based hallucination control

---

## Technologies Used

- **Python 3.10+**
- **LangChain** – RAG orchestration
- **FAISS** – vector similarity search
- **SentenceTransformers** – text embeddings
- **Ollama** – local LLM serving
- **Mistral (Ministral-3)** – language model

---

## System Pipeline

1. Load financial documents from disk
2. Split documents into overlapping text chunks
3. Generate embeddings for each chunk
4. Store embeddings in a FAISS index
5. Retrieve top-k relevant chunks for a query
6. Generate an answer strictly from retrieved context

---

## Project Structure

```text
Genai_patham/
├── data/
│   └── docs/                    # Financial source documents
│       ├── nvidia_10k.txt
│       └── NVIDIA-2025-Annual-Report.pdf
│
├── faiss_index/                 # Persisted FAISS vector store
│   ├── index.faiss
│   └── index.pkl
│
├── notebooks/
│   └── training.ipynb           # Development and experimentation
│
├── ingest.py                    # Document ingestion and indexing
├── query.py                     # CLI interface for querying the system
│
├── requirements.txt
├── README.md
└── .gitignore


## Setup

### 1. Clone the repository
```bash
git clone https://github.com/Van-der/Financial_RAG_Advisor.git
cd Financial_RAG_Advisor

2. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\activate       # Windows

3. Install dependencies

pip install -r requirements.txt

4. Install and start Ollama

ollama pull ministral-3
ollama serve

## Usage

### Step 1: Index documents

Run this once (or whenever documents change):

```bash
python ingest.py
```

This builds and stores the FAISS index in `faiss_index/`.

---

### Step 2: Query the system

```bash
python query.py
```

**Example queries**

```
By what percentage did NVIDIA’s revenue grow year-over-year in Fiscal 2025?
What major industry shift drove NVIDIA’s performance in Fiscal 2025?
What is NVIDIA’s stock price today?
```

---

## Grounding and Hallucination Control

The system enforces strict grounding:

* Answers are generated **only from retrieved document chunks**
* No external knowledge or assumptions are allowed
* If the answer is not explicitly present, the system responds with:

```
Not found in documents.
```

This behavior is enforced through both prompt constraints and programmatic guardrails.

---

## Current Limitations

* No source citations or page numbers
* CLI-only interface
* Single-domain focus (financial filings)

---

## Possible Extensions

* Add citations (page number + text snippet)
* Streamlit or web-based UI
* Dockerized deployment
* Multi-agent verification using LangGraph
* Support for additional document formats

---

## License

This project is released under the **MIT License**.

```

---
```
