import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

OUT_DIR = "data/raw/web"
os.makedirs(OUT_DIR, exist_ok=True)

def fetch_article(url):
    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            }
        )

        if response.status_code != 200:
            print(f"Skipping {url} (status {response.status_code})")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        title = soup.title.string.strip() if soup.title else "untitled"
        paragraphs = [
            p.get_text().strip()
            for p in soup.find_all("p")
            if p.get_text().strip()
        ]

        if not paragraphs:
            print(f"No readable content at {url}")
            return

        text = "\n".join(paragraphs)

        domain = urlparse(url).netloc.replace(".", "_")
        filename = f"{domain}_{title[:60].replace('/', '_')}.txt"

        with open(os.path.join(OUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(f"[URL: {url}]\n\n{text}")

        print(f"Saved article: {filename}")

    except Exception as e:
        print(f"Failed to fetch {url}: {e}")


# 👇 ADD YOUR URLS HERE
URLS = [
    "https://learn.palantir.com/?utm_source=chatgpt.com",
    "https://learn.palantir.com/data-engineer-guide-2023?utm_source=chatgpt.com",
"https://learn.palantir.com/app-dev-guide-2023?utm_source=chatgpt.com",
"https://learn.palantir.com/page/exam-guides?utm_source=chatgpt.com",
"https://learn.palantir.com/page/training-track-data-engineer?utm_source=chatgpt.com",
"https://learn.palantir.com/page/training-track-application-developer?utm_source=chatgpt.com",
"https://learn.palantir.com/foundry-application-developer-associate-quiz?utm_source=chatgpt.com",
"https://community.palantir.com/t/data-engineer-certification-preperation/2789?utm_source=chatgpt.com",
"https://quizlet.com/991711798/palantir-data-engineering-certification-exam-flashcards/?utm_source=chatgpt.com",
"https://quizlet.com/990528237/palantir-application-developer-flash-cards/?utm_source=chatgpt.com",
"https://www.udemy.com/course/ace-foundry-decx/?srsltid=AfmBOoo",
"https://community.palantir.com/t/mock-exams-for-palantir-data-engineer-certification/4776?utm_source=chatgpt.com",
"https://www.perplexity.ai/search/0a687caa-5a4d-4c1d-b2cf-cb4073c17a04",
"https://www.perplexity.ai/search/2fc0f550-76f7-49b7-8761-55c917f4eb52",
"https://www.perplexity.ai/search/f4b7e4f4-ce6d-4807-afbd-47d09b74a0be"
]

for url in URLS:
    fetch_article(url)

