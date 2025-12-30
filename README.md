# 🛠️ Self-Healing Incident Detection System

> Because staring at logs at 3 AM builds character, not systems.

---

## What this is

This is a **self-healing backend system (at the detection & response layer)** that continuously ingests logs, detects incidents, classifies failures, and alerts humans **before they start pretending nothing is broken**.

No dashboards.  
No vanity charts.  
Just signals, decisions, and consequences.

---

## What it actually does

- Ingests application logs
- Detects incidents (e.g. database failures)
- Classifies incidents by category
- Stores incident records
- Sends real-time alerts via Telegram
- Runs as a live backend service

---

## What it deliberately does NOT do

- Restart services automatically  
- Modify infrastructure without guardrails  
- Pretend to be “AI” where rules are enough  

This system knows **when** something is broken.  
Deciding **how far to automate fixes** is intentionally separate.

---

## Architecture (high level)

Logs → Detector → Classifier → Incident Engine → Alert Channel

Each layer does one job.  
None of them are clever alone.  
Together, they prevent silent failure.

---

## Core Components

- **Log Ingestion** – Accepts structured logs
- **Incident Detector** – Identifies anomalies and failures
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/20b8be2b-5198-4e79-856b-536ef966aa0d" />
- **Classifier** – Categorizes incidents (database, runtime, etc.)
- **Incident Engine** – Orchestrates detection logic
- **Telegram Alerter** – Sends alerts instantly
-  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/bec9a890-dd20-48bb-a7a6-d9390f3d6ba6" />
- **FastAPI App** – API layer and lifecycle management

---

## Live Deployment

The service is deployed and running.

**Base URL:**  
https://self-healing-system-1.onrender.com

**API Docs:**  
- `/docs`  
- `/openapi.json`

---

## Why “Self-Healing”?

Self-healing is not magic. It’s layers:

1. Detect failure  
2. Classify failure  
3. Notify decision-makers  
4. (Optionally) automate remediation  

This project **cleanly solves steps 1–3**.  
Automatic fixes can be added safely on top.

---

## Tech Stack

- Python 3
- FastAPI
- SQLite
- Uvicorn
- Requests
- Render (deployment)

Minimal by design. Boring on purpose.

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload

TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id
