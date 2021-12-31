from pydantic import BaseModel
from datetime import datetime


class FishInformation(BaseModel):
    device_id: str = "DEFAULT_DEVICE_ID"
    language_key: str = "en"
    last_updated: datetime = datetime.utcnow()
    state: str = "booting"
