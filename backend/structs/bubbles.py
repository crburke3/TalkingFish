from pydantic import BaseModel


class Bubbles(BaseModel):
    queue_count: float = None
    speech_text: str = None
    commands: str = None
