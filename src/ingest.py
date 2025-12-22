import os
from pypdf import PdfReader

RAW_DIR = "data/raw"
OUT_FILE = "data/processed/documents.txt"

def read_pdf(path):
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)
    return "\n".join(pages)

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

documents = []

for filename in os.listdir(RAW_DIR):
    path = os.path.join(RAW_DIR, filename)

    if filename.lower().endswith(".pdf"):
        print(f"Reading PDF: {filename}")
        documents.append(read_pdf(path))

    elif filename.lower().endswith((".txt", ".md")):
        print(f"Reading text: {filename}")
        documents.append(read_text(path))

os.makedirs("data/processed", exist_ok=True)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n\n".join(documents))

print("Ingestion complete.")



