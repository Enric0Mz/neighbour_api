from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordRequestForm

from api.base_app.security.dependecies import protected_route
from api.database.config import DBConnectionHandler

from . import domain, models

router = APIRouter()


@router.post("/token", response_model=models.Token)
async def authenticate(
    payload: OAuth2PasswordRequestForm = Depends(),
    context: DBConnectionHandler = Depends(),
):
    return await domain.UserLoginUseCase(
        context, payload.username, payload.password
    ).execute()


@router.post("/refresh", response_model=models.Token)
async def refresh_session(
    refresh_token: str = Body(..., embed=True),
    context: DBConnectionHandler = Depends(),
):
    return await domain.UserRefreshSessionUseCase(refresh_token, context).execute()


@router.delete("/logout", status_code=204)
async def logout(
    context: DBConnectionHandler = Depends(),
    user: str = Depends(protected_route),
):
    await domain.LogoutUseCase(context, user).execute()
