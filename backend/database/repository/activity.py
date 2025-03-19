from database.models.activity import ActivityORM
from database.repository.repository import SQLAlchemyRepository


class ActivityRepository(SQLAlchemyRepository):
    model = ActivityORM