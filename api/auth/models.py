from api.base_app.model import Model

from datetime import datetime


class Token(Model):
    acess_token: str
    expires: datetime
    type: str
    refresh_token: str
