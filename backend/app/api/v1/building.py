from fastapi import APIRouter
from app.schemas.building import BuildingResponse
from app.service.building import BuildingService

router = APIRouter(prefix="/buildings", tags=["Здания"])

@router.get("", response_model=list[BuildingResponse])
async def get_all_buildings() -> list[BuildingResponse]:
    """Получение списка всех зданий"""
    return await BuildingService.get_all_buildings()

@router.get("/radius", response_model=list[BuildingResponse])
async def get_buildings_in_radius(lat: float, lon: float, radius: float) -> list[BuildingResponse]:
    """Получение зданий в радиусе от точки"""
    return await BuildingService.get_buildings_in_radius(lat, lon, radius)