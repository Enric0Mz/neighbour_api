from fastapi import APIRouter
from fastapi import Depends

from api import common
from api.database.config import DBConnectionHandler
from api.base_app.security.dependecies import protected_route

from . import domain
from . import models


router = APIRouter(dependencies=[Depends(protected_route)])


@router.get("/products", response_model=common.BasePagination[models.Product])
async def list_products(
    user: common.BaseUser = Depends(protected_route),
    params: common.PageParams = Depends(),
    context: DBConnectionHandler = Depends(),
):
    return await domain.ListProductsByUserUseCase(context, user, params).execute()


@router.post("/products")
async def create_product(
    context: DBConnectionHandler = Depends(),
    user: common.BaseUser = Depends(protected_route),
    payload: models.CreateProduct = Depends(),
):
    return await domain.CreateProductUseCase(context, user, payload).execute()
