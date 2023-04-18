from .config import DBConnectionHandler


class Repository:
    __abstract__ = True

    def __init__(self, context: DBConnectionHandler) -> None:
        self._context = context
