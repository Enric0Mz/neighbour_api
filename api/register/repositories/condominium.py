from api.database.config import DBConnectionHandler
from api.register import models
from api.register.entities.condominium import CondominiumEntity


class CondominiumRepository:
    def __init__(self, context: DBConnectionHandler) -> None:
        self._context = context

    def to_dto(self, obj: CondominiumEntity) -> models.Condominium:
        return models.Condominium.parse_obj(
            {
                "name": obj.name,
                "street": obj.street,
                "neighborhood": obj.neighborhood,
                "city": obj.city,
                "state": obj.state,
                "cep": obj.cep,
            }
        )

    async def create(self, model: models.Condominium):
        async with self._context.create_session() as session:
            condominium = CondominiumEntity(**model.dict())
            session.add(condominium)
            await session.commit()
            return self.to_dto(condominium)
