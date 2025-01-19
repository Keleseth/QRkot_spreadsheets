from fastapi import APIRouter

from app.api.endpoints import (
    charity_project_router,
    donation_router,
    user_router,
    google_router
)
from app.core.constants import (
    CHARITY_PROJECT_API_PATH,
    CHARITY_PROJECT_TAGS,
    DONATION_API_PATH,
    DONATION_TAGS,
    GOOGLE_ROUTE,
    GOOGLE_TAG
)


main_router = APIRouter()

main_router.include_router(user_router)
main_router.include_router(
    charity_project_router,
    prefix=CHARITY_PROJECT_API_PATH,
    tags=[CHARITY_PROJECT_TAGS]
)
main_router.include_router(
    donation_router,
    prefix=DONATION_API_PATH,
    tags=[DONATION_TAGS]
)
main_router.include_router(
    google_router,
    prefix=GOOGLE_ROUTE,
    tags=[GOOGLE_TAG]
)
