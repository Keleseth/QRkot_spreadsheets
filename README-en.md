# QRKot — Donation Platform for Cats and Kittens. Let's support the greatest life form on Earth! 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![FastAPI](https://img.shields.io/badge/fastapi-%2300C7B7.svg?style=for-the-badge&logo=fastapi&logoColor=white) ![FastAPI Users](https://img.shields.io/badge/fastapi--users-%2300C7B7.svg?style=for-the-badge&logo=fastapi&logoColor=white) ![Pydantic](https://img.shields.io/badge/pydantic-%2300A1E0.svg?style=for-the-badge&logo=python&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23F47216.svg?style=for-the-badge&logo=python&logoColor=white) ![Uvicorn](https://img.shields.io/badge/uvicorn-%23007ACC.svg?style=for-the-badge&logo=python&logoColor=white) ![Alembic](https://img.shields.io/badge/alembic-%230071C5.svg?style=for-the-badge&logo=alembic&logoColor=white) ![Swagger](https://img.shields.io/badge/swagger-%2385EA2D.svg?style=for-the-badge&logo=swagger&logoColor=black) ![ReDoc](https://img.shields.io/badge/redoc-%23CB3837.svg?style=for-the-badge&logo=redoc&logoColor=white) ![Google API](https://img.shields.io/badge/google--api-%234285F4.svg?style=for-the-badge&logo=google&logoColor=white)


## Description
QRKot is a donation service designed to support our furry overlords. 
Every user is encouraged to deploy at least 10 servers in their honor! 


## Deployment
Clone the repository and navigate to the project folder:
```bash
git clone https://github.com/Keleseth/QRkot_spreadsheets
```
```bash
cd qrkot_spreadsheets
```
## Required .env variables:
### Create a .env file in the root directory with the following variables:
- APP_TITLE: Application name
- APP_DESCRIPTION: Application description
- SECRET: (a string) A secret key (the more complex, the better)
- DATABASE_URL: Database connection string (e.g., sqlite+aiosqlite:///./app.db)
- Next two variables for creating first superuser after project launch:
  - FIRST_SUPERUSER_EMAIL= string with superuser email
  - FIRST_SUPERUSER_PASSWORD= string with superuser password

- Google API keys: Required for Google API integration. These keys are taken from the JSON file of your service account in the Google Cloud project (e.g., TYPE, PROJECT_ID, PRIVATE_KEY, CLIENT_EMAIL, etc.)
- EMAIL: this key provides access to a google table with closed charity projects to an owner of email

## Virtual Environment and Dependencies
1.  Install Virtual Environment and activate it:

For Windows:
```bash
python -m venv venv
source \venv\Scripts\activate
```

For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
alembic upgrade head
```

## Start the Project
Run the application server using Uvicorn:

```bash
uvicorn app.main:app
```
By default, the project will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage Examples
### Web Interface
Visit the following URLs for the API documentation:
- [Swagger UI](http://127.0.0.1:8000/docs)
- [ReDoc](http://127.0.0.1:8000/redoc)

### API Interface
QRKot supports:
- Creation of charity projects for cats and kittens. 
- Ability to donate to these projects. 
- Automatic distribution of donations across active projects.
- For superuser only: You can upload a list of fully invested projects to your Google Sheets document in your Google Cloud project.

Developed by Alexander Kelesidis. GitHub: [Keleseth](https://github.com/Keleseth)