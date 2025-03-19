from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import List, Optional
from datetime import datetime
from .building import BuildingResponse
from .activity import ActivityResponse


class OrganizationResponse(BaseModel):
    id: int
    name: str
    phone_numbers: List[str]
    building_id: int
    building: Optional[BuildingResponse]
    activities: List[ActivityResponse]
    created_at: datetime
    updated_at: datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class OrganizationCreate(BaseModel):
    name: str = Field(
        ..., min_length=1, max_length=255, description="Название организации"
    )
    phone_numbers: List[str] = Field(..., description="Список телефонных номеров")
    building_id: int = Field(..., description="ID здания")
    activity_ids: List[int] = Field(..., description="Список ID видов деятельности")

    @field_validator("phone_numbers")
    def validate_phone_numbers(cls, v):
        if not v:
            raise ValueError("Должен быть указан хотя бы один номер телефона")
        return v

    @field_validator("activity_ids")
    def validate_activity_ids(cls, v):
        if not v:
            raise ValueError("Должен быть указан хотя бы один вид деятельности")
        return v


class OrganizationSearchRequest(BaseModel):
    name: str
