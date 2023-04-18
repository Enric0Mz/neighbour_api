import sqlalchemy as sa

from api.database.entity import Entity


class CondominiumTypeEntity(Entity):
    __tablename__ = "condominium_type"

    name = sa.Column(sa.String(255))
