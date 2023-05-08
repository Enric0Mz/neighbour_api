from fastapi import File
from fastapi import Body
from fastapi import UploadFile

from api.base_app.model import BaseModel


class Product(BaseModel):
    name: str
    description: str
    image: str


class CreateProduct(BaseModel):
    name: str = Body(...)
    description: str = Body(...)
    image: UploadFile = File(...) 


class InsertProduct(Product):
    user_id: int