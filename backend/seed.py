import asyncio
from faker import Faker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from database.db_metadata import Base
from database.models import BuildingORM, ActivityORM, OrganizationORM
from config.db import DBSettings

# Инициализация Faker
fake = Faker("ru_RU")


async def seed_database():
    # Получаем настройки базы данных
    db_settings = DBSettings()
    DATABASE_URL = db_settings.dsn_async

    # Создаем асинхронный движок и сессию
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        # Создаем здания
        buildings = []
        for _ in range(10):
            building = BuildingORM(
                address=fake.address(),
                latitude=float(fake.latitude()),
                longitude=float(fake.longitude()),
            )
            session.add(building)
            buildings.append(building)
        await session.commit()

        # Создаем дерево деятельностей
        activities = []
        for name in ["Еда", "Автомобили", "Одежда"]:
            parent = ActivityORM(name=name, level=1)
            session.add(parent)
            activities.append(parent)

            for sub_name in (
                ["Мясная продукция", "Молочная продукция"]
                if name == "Еда"
                else ["Грузовые", "Легковые"]
            ):
                child = ActivityORM(name=sub_name, level=2, parent_id=parent.id)
                session.add(child)
                activities.append(child)

                if sub_name == "Легковые":
                    for sub_sub_name in ["Запчасти", "Аксессуары"]:
                        sub_child = ActivityORM(
                            name=sub_sub_name, level=3, parent_id=child.id
                        )
                        session.add(sub_child)
                        activities.append(sub_child)
        await session.commit()

        # Создаем организации
        for _ in range(50):
            org = OrganizationORM(
                name=fake.company(),
                phone_numbers=[fake.phone_number() for _ in range(3)],
                building_id=fake.random_element(buildings).id,
            )
            session.add(org)

            # Добавляем случайные виды деятельности
            activity_ids = [
                a.id
                for a in fake.random_elements(activities, length=fake.random_int(1, 3))
            ]
            org.activities = [a for a in activities if a.id in activity_ids]
        await session.commit()


if __name__ == "__main__":
    asyncio.run(seed_database())
