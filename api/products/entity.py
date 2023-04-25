import sqlalchemy as sa

from database.entity import Entity
from register.entities.user import UserEntity


class ProductEntity(Entity):
    name = sa.Column(sa.String(255))
    description = sa.Column(sa.Text)
    image = sa.Column(sa.String)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    user = sa.orm.relationship(UserEntity)

