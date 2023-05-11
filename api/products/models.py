from api.base_app.model import BaseModel


class Product(BaseModel):
    name: str
    description: str


class InsertProduct(Product):
    user_id: int
