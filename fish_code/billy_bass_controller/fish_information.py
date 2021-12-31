from pydantic import BaseModel
from datetime import datetime


class FishInformation(BaseModel):
    device_id: str
    language_key: str = "en"
    last_updated: datetime = datetime.utcnow()
    state: str = "booting"
