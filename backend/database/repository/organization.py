from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database.models.activity import ActivityORM
from database.models.organization import OrganizationORM
from database.repository.repository import ORMType, SQLAlchemyRepository


class OrganizationRepository(SQLAlchemyRepository):
    model = OrganizationORM

    async def get_by_building(self, building_id: int) -> list[OrganizationORM]:
        """Получение организаций по ID здания"""
        stmt = (
            select(OrganizationORM)
            .options(
                joinedload(OrganizationORM.building),
                joinedload(OrganizationORM.activities).joinedload(ActivityORM.children),
            )
            .where(OrganizationORM.building_id == building_id)
        )

        result = await self.session.execute(stmt)
        return result.unique().scalars().all()

    async def get_by_id(self, id: int) -> ORMType:
        stmt = (
            select(self.model)
            .options(
                joinedload(OrganizationORM.building),
                joinedload(OrganizationORM.activities).joinedload(ActivityORM.children),
            )
            .where(self.model.id == id)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def get_by_name(self, name: str) -> list[OrganizationORM]:
        """Поиск организаций по названию (регистронезависимый)"""
        stmt = (
            select(OrganizationORM)
            .options(
                joinedload(OrganizationORM.building),
                joinedload(OrganizationORM.activities).joinedload(ActivityORM.children),
            )
            .where(
                OrganizationORM.name.ilike(f"%{name}%")
            )  # ILIKE для регистронезависимого поиска
        )
        result = await self.session.execute(stmt)
        return result.unique().scalars().all()
