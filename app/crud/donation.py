from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import (
    Donation,
    User
)


class CRUDDonation(CRUDBase):

    async def get_multi_by_user_id(
        self,
        session: AsyncSession,
        user: User
    ):
        return (
            await session.execute(
                select(self.model).where(
                    self.model.user_id == user.id
                )
            )
        ).scalars().all()


donation_crud = CRUDDonation(Donation)
