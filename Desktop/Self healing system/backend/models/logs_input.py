from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Log(BaseModel):
    id: Optional[str] = None
    message: str
    type: str
    category: Optional[str] = None
    incident: Optional[bool] = None
    received_at: datetime = Field(default_factory=datetime.utcnow)
