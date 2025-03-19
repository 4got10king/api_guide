from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload
from database.models.activity import ActivityORM
from database.models.organization import OrganizationORM
from database.repository.repository import ModelType, ORMType, SQLAlchemyRepository
import asyncio


class ActivityRepository(SQLAlchemyRepository):
    model = ActivityORM

    async def get_organizations_by_tree(
        self, activity_id: int, result: list = None
    ) -> list:
        """Рекурсивно получает все организации по дереву деятельностей"""
        if result is None:
            result = []

        stmt = (
            select(ActivityORM)
            .options(
                selectinload(ActivityORM.organizations).selectinload(
                    OrganizationORM.building
                ),
                selectinload(ActivityORM.organizations)
                .selectinload(OrganizationORM.activities)
                .selectinload(ActivityORM.children),
                selectinload(ActivityORM.children),
            )
            .where(ActivityORM.id == activity_id)
        )
        activity = (await self.session.execute(stmt)).scalars().first()

        if activity:
            result.extend(activity.organizations)
            await asyncio.gather(
                *[
                    self.get_organizations_by_tree(child.id, result)
                    for child in activity.children
                ]
            )

        return result

    async def get_all(self) -> list[ModelType]:
        stmt = select(self.model).options(joinedload(self.model.children))
        res = await self.session.execute(stmt)
        res = [row[0].get_schema() for row in res.unique().all()]
        return res

    async def get_by_id(self, id: int) -> ORMType:
        stmt = (
            select(self.model)
            .options(joinedload(self.model.children))
            .where(self.model.id == id)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()
