from datetime import datetime

from api import common
from api.database.config import DBConnectionHandler

from . import models
from .repositories.loans import LoanRepository
from .repositories.needs import NeedRepository


class CreateNeedUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        user: common.BaseUser,
        product_id: int,
        payload: models.BaseNeed,
    ) -> None:
        self._repository = NeedRepository(context)
        self._user = user
        self._product_id = product_id
        self._payload = payload

    async def execute(self):
        return await self._repository.create(
            models.CreateNeed(
                **self._payload.dict(),
                product_id=self._product_id,
                user_id=self._user.id,
            )
        )


class ListNeedsUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        params: common.PageParams,
        self_user_only: bool,
        user: common.BaseUser,
    ) -> None:
        self._repository = NeedRepository(context)
        self._params = params
        self._self_user_only = self_user_only
        self._user = user

    async def execute(self):
        filters = {"loan_id": None}
        if self._self_user_only:
            filters["user_id"] = self._user.id

        result = await self._repository.fetch(
            filters, self._params.page, self._params.limit
        )

        total = await self._repository.count()

        total_pages = (
            0 if (total / self._params.limit) == 1 else (total // self._params.limit)
        )

        return common.BasePagination[models.BaseNeed](
            data=result,
            details=common.Details(
                page=self._params.page,
                limit_per_page=self._params.limit,
                total_pages=total_pages,
                total_items=total,
            ),
        )


class CreateLoanUseCase:
    def __init__(
        self,
        context: DBConnectionHandler,
        user: common.BaseUser,
        product_id: int,
        payload: models.BaseLoan,
    ) -> None:
        self._repository = LoanRepository(context)
        self._user = user
        self._product_id = product_id
        self._payload = payload

    async def execute(self):
        return await self._repository.create(
            models.CreateLoan(
                **self._payload.dict(),
                loan_date=datetime.now(),
                product_id=self._product_id,
                user_id=self._user.id,
            )
        )
