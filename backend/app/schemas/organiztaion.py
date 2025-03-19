from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .building import BuildingResponse
from .activity import ActivityResponse

class OrganizationResponse(BaseModel):
    id: int
    name: str
    phone_numbers: str
    building_id: int
    building: Optional[BuildingResponse]
    activities: List[ActivityResponse]
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True