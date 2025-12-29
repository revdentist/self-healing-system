# models/logs.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class LogEvent:
    service: str
    level: str
    message: str
    duration_ms: Optional[int]
    timestamp: datetime = datetime.utcnow()

    def is_error(self) -> bool:
        return self.level.upper() == "ERROR"

    def is_slow(self, threshold=500) -> bool:
        return self.duration_ms and self.duration_ms > threshold
