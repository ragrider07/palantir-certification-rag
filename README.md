# Palantir Certification RAG

A Retrieval-Augmented Generation (RAG) project designed to help prepare for Palantir Data Engineering and Application Developer certifications.

## What this project does
- Ask Palantir certification-style questions
- Get answers grounded in reference documents
- Use the same backend for CLI and UI

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt






# How to Run the **Palantir Certification RAG**

GitHub repo:
👉 **[https://github.com/ragrider07/palantir-certification-rag](https://github.com/ragrider07/palantir-certification-rag)**

---

## Prerequisites (One-time)

Make sure you have:

* **Python 3.9+**

  ```bash
  python3 --version
  ```
* **Git**

  ```bash
  git --version
  ```

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/ragrider07/palantir-certification-rag.git
cd palantir-certification-rag
```

---

## Step 2 — Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

You should now see `(venv)` in your terminal.

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Configure Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit it:

```bash
nano .env
```

Add your API key (example):

```env
OPENAI_API_KEY=your_api_key_here
```

Save and exit.

---

## Step 5 — Build the Vector Index (Important)

This step processes the documents and builds the FAISS index.

```bash
python src/ingest.py
```

(If there is a web ingestion script, run that instead as documented.)

---

## Step 6 — Run the RAG

### Option A — Streamlit UI (Recommended)

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

### Option B — CLI Mode

```bash
python src/query.py
```

Type questions directly in the terminal.

---

## What This RAG Is For

* Practice **Palantir Data Engineering & Application Developer** certification questions
* Ask **scenario-based questions**
* Get **document-grounded answers**
* Modify prompts, retrieval depth, or embeddings freely

---

## Common Issues & Fixes

### Streamlit port already in use

```bash
lsof -i :8501
Ctrl + C
```

### Forgot to activate venv

```bash
source venv/bin/activate
```

### Rebuild index after adding documents

```bash
python src/ingest.py
```

---

## How to Modify / Extend

* **Change prompt logic** → `src/query.py`
* **Change embedding model** → `src/embed.py`
* **Add new documents** → put them in the data source folder, then re-run ingestion
* **UI changes** → `app.py`

---

## How to Contribute Back (Optional)

```bash
git checkout -b feature-my-changes
# make changes
git commit -m "Improve retrieval logic"
git push origin feature-my-changes
```

Open a Pull Request on GitHub.

---

## One-Line Quick Start (For Power Users)

```bash
git clone https://github.com/ragrider07/palantir-certification-rag.git && \
cd palantir-certification-rag && \
python3 -m venv venv && source venv/bin/activate && \
pip install -r requirements.txt && \
cp .env.example .env && \
python src/ingest.py && \
streamlit run app.py
```

---


> “Clone the repo, create a venv, install requirements, add your API key, run ingestion once, then start Streamlit.”

That’s it.






































Below is a **clean, copy-paste-ready set of instructions** you can send to your friends so they can **successfully clone, run, and modify your Palantir Certification RAG** without confusion.

You can share this **as-is** via WhatsApp, Slack, email, or in the GitHub README.

---

# How to Run the **Palantir Certification RAG**

GitHub repo:
👉 **[https://github.com/ragrider07/palantir-certification-rag](https://github.com/ragrider07/palantir-certification-rag)**

---

## Prerequisites (One-time)

Make sure you have:

* **Python 3.9+**

  ```bash
  python3 --version
  ```
* **Git**

  ```bash
  git --version
  ```

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/ragrider07/palantir-certification-rag.git
cd palantir-certification-rag
```

---

## Step 2 — Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

You should now see `(venv)` in your terminal.

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Configure Environment Variables

Create a `.env` file from the example:

```bash
cp .env.example .env
```

Edit it:

```bash
nano .env
```

Add your API key (example):

```env
OPENAI_API_KEY=your_api_key_here
```

Save and exit.

---

## Step 5 — Build the Vector Index (Important)

This step processes the documents and builds the FAISS index.

```bash
python src/ingest.py
```

(If there is a web ingestion script, run that instead as documented.)

---

## Step 6 — Run the RAG

### Option A — Streamlit UI (Recommended)

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

### Option B — CLI Mode

```bash
python src/query.py
```

Type questions directly in the terminal.

---

## What This RAG Is For

* Practice **Palantir Data Engineering & Application Developer** certification questions
* Ask **scenario-based questions**
* Get **document-grounded answers**
* Modify prompts, retrieval depth, or embeddings freely

---

## Common Issues & Fixes

### Streamlit port already in use

```bash
lsof -i :8501
Ctrl + C
```

### Forgot to activate venv

```bash
source venv/bin/activate
```

### Rebuild index after adding documents

```bash
python src/ingest.py
```

---

## How to Modify / Extend

* **Change prompt logic** → `src/query.py`
* **Change embedding model** → `src/embed.py`
* **Add new documents** → put them in the data source folder, then re-run ingestion
* **UI changes** → `app.py`

---

## How to Contribute Back (Optional)

```bash
git checkout -b feature-my-changes
# make changes
git commit -m "Improve retrieval logic"
git push origin feature-my-changes
```

Open a Pull Request on GitHub.

---

## One-Line Quick Start (For Power Users)

```bash
git clone https://github.com/ragrider07/palantir-certification-rag.git && \
cd palantir-certification-rag && \
python3 -m venv venv && source venv/bin/activate && \
pip install -r requirements.txt && \
cp .env.example .env && \
python src/ingest.py && \
streamlit run app.py
```

---


> “Clone the repo, create a venv, install requirements, add your API key, run ingestion once, then start Streamlit.”

That’s it.

---


