from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    # Названеи и описание приложения FastAPI проекта
    app_title: str = 'QRKot'
    app_description: str = (
        'APP_DESCRIPTION=Сервис собирающий пожертвования для котиков.'
    )
    # Адрес для настройки соединения с базой данных через sqlalchemy
    database_url: str = 'sqlite+aiosqlite:///./cat_charity_fund.db'
    secret: str = 'SECRET'  # Генерация и проверка JWT токенов проекта

    # Настройки для создания первого суперюзера
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    # Данные для создания объекта cred - доступа к сервис-аккаунту Google.
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None

    # Почта пользователя, которому будет предоставлен доступ к google
    # документу через google drive api.
    email: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
