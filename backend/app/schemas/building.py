from pydantic import BaseModel, ConfigDict
from datetime import datetime


class BuildingResponse(BaseModel):
    id: int
    address: str
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
