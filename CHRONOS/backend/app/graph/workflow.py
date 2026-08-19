from typing import TypedDict, Any
from langgraph.graph import StateGraph, START, END
from app.agents.planner import plan_question
from app.agents.researcher import research
from app.agents.timeline import build_timeline
from app.agents.specialized import analyze_specialists
from app.agents.hypotheses import generate_hypotheses
from app.agents.contradiction import find_contradictions
from app.agents.synthesis import synthesize

class State(TypedDict, total=False):
    question:str; plan:list; evidence:list; timeline:list
    specialist_scores:dict; hypotheses:list; contradictions:list; report:str

def planner(s): return {"plan":plan_question(s["question"])}
def researcher(s): return {"evidence":research(s["question"],s["plan"])}
def specialists(s): return {"specialist_scores":analyze_specialists(s["evidence"])}
def hyp(s): return {"hypotheses":generate_hypotheses(s["specialist_scores"])}
def contra(s): return {"contradictions":find_contradictions(s["hypotheses"],s["evidence"])}
def timeline(s): return {"timeline":build_timeline(s["evidence"])}
def final(s): return {"report":synthesize(s["question"],s["hypotheses"],s["evidence"],s["contradictions"],s["timeline"])}

g=StateGraph(State)
g.add_node("planner",planner); g.add_node("researcher",researcher)
g.add_node("specialists",specialists); g.add_node("hypotheses",hyp)
g.add_node("contradiction",contra); g.add_node("timeline",timeline); g.add_node("synthesis",final)
g.add_edge(START,"planner"); g.add_edge("planner","researcher")
g.add_edge("researcher","specialists"); g.add_edge("specialists","hypotheses")
g.add_edge("hypotheses","contradiction"); g.add_edge("contradiction","timeline")
g.add_edge("timeline","synthesis"); g.add_edge("synthesis",END)
workflow=g.compile()
