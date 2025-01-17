from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud import donation_crud, charity_project_crud
from app.models import User
from app.schemas.dotanion import (
    CreateDonationScheme,
    DonationDBScheme,
    UserDonationDBScheme
)
from app.services.donation_distribution import distribute_donation


router = APIRouter()


@router.post(
    '/',
    response_model=UserDonationDBScheme,
)
async def donation_create(
    donation: CreateDonationScheme,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Создает объект доната. Требует аутентификацию.
    """
    new_donation = await donation_crud.create(
        donation,
        session,
        user,
    )
    session.add_all(
        # функция возвращает список объектов, измененных в процессе работы
        # функции. Эти объекты добавляются в сессию перед коммитом.
        distribute_donation(
            new_object=new_donation,
            available_targets=(
                await charity_project_crud.retrieve_uninvested_objects(
                    session=session
                )
            )
        )
    )
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get(
    '/my',
    response_model=list[UserDonationDBScheme],
)
async def get_my_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Получение всех донатов, пренадлежащих текущему пользователю.
    Требуется аутентификация.
    """
    return await donation_crud.get_multi_by_user_id(
        session=session,
        user=user
    )


@router.get(
    '/',
    response_model=list[DonationDBScheme],
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """Возвращает список всех донатов. Только для суперпользователя."""
    return await donation_crud.get_multi(session=session)
