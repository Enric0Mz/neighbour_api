from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path

from api.database.config import DBConnectionHandler
from api.base_app.security.dependecies import protected_route

from . import domain
from . import models


router = APIRouter()


@router.get("/me", response_model=models.BaseUser)
async def get_self_user(
    user: models.BaseUser = Depends(protected_route),
    context: DBConnectionHandler = Depends(),
):
    return await domain.GetSelfUserUseCase(context, user).execute()


@router.patch("/me", status_code=204)
async def update_user(
    user: models.BaseUser = Depends(protected_route),
    payload: models.BaseUser = Body(...),
    context: DBConnectionHandler = Depends(),
):
    await domain.UpdateUserUseCase(context, user, payload).execute()


@router.put("/me/password", status_code=204)
async def update_password(
    user: models.BaseUser = Depends(protected_route),
    payload: models.UpdatePassword = Body(...),
    context: DBConnectionHandler = Depends(),
):
    await domain.UpdatePasswordUseCase(context, user, payload).execute()
