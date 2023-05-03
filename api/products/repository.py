import sqlalchemy as sa

from api.database.repository import Repository

from .entity import ProductEntity
from . import models


class ProductRepository(Repository):
    def to_dto(self, obj: ProductEntity) -> models.Product:
        return models.Product.parse_obj(
            {
                "id": obj.id,
                "name": obj.name,
                "description": obj.description,
                "image": obj.image,
            }
        )

    async def fetch(self, clause, page: int = 0, limit: int = 100):
        async with self._context.create_session() as session:
            
            q = (
                sa.select(ProductEntity)
                .where(ProductEntity.user_id == clause)
                .limit(limit)
                .offset(page * limit)
            )

            result = await session.execute(q)

            return [self.to_dto(item) for item in result.scalars().all()]
        

    async def count(self, clause):
        async with self._context.create_session() as session:

            q =  sa.select(sa.func.count(ProductEntity.id)).where(
                    (ProductEntity.user_id == clause)
                )
            
            result = await session.execute(q)

            return result.scalar_one()
        

    async def create(self, model: models.InsertProduct):
        async with self._context.create_session() as session:

            product = ProductEntity(**model.dict())
            session.add(product)
            await session.commit()

            return self.to_dto(product)