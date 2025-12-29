from pydantic import BaseModel

class Log(BaseModel):
    message: str
    service: str
    level: str 
    duration_ms: int | None = none