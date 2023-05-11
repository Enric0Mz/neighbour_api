from datetime import datetime

from api.base_app.model import Model


class BaseNeed(Model):
    description: str
    period: str


class CreateNeed(BaseNeed):
    product_id: int
    user_id: int


class BaseLoan(Model):
    devolution_date: datetime


class CreateLoan(BaseLoan):
    loan_date: datetime
    user_id: int
    product_id: int
