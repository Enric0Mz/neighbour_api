from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self):
        self._connection_string = (
            "mysql+aiomysql://root:senha@localhost:3306/neighbor_app"
        )
        self._async_engine = None

    def create_async_engine(self) -> AsyncEngine:
        if self._async_engine:
            return self._async_engine

        self._async_engine = create_async_engine(self._connection_string, echo=False)

        return self._async_engine

    def create_session(self) -> AsyncSession:
        if not self._async_engine:
            self.create_async_engine()
        async_session = sessionmaker(
            self._async_engine, class_=AsyncSession, expire_on_commit=False
        )
        session: AsyncSession = async_session()
        return session
