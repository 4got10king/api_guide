from fastapi import APIRouter
from app.schemas.activity import ActivityResponse
from app.schemas.organiztaion import OrganizationResponse
from app.service.activity import ActivityService

router = APIRouter(prefix="/activities", tags=["Деятельности"])


@router.get("", response_model=list[ActivityResponse])
async def get_all_activities() -> list[ActivityResponse]:
    """Получение списка всех деятельностей"""
    return await ActivityService.get_all_activities()


@router.get("/{activity_id}", response_model=ActivityResponse)
async def get_activity(activity_id: int) -> ActivityResponse:
    """Получение деятельности по ID"""
    return await ActivityService.get_activity_tree(activity_id)


@router.get("/{activity_id}/organizations", response_model=list[OrganizationResponse])
async def get_organizations_by_activity(activity_id: int) -> list[OrganizationResponse]:
    """Получение организаций по виду деятельности"""
    return await ActivityService.search_organizations_by_activity_tree(activity_id)
