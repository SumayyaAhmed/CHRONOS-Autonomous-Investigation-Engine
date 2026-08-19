def synthesize(question, hypotheses, evidence, contradictions, timeline):
    hs=sorted(hypotheses,key=lambda x:x["support"],reverse=True)
    top=hs[0] if hs else None
    lines=[
      "# CHRONOS Investigation Report",
      f"## Question\n{question}",
      "## Executive Conclusion",
      f"The evidence currently gives the strongest support to **{top['name']}** ({top['support']:.0%}), "
      "but the investigation does not treat this as a single-cause explanation. "
      "Political, economic and military factors are evaluated as interacting explanations.",
      "## Competing Hypotheses"
    ]
    for h in hs:
        lines.append(f"- **{h['name']}** — support {h['support']:.0%}; contradiction {h['contradiction']:.0%}")
    lines += ["## Evidence"]
    for e in evidence:
        lines.append(f"- **{e['id']}** — {e['claim']} — {e['source']} (reliability {e['reliability']:.0%})")
    lines += ["## Timeline"]
    for e in timeline:
        lines.append(f"- **{e['year']}** — {e['title']}: {e['description']}")
    lines += ["## Contradictions"]
    for c in contradictions:
        lines.append(f"- {c['hypothesis']}: {', '.join(c['challenging_evidence']) or 'No direct challenge found'}")
    lines += [
      "## Unresolved Questions",
      "- Which causal factor preceded the others?",
      "- Which claims are independently supported by primary sources?",
      "- Are apparently contradictory accounts explained by chronology, source perspective, or genuine disagreement?"
    ]
    return "\n".join(lines)
