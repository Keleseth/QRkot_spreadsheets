from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud, donation_crud
from app.models import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate
)
from app.services.donation_distribution import distribute_donation
from app.api.validators.charity_project import (
    check_unique_field_occupied,
    project_validator
)


router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def create_charity_project(
    charity_project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session)
):
    """Создание проекта для пожертвований суперпользователем."""
    await check_unique_field_occupied(
        'name',
        charity_project.name,
        CharityProject,
        session
    )
    new_charity_project: CharityProject = await charity_project_crud.create(
        charity_project,
        session
    )
    session.add_all(
        # функция возвращает список объектов, измененных в процессе работы
        # функции. Эти объекты добавляются в сессию перед коммитом.
        distribute_donation(
            new_object=new_charity_project,
            available_targets=await donation_crud.retrieve_uninvested_objects(
                session=session
            ),
        )
    )
    await session.commit()
    await session.refresh(new_charity_project)
    return new_charity_project


@router.get(
    '/',
    response_model=list[CharityProjectDB],
)
async def get_charity_projects(
    session: AsyncSession = Depends(get_async_session)
):
    """Получение всех проектов. Доступно для любого пользователя."""
    return await charity_project_crud.get_multi(session)


@router.delete(
    '/{project_id}',
    dependencies=[Depends(current_superuser)]
)
async def remove_charity_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Удаление проекта суперпользователем. Доступно только по отношению к
    проекту, в который еще никто не инвестировал.
    """
    project = await charity_project_crud.get_object_by_id(
        project_id,
        session
    )
    project_validator.validate_deletion(project)
    project = await charity_project_crud.remove(
        project,
        session
    )
    return project


@router.patch(
    '/{project_id}',
    dependencies=[Depends(current_superuser)],
    response_model=CharityProjectDB,
)
async def update_charity_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Изменение проекта суперпользователем.
    Доступные поля для изменения: name, description, full_amount
    Для поля name ограничение на уникальность не включая название
    изменяемого проекта. Для full_amount, нельзя изменять поле на величину,
    меньшую чем поле invested_amount(уже проинвестировано). Если же эти две
    величины совпадут, изменения вступают в силу и проект становится закрытым,
    т.к. full_amount становится равным invested_amount.
    """
    project = await charity_project_crud.get_object_by_id(
        project_id,
        session
    )
    project_validator.validate_project_exists(project)
    await project_validator.validate_update(
        obj_in,
        project,
        session
    )
    project = await charity_project_crud.update(
        project,
        obj_in,
        session
    )
    return project
