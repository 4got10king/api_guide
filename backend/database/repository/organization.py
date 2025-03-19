from database.models.organization import OrganizationORM
from database.repository.repository import SQLAlchemyRepository


class OrganizationRepository(SQLAlchemyRepository):
    model = OrganizationORM