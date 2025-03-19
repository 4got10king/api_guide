from fastapi import HTTPException
from app.schemas.organiztaion import OrganizationCreate, OrganizationResponse
from database.unitofwork import IUnitOfWork, UnitOfWork

class OrganizationService:
    @classmethod
    async def get_organization_by_id(
        cls, org_id: int, uow: IUnitOfWork = UnitOfWork()
    ) -> OrganizationResponse:
        async with uow:
            org = await uow.organization.get_by_id(org_id)
            if not org:
                raise HTTPException(status_code=404, detail="Organization not found")
            return OrganizationResponse.model_validate(org)

    @classmethod
    async def get_organizations_by_building(
        cls, building_id: int, uow: IUnitOfWork = UnitOfWork()
    ) -> list[OrganizationResponse]:
        async with uow:
            orgs = await uow.organization.get_by_building(building_id)
            return [OrganizationResponse.model_validate(org) for org in orgs]

    @classmethod
    async def create_organization(
        cls, org_data: OrganizationCreate, uow: IUnitOfWork = UnitOfWork()
    ) -> OrganizationResponse:
        async with uow:
            org = await uow.organization.add_one(org_data.model_dump())
            await uow.commit()
            return OrganizationResponse.model_validate(org)
