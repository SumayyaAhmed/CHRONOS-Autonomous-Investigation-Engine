# CHRONOS — Complete Runnable Portfolio Package

CHRONOS is an agentic historical investigation platform prototype.

## Included
- FastAPI backend
- LangGraph cyclic investigation workflow
- Planner, research, timeline, political, economic, military, contradiction and synthesis agents
- Hybrid-style retrieval interface with local knowledge base
- SQLite by default for zero-setup local execution
- PostgreSQL + pgvector Docker profile for production-style deployment
- Evidence, claims, hypotheses and source metadata
- Human-in-the-loop review endpoint
- MCP-style research tool server
- React-style single-page dashboard (no build step required)
- Docker configuration
- Evaluation endpoint
- Seed historical dataset

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

## Example question

"Why did the Western Roman Empire decline?"

## Important

This is a complete runnable portfolio implementation. External web search, a production Neo4j deployment, and a production MCP transport can be connected through the provided interfaces, but the local package is deliberately self-contained so it runs without paid APIs.
