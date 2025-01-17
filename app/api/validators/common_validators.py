from typing import Any, Type, Optional

from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from app.core import error_messages
from app.core.exceptions import UniqueFieldOccupiedExcedption


async def check_unique_field_occupied(
    unique_field: str,
    unique_field_data: Any,
    model: Type[DeclarativeMeta],
    session: AsyncSession,
    updated_obj_id: Optional[int] = None,
) -> None:
    if not hasattr(model, unique_field):
        raise ValueError(
            error_messages.NO_SUCH_FIELD_IN_MODEL.format(
                model=model.__name__,
                field=unique_field
            )
        )
    field = getattr(model, unique_field)
    where_conditions = [field == unique_field_data]
    if updated_obj_id is not None:
        where_conditions.append(model.id != updated_obj_id)
    obj_exists = await session.execute(
        select(exists().where(*where_conditions))
    )
    if obj_exists.scalar():
        raise UniqueFieldOccupiedExcedption(
            model_name=model.__name__,
            field=unique_field,
            field_data=unique_field_data
        )
