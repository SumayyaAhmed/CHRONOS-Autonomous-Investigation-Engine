# CHRONOS — Autonomous AI Platform for Evidence-Based Investigation

CHRONOS is an agentic AI investigation platform designed to investigate complex questions across history, news and current events, academic topics, market intelligence, and general information. Instead of simply generating an answer, CHRONOS treats each question as a structured investigation: it plans investigative tasks, gathers evidence, compares competing explanations, identifies contradictory information, and produces an evidence-grounded report with confidence and uncertainty tracking.

**Investigate. Verify. Compare. Understand.**

## Included

* FastAPI backend
* LangGraph cyclic investigation workflow
* Planner, investigation, timeline, political, economic, military, contradiction and synthesis agents
* Hybrid-style retrieval interface with local knowledge base
* SQLite by default for zero-setup local execution
* PostgreSQL + pgvector Docker profile for production-style deployment
* Evidence, claims, hypotheses and source metadata
* Human-in-the-loop review endpoint
* MCP-style investigation tool server
* React-style single-page dashboard (no build step required)
* Docker configuration
* Evaluation endpoint
* Seed evidence dataset

## Quickest Run

Python 3.11+:

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

http://localhost:8000

API docs:

http://localhost:8000/docs

## Docker

```bash
docker compose up --build
```

Open:

http://localhost:8000

## Optional OpenAI

Copy `.env.example` to `.env` and add:

```text
OPENAI_API_KEY=your_key
MODEL_NAME=gpt-4o-mini
```

The application still runs without a key using deterministic local synthesis.

## Example questions

"Why did the Western Roman Empire decline?"

"What factors contributed to a recent geopolitical crisis?"

"What evidence supports or challenges this reported claim?"

"What are the competing explanations for a major economic trend?"

## Important

This is a complete runnable portfolio implementation. External web search, a production Neo4j deployment, and a production MCP transport can be connected through the provided interfaces, but the local package is deliberately self-contained so it runs without paid APIs.
