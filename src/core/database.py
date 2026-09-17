from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from src.core.config import get_settings

Base = declarative_base()


class DatabaseManager:
    """Gestor de la conexión a la base de datos.
    
    Maneja el ciclo de vida del engine y las sesiones de SQLAlchemy
    para operaciones asíncronas con la base de datos.
    """
    
    def __init__(self) -> None:
        self._engine: AsyncEngine | None = None
        self._session_factory: async_sessionmaker[AsyncSession] | None = None
    
    @property
    def engine(self) -> AsyncEngine:
        if self._engine is None:
            raise RuntimeError(
                "DatabaseManager no ha sido inicializado. "
                "Llama a init() antes de usar el engine."
            )
        return self._engine
    
    @property
    def session_factory(self) -> async_sessionmaker[AsyncSession]:
        if self._session_factory is None:
            raise RuntimeError(
                "DatabaseManager no ha sido inicializado. "
                "Llama a init() antes de usar las sesiones."
            )
        return self._session_factory
    
    def init(self, database_url: str | None = None) -> None:
        """Inicializa el engine y la fábrica de sesiones.
        
        Args:
            database_url: URL de conexión a la base de datos.
                         Si no se proporciona, se usa la configuración.
        """
        settings = get_settings()
        url = database_url or settings.database_url
        
        self._engine = create_async_engine(
            url,
            echo=settings.debug,
            pool_size=20,
            max_overflow=10,
            pool_pre_ping=True,
            pool_recycle=3600,
        )
        
        self._session_factory = async_sessionmaker(
            self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )
    
    async def create_tables(self) -> None:
        """Crea todas las tablas definidas en los modelos."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    
    async def drop_tables(self) -> None:
        """Elimina todas las tablas de la base de datos."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
    
    async def close(self) -> None:
        """Cierra las conexiones del pool y el engine."""
        if self._engine is not None:
            await self._engine.dispose()
            self._engine = None
        self._session_factory = None
    
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Generador de sesiones para inyección de dependencias.
        
        Yields:
            AsyncSession: Sesión de base de datos lista para usar.
        """
        if self._session_factory is None:
            raise RuntimeError(
                "DatabaseManager no ha sido inicializado. "
                "Llama a init() antes de obtener sesiones."
            )
        
        async with self._session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise


db_manager = DatabaseManager()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependencia de FastAPI para obtener sesiones de base de datos.
    
    Esta función se usa como dependencia en los endpoints de FastAPI
    para inyectar automáticamente una sesión de base de datos.
    
    Yields:
        AsyncSession: Sesión de base de datos para el handler.
    """
    async for session in db_manager.get_session():
        yield session


async def init_db() -> None:
    """Inicializa la base de datos al iniciar la aplicación."""
    db_manager.init()
    await db_manager.create_tables()


async def close_db() -> None:
    """Cierra las conexiones al detener la aplicación."""
    await db_manager.close()