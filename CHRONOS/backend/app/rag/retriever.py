import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[3] / "seed_data.json"

def load_documents():
    if DATA.exists():
        return json.loads(DATA.read_text(encoding="utf-8"))
    return []

def retrieve(query, k=8):
    q = set(query.lower().split())
    docs = load_documents()
    scored = []
    for d in docs:
        text = (d.get("text","") + " " + d.get("title","")).lower()
        score = sum(1 for word in q if len(word) > 3 and word in text)
        scored.append((score, d))
    scored.sort(key=lambda x:x[0], reverse=True)
    return [d for score,d in scored[:k]]
