from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path
from fastapi import Body

from api.database.config import DBConnectionHandler
from api.base_app.security.dependecies import protected_route
from api.common.user import BaseUser


from . import domain
from . import models


router = APIRouter(dependencies=[Depends(protected_route)])


@router.post("/need", response_model=models.BaseNeed, status_code=201)
async def create_need(
    product_id: int = Path(...),
    context: DBConnectionHandler = Depends(),
    user: BaseUser = Depends(protected_route),
    payload: models.BaseNeed = Body(...),
):
    return await domain.CreateNeedUseCase(context, user, product_id, payload).execute()
