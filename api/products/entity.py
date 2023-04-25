import sqlalchemy as sa

from api.database.entity import Entity
from api.register.entities.user import UserEntity


class ProductEntity(Entity):
    __tablename__ = 'products'

    name = sa.Column(sa.String(255))
    description = sa.Column(sa.Text)
    image = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    user = sa.orm.relationship(UserEntity)

