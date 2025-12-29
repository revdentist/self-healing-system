from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class Incident:
    type: str
    severity: str
    detected_at: datetime = datetime.utcnow()
    id: str = uuid.uuid4().hex
    status: str = "open"

    def close(self):
        self.status = "closed"

    def escalate(self):
        self.severity = "high"