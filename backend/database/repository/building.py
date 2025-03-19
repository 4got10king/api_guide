from sqlalchemy import select, func
from database.models.building import BuildingORM
from database.repository.repository import SQLAlchemyRepository


class BuildingRepository(SQLAlchemyRepository):
    model = BuildingORM

    async def get_in_radius(
        self, lat: float, lon: float, radius: float
    ) -> list[BuildingORM]:
        """Получение зданий в радиусе от заданной точки"""
        haversine = (
            6371
            * 2
            * func.asin(
                func.sqrt(
                    func.pow(
                        func.sin(
                            (func.radians(BuildingORM.latitude) - func.radians(lat)) / 2
                        ),
                        2,
                    )
                    + func.cos(func.radians(lat))
                    * func.cos(func.radians(BuildingORM.latitude))
                    * func.pow(
                        func.sin(
                            (func.radians(BuildingORM.longitude) - func.radians(lon))
                            / 2
                        ),
                        2,
                    )
                )
            )
        )

        stmt = select(BuildingORM).where(haversine <= radius)

        result = await self.session.execute(stmt)
        return result.scalars().all()
