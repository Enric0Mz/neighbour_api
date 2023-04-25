from fastapi import APIRouter
from fastapi import Depends

from api import common
from api.database.config import DBConnectionHandler
from api.base_app.security.dependecies import protected_route

from .domain import ListProductsByUserUseCase
from . import models


router = APIRouter(dependencies=[Depends(protected_route)])


@router.get("/products", response_model=list[models.Product])
async def list_products(
    user: common.user.BaseUser = Depends(protected_route),
    params: common.page.PageParams = Depends(),
    context: DBConnectionHandler = Depends(),
):
    return await ListProductsByUserUseCase(context, user, params).execute()