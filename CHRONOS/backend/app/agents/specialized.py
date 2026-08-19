def analyze_specialists(evidence):
    text = " ".join(e["text"].lower() for e in evidence)
    def score(words):
        hits = sum(text.count(w) for w in words)
        return min(0.95, 0.35 + hits * 0.06)
    return {
      "Political": score(["polit","civil","succession","administr"]),
      "Economic": score(["economic","tax","trade","currency","agricultur"]),
      "Military": score(["military","army","border","war","gothic"]),
    }
