def generate_hypotheses(scores):
    mapping = {
      "Military": "Military pressure and frontier insecurity",
      "Political": "Political instability and administrative fragmentation",
      "Economic": "Economic deterioration and fiscal pressure"
    }
    out=[]
    for area,name in mapping.items():
        s=scores.get(area,0.5)
        out.append({
          "id": "H"+str(len(out)+1),
          "name": name,
          "support": round(s,2),
          "contradiction": round(max(0.05, 0.55-s/2),2),
          "rationale": f"Evidence-weighted score from the {area.lower()} investigation."
        })
    return out
