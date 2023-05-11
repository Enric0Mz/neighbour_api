from datetime import datetime

from api.base_app.model import Model


class Token(Model):
    acess_token: str
    expires: datetime
    type: str
    refresh_token: str
