from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate
from app.api.validators.common_validators import check_unique_field_occupied
from app.core import error_messages


class ProjectValidator:
    """
    Класс валидации для модели CharityProject. Содержит методы, необходимые
    для проверки соответствия бизнес логики проекта при выполнении
    небезопасных HTTP методов запроса.
    """

    model = CharityProject

    @staticmethod
    def validate_project_exists(
        project: CharityProject,
    ) -> None:
        """Проверка существования проекта в бд."""
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=error_messages.OBJECT_NOT_FOUND.format(
                    table_name=CharityProject.__tablename__
                )
            )

    @staticmethod
    def validate_deletion(
        project: CharityProject
    ) -> None:
        """Проверка состояния инвестирования проекта перед удаленеим."""
        ProjectValidator.validate_project_exists(
            project
        )
        if project.invested_amount > 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_messages.ALREADY_INVESTED
            )

    @staticmethod
    async def validate_update(
        obj_in: CharityProjectUpdate,
        project: CharityProject,
        session: AsyncSession
    ) -> None:
        ProjectValidator.validate_fully_invested(
            project,
            should_be_fully_invested=False
        )
        update_data = obj_in.dict(exclude_unset=True)
        if update_data.get('name'):
            await check_unique_field_occupied(
                'name',
                update_data['name'],
                CharityProject,
                session,
                updated_obj_id=project.id
            )
        full_amount_data = update_data.get('full_amount')
        if full_amount_data is not None:
            ProjectValidator.validate_between_update_full_amount(
                project,
                full_amount_data
            )

    @staticmethod
    def validate_between_update_full_amount(
        project: CharityProject,
        full_amount_data: int
    ) -> None:
        if project.invested_amount > full_amount_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_messages.INVESTMENT_EXCEEDS_FULL_AMOUNT
            )
        project.fully_invested = project.invested_amount == full_amount_data
        if project.fully_invested:
            project.close_date = datetime.now(timezone.utc)

    @staticmethod
    def validate_fully_invested(
        project: CharityProject,
        should_be_fully_invested: bool
    ) -> None:
        """
        Универсальный валидатор, проверяющий,
        полностью ли проинвестирован проект.
        Работает так:
        1. Передавайте в функцию в параметр should_be_fully_invested - False,
        если хотите убедиться, что проект еще не полностью проинвестирован.
        2. Передавайте в should_be_fully_invested - True, чтобы убедиться,
        что проект уже полностью проинвестирован.
        """
        if not should_be_fully_invested and project.fully_invested:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_messages.FULLY_INVESTED_PROJECT
            )
        if should_be_fully_invested and not project.fully_invested:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_messages.NOT_FULLY_INVESTED_PROJECT
            )


project_validator = ProjectValidator()
