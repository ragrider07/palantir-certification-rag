import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

INPUT_FILE = "data/processed/documents.txt"
INDEX_FILE = "data/index/faiss.index"
CHUNKS_FILE = "data/index/chunks.pkl"

# Load consolidated document text
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

# Split text into overlapping chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=450,
    chunk_overlap=100
)

chunks = splitter.split_text(text)
print(f"Total chunks created: {len(chunks)}")

# Load embedding model (runs fully locally)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
embeddings = model.encode(chunks, show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Persist index and chunks
os.makedirs("data/index", exist_ok=True)
faiss.write_index(index, INDEX_FILE)

with open(CHUNKS_FILE, "wb") as f:
    pickle.dump(chunks, f)

print("Embedding and indexing complete.")
