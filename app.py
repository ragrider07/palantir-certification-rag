import streamlit as st
import pickle
import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

# ---------------- CONFIG ----------------
INDEX_FILE = "data/index/faiss.index"
CHUNKS_FILE = "data/index/chunks.pkl"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "mistral"
TOP_K = 4
# ----------------------------------------

@st.cache_resource
def load_resources():
    index = faiss.read_index(INDEX_FILE)
    with open(CHUNKS_FILE, "rb") as f:
        chunks = pickle.load(f)
    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    return index, chunks, embedder

index, chunks, embedder = load_resources()

def retrieve_chunks(question):
    q_embedding = embedder.encode([question])
    distances, indices = index.search(
        np.array(q_embedding).astype("float32"),
        TOP_K
    )
    return [chunks[i] for i in indices[0]]

def ask_mistral(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
Answer the question using only the context below.
If the answer is not present, say you do not know.

Context:
{context}

Question:
{question}

Answer:
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()
    return r.json()["response"]

# ---------------- UI ----------------
st.set_page_config(page_title="Document RAG", layout="wide")
st.title("📄 Document Q&A Assistant")

question = st.text_input("Ask a question based on the documents:")

if question:
    with st.spinner("Searching documents..."):
        retrieved = retrieve_chunks(question)
        answer = ask_mistral(question, retrieved)

    st.subheader("Answer")
    st.write(answer)

    with st.expander("Retrieved context"):
        for chunk in retrieved:
            st.markdown("---")
            st.write(chunk)

