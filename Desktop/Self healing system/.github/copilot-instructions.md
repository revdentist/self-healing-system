<!-- .github/copilot-instructions.md - guidance for AI coding agents in this repo -->
# Copilot instructions — Self Healing System (backend)

These instructions are concise, actionable notes for AI coding agents working in this repository. Focus on the backend service in `backend/`.

- **Project purpose**: a small FastAPI service that accepts log messages, classifies them, and flags incidents. Core files: `backend/main.py`, `backend/classifier.py`, `backend/incident_detector.py`.

- **Run (development)**: from repository root, create a venv and install runtime deps, then run Uvicorn:

  ```powershell
  python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install fastapi uvicorn pydantic
  uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
  ```

- **API surface** (examples):
  - `GET /` — health check, returns `{ "status": "ok" }` (see `backend/main.py`).
  - `POST /logs` — payload `{"message": "...", "type": "..."}`; response contains `category` (from `classify_log`) and `incident` (from `is_incident`).
  - `GET /logs` — returns in-memory `logs` list.

- **Important code patterns & conventions**:
  - `classify_log(message: str) -> str` (in `backend/classifier.py`) returns a short category string such as `"error"`, `"timeout"`, `"database_error"`, `"payment"`, `"authentication"`, or `"unknown error"` (note: the exact string `"unknown error"` is used in code; keep labels consistent when updating other modules).
  - `is_incident(entry: dict) -> bool` (in `backend/incident_detector.py`) inspects both `message` and `category`. It uses a small keyword list and specific category rules (database/authentication always incident; timeout+error is incident). When editing detection logic, update both the function and any tests or callers that rely on these boolean semantics.
  - `backend/main.py` keeps an in-memory `logs` list at module scope — there is no persistence. Any change that depends on durability should add storage and adapt `GET /logs` accordingly.

- **Data flow / integration points**:
  - Request -> `main.collect_log` -> `classify_log(message)` -> build `entry` -> `is_incident(entry)` -> append to `logs`.
  - There are no external integrations (databases, message buses) in the current codebase; adding them should also update README and run instructions.

- **Common gotchas discovered in code** (use these as guidance for edits):
  - `classifier.py` contains a misspelling check: it looks for `"db"` or `"datebase"` (typo). If you change wording, keep backward-compatible detection or add tests to avoid regressions.
  - Returned category labels are compared case-insensitively in `is_incident`, but `classify_log` returns lowercase labels — keep this convention.
  - `logs` is a plain Python list; concurrent requests will mutate it without locking. For a production change, consider thread-safe storage.

- **Where to change behavior**:
  - Add new log categories: update `classify_log` and adjust `is_incident` rules if needed.
  - Extend incident rules: modify `backend/incident_detector.py` and keep semantics simple (bool return).

- **Testing / validation hints (discoverable)**:
  - There are no tests in the repo. When adding tests, place them under `tests/` and validate the following flows: `POST /logs` classification, `is_incident` edge cases, and `GET /logs` ordering and content.

- **When making PRs**:
  - Reference the files changed (`backend/*.py`) and include a short sample `curl` or `uvicorn` command that demonstrates the change.

If anything here is unclear or you want me to include examples for a specific change (e.g., adding persistence, unit tests, or new categories), tell me which area to expand. 
