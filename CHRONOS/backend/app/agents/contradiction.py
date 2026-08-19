def find_contradictions(hypotheses, evidence):
    results=[]
    for h in hypotheses:
        challenging = [
            e["id"] for e in evidence
            if h["name"].split()[0].lower() not in e["text"].lower()
        ][:3]
        results.append({
          "hypothesis":h["name"],
          "support":h["support"],
          "contradiction":h["contradiction"],
          "challenging_evidence":challenging,
          "status":"requires comparison"
        })
    return results
