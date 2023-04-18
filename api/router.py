from fastapi import APIRouter

from . import auth
from . import register
from . import user


router = APIRouter(prefix="/api")


router.include_router(register.router, prefix="/register", tags=["Register"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(user.router, prefix="/user", tags=["User"])
