import sqlite3

def get_db():
    return sqlite3.connect("logs.db")

def create_incident_table():
    con = get_db()
    con.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        id TEXT PRIMARY KEY,
        type TEXT,
        severity TEXT,
        detected_at TEXT,
        status TEXT
    )
    """)
    con.commit()
    con.close()

def save_incident(inc):
    con = get_db()
    con.execute("INSERT INTO incidents VALUES (?, ?, ?, ?, ?)",
                (inc.id, inc.type, inc.severity, inc.detected_at.isoformat(), inc.status))
    con.commit()
    con.close()

def list_incidents(status=None):
    con = get_db()
    if status:
        rows = con.execute("SELECT * FROM incidents WHERE status=?", (status,)).fetchall()
    else:
        rows = con.execute("SELECT * FROM incidents").fetchall()

    con.close()
    return rows
