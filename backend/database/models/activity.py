from sqlalchemy import Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from app.schemas.activity import ActivityResponse
from database.db_metadata import Base
from database.models.mixin import IsActiveMixin, TimestampMixin


class ActivityORM(Base, IsActiveMixin, TimestampMixin):
    """ORM модель для таблицы activities"""

    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("activities.id"), nullable=True
    )
    level: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    __table_args__ = (CheckConstraint("level <= 3", name="check_level"),)

    parent = relationship("ActivityORM", remote_side=[id], back_populates="children")
    children = relationship("ActivityORM", back_populates="parent")
    organizations = relationship(
        "OrganizationORM",
        secondary="organization_activities",
        back_populates="activities",
    )

    def get_schema(self) -> ActivityResponse:
        return ActivityResponse(
            id=self.id,
            name=self.name,
            parent_id=self.parent_id,
            level=self.level,
            children=(
                [child.get_schema() for child in self.children] if self.children else []
            ),
            created_at=self.created_at,
            updated_at=self.updated_at,
            is_active=self.is_active,
        )
