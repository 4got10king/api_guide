from fastapi import HTTPException
from app.schemas.activity import ActivityResponse
from app.schemas.organiztaion import OrganizationResponse
from database.unitofwork import IUnitOfWork, UnitOfWork


class ActivityService:
    @classmethod
    async def get_all_activities(
        cls, uow: IUnitOfWork = UnitOfWork()
    ) -> list[ActivityResponse]:
        async with uow:
            activities = await uow.activity.get_all()
            return [
                ActivityResponse.model_validate(activity) for activity in activities
            ]

    @classmethod
    async def get_activity_tree(
        cls, activity_id: int, uow: IUnitOfWork = UnitOfWork()
    ) -> ActivityResponse:
        async with uow:
            activity = await uow.activity.get_by_id(activity_id)
            if not activity:
                raise HTTPException(status_code=404, detail="Activity not found")
            return ActivityResponse.model_validate(activity)

    @classmethod
    async def search_organizations_by_activity_tree(
        cls, activity_id: int, uow: IUnitOfWork = UnitOfWork()
    ) -> list[OrganizationResponse]:
        async with uow:
            orgs = await uow.activity.get_organizations_by_tree(activity_id)
            return [OrganizationResponse.model_validate(org) for org in orgs]
