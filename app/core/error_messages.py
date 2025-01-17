
# Общие сообщения об ошибках для проектов и донатов
OBJECT_NOT_FOUND = 'Объект {table_name} с указанным id не найден.'
NO_SUCH_FIELD_IN_MODEL = (
    'Модель {model} не содержит поле {field}'
)
UNIQUE_FIELD_IS_OCCUPIED = (
    '{model_name} c полем {field} = {field_data}'
    ' уже существует'
)

# Сообщения об ошибках для проектов
ALREADY_INVESTED = (
    'Удаление проекта невозможно, т.к. в проект уже инвестировали.'
)
INVESTMENT_EXCEEDS_FULL_AMOUNT = (
    'Инвестированная в проект сумма превышает указанное '
    'вами значение поля - full_amount'
)
FULLY_INVESTED_PROJECT = 'Нельзя изменять полностью проинвестированный проект.'
NOT_FULLY_INVESTED_PROJECT = 'Проект должен быть полностью проинвестирован'

# Сообщения об ошибках для юзеров
SHORT_PASSWORD = 'Password should be at least 3 characters'
NO_EMAIL_IN_PASSWORD = 'Password should not contain e-mail'
EXISTING_USER = 'Пользователь {user} зарегистрирован.'

# Сообщения об ошибках связанных с Google API
PROJECTS_NUMBER_EXCEEDS_TABLE_CAPACITY = (
    'Кол-во проектов превысило вместимость таблицы.'
)
