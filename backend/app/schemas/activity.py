from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ActivityResponse(BaseModel):
    id: int
    name: str
    parent_id: Optional[int]
    level: int
    children: List['ActivityResponse'] = []
    created_at: datetime
    updated_at: datetime
    is_active: bool

    class Config:
        from_attributes = True

ActivityResponse.update_forward_refs()