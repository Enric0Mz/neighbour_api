from base_app.model import BaseModel


class Product(BaseModel):
    name: str
    description: str
    image: str

class CreateProduct(Product):
    user_id: int