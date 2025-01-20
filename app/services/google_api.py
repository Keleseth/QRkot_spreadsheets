from copy import deepcopy
from datetime import datetime, timedelta

from aiogoogle import Aiogoogle

from app.core import constants
from app.core.config import settings
from app.core.error_messages import (
    COLUMNS_NUMBER_EXCEEDS_SHEET_CAPACITY,
    ROWS_NUMBER_EXCEEDS_SHEET_CAPACITY
)


def validate_sheet_capacity(
    rows_to_insert: int,
    columns_to_insert: int
) -> None:
    if rows_to_insert > constants.SHEET_MAX_ROWS:
        raise ValueError(
            ROWS_NUMBER_EXCEEDS_SHEET_CAPACITY.format(
                rows=rows_to_insert
            )
        )
    if columns_to_insert > constants.SHEET_MAX_COLUMNS:
        raise ValueError(
            COLUMNS_NUMBER_EXCEEDS_SHEET_CAPACITY.format(
                columns=columns_to_insert
            )
        )


async def spreadsheets_create(
    wrapper_services: Aiogoogle
) -> tuple[str, str]:
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = deepcopy(constants.PROJECT_SHEET)
    spreadsheet_body['properties']['title'] = (
        constants.PROJECT_SPREADSHEET_TITLE.format(
            date=datetime.now().strftime(constants.DATE_FORMAT)
        )
    )
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(
            json=spreadsheet_body
        )
    )
    return response['spreadsheetId'], response['spreadsheetUrl']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields='id',
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    projects: list[tuple],
    wrapper_service: Aiogoogle
) -> None:
    service = await wrapper_service.discover(
        'sheets',
        'v4'
    )
    sheet_head = deepcopy(constants.GOOGLE_SHEET_FORMAT)
    sheet_head[0][1] = datetime.now().strftime(constants.DATE_FORMAT)
    # Генератор преобразует float поле time_required в timedelta у объектов
    # projects в едином генераторе создания данных для таблицы
    sheet_values = [
        *sheet_head,
        *[list(map(
            str, [
                project[0],  # Наименование закрытого проекта
                timedelta(days=project[1]),  # Время потраченное на закрытие
                project[2]  # Описание проекта
            ]
        )) for project in projects]
    ]
    update_body = {
        'majorDimension': 'ROWS',
        'values': sheet_values
    }
    rows_to_insert = len(sheet_values)
    columns_to_insert = max(map(len, sheet_values))
    validate_sheet_capacity(
        rows_to_insert=rows_to_insert,
        columns_to_insert=columns_to_insert
    )
    await wrapper_service.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=constants.INSERT_DATA_RANGE.format(
                rows=rows_to_insert,
                columns=columns_to_insert
            ),
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
