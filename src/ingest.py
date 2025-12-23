import os
from pypdf import PdfReader

RAW_DIR = "data/raw"
WEB_DIR = "data/raw/web"
OUT_FILE = "data/processed/documents.txt"

os.makedirs("data/processed", exist_ok=True)

all_text = []

def read_txt_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read().strip()
                    if text:
                        all_text.append(text)

def read_pdf_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                path = os.path.join(root, file)
                reader = PdfReader(path)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        all_text.append(text)

# Read local raw text
read_txt_files(RAW_DIR)

# Read web-ingested text
if os.path.exists(WEB_DIR):
    read_txt_files(WEB_DIR)

# Read PDFs (if any)
read_pdf_files(RAW_DIR)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_text))

print(f"Ingested {len(all_text)} documents into {OUT_FILE}")



