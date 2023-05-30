from fastapi import APIRouter, Body, Depends, Path

from api.base_app.security.dependecies import protected_route
from api.common.user import BaseUser
from api.database.config import DBConnectionHandler

from . import domain, models
from api import common

router = APIRouter(dependencies=[Depends(protected_route)])


@router.post("/need/{product_id}", response_model=models.BaseNeed, status_code=201)
async def create_need(
    product_id: int = Path(...),
    context: DBConnectionHandler = Depends(),
    user: BaseUser = Depends(protected_route),
    payload: models.BaseNeed = Body(...),
):
    return await domain.CreateNeedUseCase(context, user, product_id, payload).execute()


@router.get("/need", response_model=common.BasePagination[models.BaseNeed])
async def list_needs(
    context: DBConnectionHandler = Depends(),
    params: common.PageParams = Depends(), 
):
    return await domain.ListNeedsUseCase(context, params).execute()


@router.post("/loan/{product_id}", response_model=models.BaseLoan, status_code=201)
async def create_loan(
    product_id: int = Path(...),
    context: DBConnectionHandler = Depends(),
    user: BaseUser = Depends(protected_route),
    payload: models.BaseLoan = Body(...),
):
    return await domain.CreateLoanUseCase(context, user, product_id, payload).execute()
