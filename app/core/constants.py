from typing import Any

# Параметры db
MAX_PROJECT_NAME_LENGTH = 100
MIN_PROJECT_NAME_LENGTH = 1
MIN_PROJECT_DESCRIPTION_LENGTH = 1
DEFAULT_INVESTED_AMOUNT = 0
GT_FULL_AMOUNT = 0

# Пути до апи проектов и донатов
CHARITY_PROJECT_API_PATH = '/charity_project'
DONATION_API_PATH = '/donation'

# Пути до совместного с Google апи
GOOGLE_ROUTE = '/google'

# Пути до апи юзеров
AUTH_JWT = '/auth/jwt'
AUTH = '/auth'
USERS = '/users'


# Теги роутеров для swagger
AUTH_TAG = 'auth'
USERS_TAG = 'users'
GOOGLE_TAG = 'Google'

# Теги роутеров проектов и донатов
CHARITY_PROJECT_TAGS = 'charity project'
DONATION_TAGS = 'donation'

# форматы
DATE_FORMAT = '%Y/%m/%d %H:%M:%S'


# Google sheets settings
SHEET_MAX_ROWS = 100
SHEET_MAX_COLUMNS = 10
LOCALE = 'ru_RU'
SHEET_TYPE = 'GRID'
SHEET_TITLE = 'Закрытые проекты'

# Строка для вставки данных в таблицу от начала таблицы и по размеру данных
INSERT_DATA_RANGE = 'R1C1:R{rows}C{colomns}'

# Способ наполнения данными гугл таблицы
SHEET_MAJOR_DIMENSION = 'ROWS'

# Установка уровня допуска к документу для пользователей
PERMISSION_TYPE = 'user'
PERMISSION_ROLE = 'writer'

PROJECT_SHEET_TITLE = 'Отчет на {date}'

# Шаблон таблицы для закрытых проектов сортированных по скорости закрытия
GOOGLE_SHEET_FORMAT = [
    ['Отчет от', 'insert_date'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]

# Дефолтная таблица для выгрузки закрытых проектов
PROJECT_SHEET: dict[str, Any] = {
    'properties': {
        'title': '',
        'locale': LOCALE
    },
    'sheets': [
        {
            'properties': {
                'sheetType': SHEET_TYPE,
                'sheetId': 0,
                'title': SHEET_TITLE,
                'gridProperties': {
                    'rowCount': SHEET_MAX_ROWS,
                    'columnCount': SHEET_MAX_COLUMNS
                }
            }
        }
    ]
}
