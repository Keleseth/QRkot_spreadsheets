from datetime import datetime

from typing import Optional

from aiogoogle import Aiogoogle

from app.core import constants
from app.core.config import settings
from app.core.error_messages import PROJECTS_NUMBER_EXCEEDS_TABLE_CAPACITY


async def spreadsheets_create(
    wrapper_services: Aiogoogle
) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(
            json=constants.PROJECT_TABLE
        )
    )
    print(type(response))
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': constants.PERMISSION_TYPE,
        'role': constants.PERMISSION_ROLE,
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id",
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    projects: Optional[list],
    wrapper_service: Aiogoogle
) -> None:
    now = datetime.now().strftime(constants.DATE_FORMAT)
    service = await wrapper_service.discover(
        'sheets',
        'v4'
    )
    table_values = constants.GOOGLE_TABLE_FORMAT
    table_values[0][1] = now
    if projects:
        for project in projects:
            table_values.append(list(map(str, project)))
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_service.as_service_account(
        service.spreadsheets.values.clear(
            spreadsheetId=spreadsheet_id,
            range=constants.CLEAN_RANGE
        )
    )
    if len(table_values) > constants.ROWS_RANGE:
        raise ValueError(PROJECTS_NUMBER_EXCEEDS_TABLE_CAPACITY)
    await wrapper_service.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='A1:E30',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
