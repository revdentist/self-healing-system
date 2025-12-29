from datetime import datetime, timedelta
from typing import List

from backend.models.logs import LogEvent
cfrom backend.models.incident import Incident

class IncidentEngine:
    def __init__(self, window_minutes: int = 5):
        self.window = timedelta(minutes=window_minutes)
        self.events: List[LogEvent] = []

    def add_log(self, log: LogEvent) -> List[Incident]:
        now = datetime.utcnow()
        self.events = [e for e in self.events if now - e.timestamp <= self.window]
        self.events.append(log)

        incidents = []

        error_events = [e for e in self.events if e.is_error()]
        if len(error_events) >= 5:
            incidents.append(Incident(type="error_spike", severity="high", detected_at=now))

        slow_events = [e for e in self.events if e.is_slow()]
        if len(slow_events) >= 3:
            incidents.append(Incident(type="slow_response", severity="medium", detected_at=now))

        return incidents
