from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    sessionmaker
)

from app.core.config import settings


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(settings.database_url)

AsyncSessionDB = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    async with AsyncSessionDB() as async_session:
        yield async_session
