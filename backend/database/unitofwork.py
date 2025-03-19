"""Module implementing Unit of Work pattern for managing repositories."""

from abc import ABC, abstractmethod
from typing import Type

from database.db import database_accessor

from database.repository.activity import ActivityRepository
from database.repository.organization import OrganizationRepository
from database.repository.building import BuildingRepository


class IUnitOfWork(ABC):
    """Interface for Unit of Work pattern."""

    activity: Type[ActivityRepository]
    organization: Type[OrganizationRepository]
    building: Type[BuildingRepository]

    @abstractmethod
    def __init__(self):
        """Initialize the Unit of Work instance."""

    @abstractmethod
    async def __aenter__(self):
        """Enter the context manager."""

    @abstractmethod
    async def __aexit__(self, *args):
        """Exit the context manager."""

    @abstractmethod
    async def commit(self):
        """Commit changes."""

    @abstractmethod
    async def rollback(self):
        """Rollback changes."""


class UnitOfWork:
    def __init__(self):
        self.session_fabric = database_accessor.get_async_session_maker()

    async def __aenter__(self):
        """Enter the context manager."""
        self.session = self.session_fabric()

        self.activity = ActivityRepository(self.session)
        self.organization = OrganizationRepository(self.session)
        self.building = BuildingRepository(self.session)

    async def __aexit__(self, exc_type, exc, tb):
        if exc_type is None:
            await self.commit()
        else:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
