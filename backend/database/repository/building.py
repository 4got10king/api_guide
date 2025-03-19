from database.models.building import BuildingORM
from database.repository.repository import SQLAlchemyRepository


class BuildingRepository(SQLAlchemyRepository):
    model = BuildingORM