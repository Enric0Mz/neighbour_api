from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path

from api.database.config import DBConnectionHandler

from . import domain
from . import models


router = APIRouter()


@router.post("/", response_model=models.Condominium)
async def insert_condominium(
    payload: models.Condominium = Body(...), context: DBConnectionHandler = Depends()
):
    return await domain.InsertCondominiumUseCase(context, payload).execute()


@router.post("/{condominium_id}", response_model=models.BaseUser, status_code=202)
async def create_user(
    condominium_id: int = Path(...),
    payload: models.CreateUser = Body(...),
    context: DBConnectionHandler = Depends(),
):
    return await domain.CreateUserUseCase(condominium_id, context, payload).execute()
