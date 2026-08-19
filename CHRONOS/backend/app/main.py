import uuid, datetime, re
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from app.graph.workflow import workflow
from app.database.db import conn

app=FastAPI(title="CHRONOS API",version="1.0.0")

class InvestigationRequest(BaseModel):
    question:str

class ReviewRequest(BaseModel):
    approved:bool
    instruction:str=""

@app.get("/",response_class=HTMLResponse)
def home():
    return open("app/static.html",encoding="utf-8").read()

@app.get("/health")
def health(): return {"status":"ok","service":"CHRONOS"}

@app.post("/api/investigations")
def investigate(req:InvestigationRequest):
    if len(req.question.strip())<8: raise HTTPException(400,"Question is too short")
    iid=str(uuid.uuid4())
    now=datetime.datetime.utcnow().isoformat()
    result=workflow.invoke({"question":req.question})
    with conn() as c:
        c.execute("INSERT INTO investigations VALUES(?,?,?,?,?,?)",(iid,req.question,"completed",now,now,result["report"]))
        for e in result["evidence"]:
            c.execute("INSERT INTO evidence VALUES(?,?,?,?,?,?,?,?,?)",
              (e["id"],iid,e["claim"],e["source"],e["source_type"],e["author"],e["reliability"],e["relevance"],e["text"]))
        for h in result["hypotheses"]:
            c.execute("INSERT INTO hypotheses VALUES(?,?,?,?,?,?)",
              (h["id"],iid,h["name"],h["support"],h["contradiction"],h["rationale"]))
        for ev in result["timeline"]:
            c.execute("INSERT INTO events VALUES(?,?,?,?,?)",(f'{iid}-{ev["year"]}',iid,ev["year"],ev["title"],ev["description"]))
    return {"id":iid,"created_at":now,**result}

@app.get("/api/investigations")
def list_investigations():
    with conn() as c:
        rows=c.execute("SELECT id,question,status,created_at FROM investigations ORDER BY created_at DESC").fetchall()
    return [dict(r) for r in rows]

@app.get("/api/investigations/{iid}")
def get_investigation(iid:str):
    with conn() as c:
        inv=c.execute("SELECT * FROM investigations WHERE id=?",(iid,)).fetchone()
        if not inv: raise HTTPException(404,"Investigation not found")
        evidence=[dict(x) for x in c.execute("SELECT * FROM evidence WHERE investigation_id=?",(iid,))]
        hypotheses=[dict(x) for x in c.execute("SELECT * FROM hypotheses WHERE investigation_id=?",(iid,))]
        events=[dict(x) for x in c.execute("SELECT * FROM events WHERE investigation_id=? ORDER BY year",(iid,))]
    return {"investigation":dict(inv),"evidence":evidence,"hypotheses":hypotheses,"timeline":events}

@app.post("/api/investigations/{iid}/review")
def review(iid:str,req:ReviewRequest):
    with conn() as c:
        row=c.execute("SELECT * FROM investigations WHERE id=?",(iid,)).fetchone()
        if not row: raise HTTPException(404,"Investigation not found")
        status="approved" if req.approved else "needs_more_research"
        c.execute("UPDATE investigations SET status=?,updated_at=? WHERE id=?",
                  (status,datetime.datetime.utcnow().isoformat(),iid))
    return {"id":iid,"status":status,"instruction":req.instruction}

@app.get("/api/evaluate")
def evaluate():
    with conn() as c:
        n=c.execute("SELECT COUNT(*) n FROM investigations").fetchone()["n"]
        e=c.execute("SELECT COUNT(*) n FROM evidence").fetchone()["n"]
        h=c.execute("SELECT COUNT(*) n FROM hypotheses").fetchone()["n"]
    return {"investigations":n,"evidence_items":e,"hypotheses":h,"evaluation_note":"Use labeled questions to measure retrieval, grounding and contradiction precision."}

@app.get("/api/mcp/tools")
def mcp_tools():
    return {"tools":["search_sources","retrieve_document","search_events","query_timeline","find_related_entities","search_evidence","get_source_metadata","store_evidence","query_knowledge_graph"]}
