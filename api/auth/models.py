from datetime import datetime

from api.base_app.model import Model


class Token(Model):
    access_token: str
    expires: datetime
    type: str
    refresh_token: str
