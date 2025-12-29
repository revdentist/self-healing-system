from fastapi import FastAPI
from datetime import datetime
import uuid
from dotenv import load_dotenv

from models.logs_input import Log
from database import get_db, init_db
from classifier import classify_log
from incident_detector import is_incident
from alerter_telegram import send_telegram_alert

load_dotenv()

app = FastAPI(title="Self Healing Infra - V1")

# initialize database
init_db()


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/logs")
def collect_log(log: Log):
    log.id = str(uuid.uuid4())
    log.category = classify_log(log.message)
    log.incident = is_incident(log.__dict__)

    # send alert only if incident
    if log.incident:
        send_telegram_alert(
            f"🚨 INCIDENT DETECTED\n\n"
            f"Message: {log.message}\n"
            f"Category: {log.category}\n"
            f"Type: {log.type}"
        )

    # store in database
    with get_db() as conn:
        conn.execute(
            """
            INSERT INTO logs (id, message, category, type, incident, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                log.id,
                log.message,
                log.category,
                log.type,
                int(log.incident),
                log.received_at,
            ),
        )

    return {
        "stored": True,
        "incident": log.incident,
        "log_id": log.id,
    }


@app.get("/logs")
def get_logs():
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM logs").fetchall()

    return [
        {
            "id": r[0],
            "message": r[1],
            "category": r[2],
            "type": r[3],
            "incident": bool(r[4]),
            "timestamp": r[5],
        }
        for r in rows
    ]
