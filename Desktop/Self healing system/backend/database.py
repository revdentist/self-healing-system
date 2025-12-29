import sqlite3
from contextlib import contextmanager

DB_NAME = "logs.db"

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id TEXT PRIMARY KEY,
            message TEXT,
            category TEXT,
            type TEXT,
            incident INTEGER,
            timestamp TEXT
        );
        """)
