Great — this structure is now **clean, correct, and professional**.
I’ll first **confirm the structure**, then give you a **single, final `README.md`** that matches it **exactly** (no placeholders, no contradictions).

---

## ✅ Verified File Structure (What You Have Now)

From your screenshot, the project looks like this:

```
Genai_patham/
├── data/
│   └── docs/
│       ├── nvidia_10k.txt
│       └── NVIDIA-2025-Annual-Report.pdf
│
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
│
├── notebooks/
│   └── training.ipynb
│
├── ingest.py
├── query.py
├── README.md
├── requirements.txt
└── .gitignore
```

This is **exactly what a solid RAG repo should look like**.
Now the README below is aligned 1:1 with this.

---

# ✅ FINAL `README.md` (Single Markdown File)

You can **replace your current README.md entirely** with this.

````md
# Grounded Financial Document Question Answering (RAG)

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline for answering factual questions over financial documents with **strict grounding to source text**.

The system is designed to avoid hallucinations by returning an answer **only if the information is explicitly present in the documents**. Otherwise, it responds with a fixed refusal message.

---

## Overview

The pipeline ingests financial documents (PDF and text), splits them into overlapping chunks, embeds them into a vector space, retrieves relevant context using similarity search, and generates grounded answers using a **locally hosted large language model**.

The entire system runs **fully offline**, without relying on external LLM APIs.

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

1. Load financial documents (PDF / TXT)
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
├── query.py                     # CLI interface for RAG queries
│
├── requirements.txt
├── README.md
└── .gitignore
````

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Genai_patham.git
cd Genai_patham
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and start Ollama

```bash
ollama pull ministral-3
ollama serve
```

---

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
