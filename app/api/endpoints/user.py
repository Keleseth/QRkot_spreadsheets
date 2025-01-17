from fastapi import APIRouter
from fastapi.routing import APIRoute

from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.core.constants import (
    AUTH,
    AUTH_JWT,
    AUTH_TAG,
    USERS,
    USERS_TAG
)


router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=AUTH_JWT,
    tags=[AUTH_TAG],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=AUTH,
    tags=[AUTH_TAG],
)
users_router = fastapi_users.get_users_router(UserRead, UserUpdate)
users_router.routes = [
    route for route in users_router.routes
    if isinstance(route, APIRoute) and route.name != 'users:delete_user'
]
router.include_router(
    users_router,
    prefix=USERS,
    tags=[USERS_TAG],
)
