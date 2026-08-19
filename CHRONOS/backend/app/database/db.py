import json, sqlite3
from pathlib import Path

DB_PATH = Path("/data/chronos.db") if Path("/data").exists() else Path("chronos.db")

def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    return c

def init_db():
    with conn() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS investigations(
          id TEXT PRIMARY KEY, question TEXT, status TEXT,
          created_at TEXT, updated_at TEXT, report TEXT
        );
        CREATE TABLE IF NOT EXISTS evidence(
          id TEXT PRIMARY KEY, investigation_id TEXT, claim TEXT,
          source TEXT, source_type TEXT, author TEXT,
          reliability REAL, relevance REAL, text TEXT
        );
        CREATE TABLE IF NOT EXISTS hypotheses(
          id TEXT PRIMARY KEY, investigation_id TEXT, name TEXT,
          support REAL, contradiction REAL, rationale TEXT
        );
        CREATE TABLE IF NOT EXISTS claims(
          id TEXT PRIMARY KEY, investigation_id TEXT,
          claim TEXT, confidence REAL, evidence_ids TEXT
        );
        CREATE TABLE IF NOT EXISTS events(
          id TEXT PRIMARY KEY, investigation_id TEXT,
          year INTEGER, title TEXT, description TEXT
        );
        """)
init_db()
