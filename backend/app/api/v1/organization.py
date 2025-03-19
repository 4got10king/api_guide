from fastapi import APIRouter
from app.schemas.organiztaion import (
    OrganizationCreate,
    OrganizationResponse,
    OrganizationSearchRequest,
)
from app.service.organization import OrganizationService

router = APIRouter(prefix="/organizations", tags=["Организации"])


@router.get("/{org_id}", response_model=OrganizationResponse)
async def get_organization(org_id: int) -> OrganizationResponse:
    """Получение организации по ID"""
    return await OrganizationService.get_organization_by_id(org_id)


@router.post("", response_model=OrganizationResponse, status_code=201)
async def create_organization(org_data: OrganizationCreate) -> OrganizationResponse:
    """Создание новой организации"""
    return await OrganizationService.create_organization(org_data)


@router.get("/building/{building_id}", response_model=list[OrganizationResponse])
async def get_organizations_by_building(building_id: int) -> list[OrganizationResponse]:
    """Получение списка организаций в здании"""
    return await OrganizationService.get_organizations_by_building(building_id)


@router.post("/search", response_model=list[OrganizationResponse])
async def search_organizations_by_name(
    search_request: OrganizationSearchRequest,
) -> list[OrganizationResponse]:
    """Поиск организаций по названию"""
    return await OrganizationService.get_organizations_by_name(search_request.name)
