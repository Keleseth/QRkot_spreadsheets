from typing import TypeVar, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from app.models import User


T = TypeVar('T', bound=DeclarativeMeta)


class CRUDBase:
    """
    Базовый CRUD класс. Содержит общие crud операции для моделей:
    CharityProject и Donation.
    """

    def __init__(self, model):
        self.model = model

    async def create(
        self,
        obj_in,
        session: AsyncSession,
        user: Optional[User] = None
    ) -> T:
        obj_in_data = obj_in.dict()
        if user:
            obj_in_data['user_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        return db_obj

    async def get_multi(
        self,
        session: AsyncSession,
    ) -> list[T]:
        return (
            await session.execute(
                select(self.model)
            )
        ).scalars().all()

    async def retrieve_uninvested_objects(
        self,
        session: AsyncSession
    ) -> list[T]:
        return (
            await session.execute(
                select(self.model).where(
                    self.model.fully_invested.is_(False)
                ).order_by(self.model.create_date)
            )
        ).scalars().all()

    async def get_object_by_id(
        self,
        object_id: int,
        session: AsyncSession
    ) -> Optional[T]:
        return (
            await session.execute(
                select(self.model).where(
                    self.model.id == object_id
                )
            )
        ).scalars().first()

    async def remove(
        self,
        db_obj,
        session: AsyncSession
    ) -> T:
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def update(
        self,
        db_obj,
        obj_in,
        session: AsyncSession
    ) -> T:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj
