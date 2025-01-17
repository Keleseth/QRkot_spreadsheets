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
GOOGLE_TABLE_FORMAT = [
    ['Отчет от', 'insert_date'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]


# Google sheets range
ROWS_RANGE = 100
INSERT_DATA_RANGE = 'A{rows}:E100'
CLEAN_RANGE = 'A1:E100'

# Установка уровня допуска к документу для пользователей
PERMISSION_TYPE = 'user'
PERMISSION_ROLE = 'writer'

# Дефолтная таблица для выгрузки закрытых проектов
PROJECT_TABLE = {
    'properties': {
        'title': 'Список закрытых проектов',
        'locale': 'ru_RU'
    },
    'sheets': [
        {
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Лист1',
                'gridProperties': {
                    'rowCount': ROWS_RANGE,
                    'columnCount': 10
                }
            }
        }
    ]
}
