from api.base_app.model import Model


class BaseNeed(Model):
    description: str
    period: str


class CreateNeed(BaseNeed):
    product_id: int
    user_id: int
