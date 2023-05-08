from api.base_app.model import Model

from datetime import datetime

class BaseNeed(Model):
    description: str
    period: datetime
    