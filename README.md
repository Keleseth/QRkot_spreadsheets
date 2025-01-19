# Проект для сбора пожертвований для котокотиков и кошечек. Поддержим же величайшую форму жизни на Земле!

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/fastapi-%2300C7B7.svg?style=for-the-badge&logo=fastapi&logoColor=white) ![FastAPI Users](https://img.shields.io/badge/fastapi--users-%2300C7B7.svg?style=for-the-badge&logo=fastapi&logoColor=white) ![Pydantic](https://img.shields.io/badge/pydantic-%2300A1E0.svg?style=for-the-badge&logo=python&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23F47216.svg?style=for-the-badge&logo=python&logoColor=white) ![Uvicorn](https://img.shields.io/badge/uvicorn-%23007ACC.svg?style=for-the-badge&logo=python&logoColor=white) ![Alembic](https://img.shields.io/badge/alembic-%230071C5.svg?style=for-the-badge&logo=alembic&logoColor=white) ![Swagger](https://img.shields.io/badge/swagger-%2385EA2D.svg?style=for-the-badge&logo=swagger&logoColor=black) ![ReDoc](https://img.shields.io/badge/redoc-%23CB3837.svg?style=for-the-badge&logo=redoc&logoColor=white) ![Google API](https://img.shields.io/badge/google--api-%234285F4.svg?style=for-the-badge&logo=google&logoColor=white)


## Описание
QRKot — это сервис для сбора пожертвований на нужды наших пушистых покровителей.
Каждый обязан развернуть минимум 10 серверов 


## Установка
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/Keleseth/QRkot_spreadsheets
```
```bash
cd qrkot_spreadsheets
```
### FASTApi ожидает наличие файла .env в корневой папке проекта с 6 переменными:
- APP_TITLE= Название приложения
- APP_DESCRIPTION= Описание приложения
- SECRET= секретная строка на ваше усмотрение (чем труднее, тем лучше)
- DATABASE_URL= строка подключения к базе данных. напр.(sqlite+aiosqlite:///./название_бд.db)
- Следующие 2 переменные для создания первого суперюзера при запуске проекта:
  - FIRST_SUPERUSER_EMAIL= строка с мейлом суперюзера
  - FIRST_SUPERUSER_PASSWORD= строка с паролем суперюзера
- Ключи Google API: Необходимы для интеграции с Google API. Эти ключи берутся из JSON-файла вашего сервисного аккаунта в проекте Google Cloud (например, TYPE, PROJECT_ID, PRIVATE_KEY, CLIENT_EMAIL и т.д.)
- EMAIL: Этот ключ можно использовать для предоставления доступа к Google таблице с закрытыми Фондами(которые набрали требуемую сумму)


## Установка виртуального окружения и зависимостей
1.  Установите виртуальное окружение и активируйте его:

Если у вас Windows:
```bash
python -m venv venv
source \venv\Scripts\activate
```

или Если у вас Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Установите зависимостей:

```bash
pip install -r requirements.txt
```

3. Примените миграции:

```bash
alembic upgrade head
```

## Запуск проекта
Запустите сервер приложения:

```bash
uvicorn app.main:app
```
По умолчанию проект будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Примеры использования
### Веб-интерфейс
Перейдите по одному из предложенных адресов для ознакомления с api документацией:
- [Swagger UI](http://127.0.0.1:8000/docs) 
- [ReDoc](http://127.0.0.1:8000/redoc)

### API-интерфейс
QRKot поддерживает:
- Создание благотворительных проектов для котиков и кошечек. 
- Возможность донатить в эти проекты. 
- Автоматическое распределение пожертвований по активным проектам.
- Только для пользователя с правами админа. Вы можете выгрузить список проинвестированных проектов в гугл таблицу вашего Google Cloud проекта через API сервис-аккаунта.

Проект разработан Келесидисом Александром. GitHub: [Keleseth](https://github.com/Keleseth)