import sqlalchemy as sa

from api.database.repository import Repository
from api.base_app.filters import comp_equals_filter_clause

from . import models
from .entity import ProductEntity


class ProductRepository(Repository):
    def to_dto(self, obj: ProductEntity) -> models.Product:
        return models.Product.parse_obj(
            {
                "id": obj.id,
                "name": obj.name,
                "description": obj.description,
            }
        )

    async def fetch(self, filters: dict, page: int = 0, limit: int = 100):
        async with self.context.create_session() as session:

            f = comp_equals_filter_clause(ProductEntity, filters)

            q = (
                sa.select(ProductEntity)
                .where(*f)
                .limit(limit)
                .offset(page * limit)
            )

            result = await session.execute(q)

            return [self.to_dto(item) for item in result.scalars().all()]

    async def count(self, filters: dict):
        async with self.context.create_session() as session:
            
            f = comp_equals_filter_clause(ProductEntity, filters)

            q = sa.select(sa.func.count(ProductEntity.id)).where(*f)

            result = await session.execute(q)

            return result.scalar_one()

    async def create(self, model: models.InsertProduct):
        async with self.context.create_session() as session:
            product = ProductEntity(**model.dict())
            session.add(product)
            await session.commit()

            return self.to_dto(product)
