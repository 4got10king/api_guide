from fastapi import HTTPException
from app.schemas.building import BuildingResponse
from database.unitofwork import IUnitOfWork, UnitOfWork

class BuildingService:
    @classmethod
    async def get_all_buildings(
        cls, uow: IUnitOfWork = UnitOfWork()
    ) -> list[BuildingResponse]:
        async with uow:
            buildings = await uow.buildings.get_all()
            return [BuildingResponse.model_validate(building) for building in buildings]

    @classmethod
    async def get_buildings_in_radius(
        cls, lat: float, lon: float, radius: float, uow: IUnitOfWork = UnitOfWork()
    ) -> list[BuildingResponse]:
        async with uow:
            buildings = await uow.buildings.get_in_radius(lat, lon, radius)
            return [BuildingResponse.model_validate(building) for building in buildings]