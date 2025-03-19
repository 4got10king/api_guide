from sqlalchemy import JSON, Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.schemas.organiztaion import OrganizationResponse
from database.db_metadata import Base
from database.models.mixin import IsActiveMixin, TimestampMixin

organization_activities = Table(
    "organization_activities",
    Base.metadata,
    Column(
        "organization_id", Integer, ForeignKey("organizations.id"), primary_key=True
    ),
    Column("activity_id", Integer, ForeignKey("activities.id"), primary_key=True),
)


class OrganizationORM(Base, IsActiveMixin, TimestampMixin):
    """ORM модель для таблицы organizations"""

    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    phone_numbers: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    building_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("buildings.id"), nullable=False
    )

    building = relationship("BuildingORM", back_populates="organizations")
    activities = relationship(
        "ActivityORM", secondary=organization_activities, back_populates="organizations"
    )

    def get_schema(self) -> OrganizationResponse:
        return OrganizationResponse(
            id=self.id,
            name=self.name,
            phone_numbers=self.phone_numbers,
            building_id=self.building_id,
            building=self.building.get_schema() if self.building else None,
            activities=[activity.get_schema() for activity in self.activities],
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_active=self.is_active,
        )
