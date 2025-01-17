from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
        self,
        charity_project_name: str,
        session: AsyncSession
    ) -> Optional[int]:
        return (
            await session.execute(
                select(CharityProject.id).where(
                    CharityProject.name == charity_project_name
                )
            )
        ).scalars().first()

    async def get_projects_by_completion_rate(
        self,
        session: AsyncSession
    ) -> list[tuple]:
        time_required = (
            func.julianday(CharityProject.close_date) -
            func.julianday(CharityProject.create_date)
        ).label('time_required')
        projects = await session.execute(
            select(
                CharityProject.name,
                time_required,
                CharityProject.description
            ).where(
                CharityProject.fully_invested.is_(True)
            ).order_by(
                time_required
            )
        )
        return projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)
