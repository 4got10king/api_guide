from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from app.schemas.building import BuildingResponse
from database.db_metadata import Base
from database.models.mixin import IsActiveMixin, TimestampMixin

class BuildingORM(Base, IsActiveMixin, TimestampMixin):
    """ORM модель для таблицы buildings"""

    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String(512), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)

    organizations = relationship("OrganizationORM", back_populates="building")

    def get_schema(self) -> BuildingResponse:
        return BuildingResponse(
            id=self.id,
            address=self.address,
            latitude=self.latitude,
            longitude=self.longitude,
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_active=self.is_active,
        )