from app.rag.retriever import retrieve

def research(question, plan):
    docs = retrieve(question + " " + " ".join(x["task"] for x in plan))
    return [
        {
            "id": f"E{i+1}",
            "claim": d["claim"],
            "source": d["title"],
            "source_type": d.get("source_type","secondary"),
            "author": d.get("author","Unknown"),
            "reliability": d.get("reliability",0.7),
            "relevance": min(1.0, 0.45 + 0.08*i),
            "text": d["text"]
        } for i,d in enumerate(docs)
    ]
