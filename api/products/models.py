from api.base_app.model import Model


class Product(Model):
    id: int
    name: str
    description: str


class SimpleProduct(Model):
    name: str
    description: str


class InsertProduct(SimpleProduct):
    user_id: int
