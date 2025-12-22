import pickle
import faiss
import numpy as np
import requests
from sentence_transformers import SentenceTransformer

INDEX_FILE = "data/index/faiss.index"
CHUNKS_FILE = "data/index/chunks.pkl"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "mistral"

TOP_K = 4  # number of relevant chunks to retrieve

# Load FAISS index and chunks
index = faiss.read_index(INDEX_FILE)

with open(CHUNKS_FILE, "rb") as f:
    chunks = pickle.load(f)

# Load embedding model (must match embed.py)
embedder = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve_chunks(question):
    question_embedding = embedder.encode([question])
    distances, indices = index.search(
        np.array(question_embedding).astype("float32"),
        TOP_K
    )
    return [chunks[i] for i in indices[0]]


def ask_mistral(question, context_chunks):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are an expert assistant.
Answer the question strictly using the context below.
Be direct, tactical, and practical.
If the answer is not in the context, say you do not know.

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

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]


if __name__ == "__main__":
    print("Document Q&A Agent (type 'exit' to quit)\n")

    while True:
        question = input("Question: ").strip()
        if question.lower() in {"exit", "quit"}:
            break

        retrieved = retrieve_chunks(question)
        answer = ask_mistral(question, retrieved)

        print("\nAnswer:\n")
        print(answer)
        print("\n" + "-" * 50 + "\n")

