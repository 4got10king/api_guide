from pydantic import BaseModel
from datetime import datetime

class BuildingResponse(BaseModel):
    id: int
    address: str
    latitude: float
    longitude: float
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True