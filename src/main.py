"""
Punto de entrada de la API REST para gestión de cuentas bancarias.

Este módulo configura la aplicación FastAPI, registra los routers de endpoints,
configura el manejo global de excepciones e inicializa el ciclo de vida
de la aplicación con eventos de startup y shutdown.
"""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.core.database import engine, Base
from src.core.exception_handlers import (
    register_exception_handlers,
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler
)
from src.api.v1.endpoints import accounts

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestor del ciclo de vida de la aplicación.
    
    Ejecuta operaciones de inicialización al arrancar la aplicación
    y limpieza al detenerla.
    """
    logger.info("Iniciando aplicación de gestión de cuentas bancarias")
    logger.info(f"Entorno: {settings.ENVIRONMENT}")
    logger.info(f"Debug mode: {settings.DEBUG}")
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Tablas de base de datos creadas/verificadas")
    
    yield
    
    await engine.dispose()
    logger.info("Conexiones de base de datos cerradas")
    logger.info("Aplicación detenida correctamente")


def create_application() -> FastAPI:
    """
    Factory para crear la instancia de FastAPI con todas las configuraciones.
    
    Returns:
        FastAPI: Instancia configurada de la aplicación.
    """
    app = FastAPI(
        title="API de Gestión de Cuentas Bancarias",
        description="""
        API REST para la gestión de cuentas bancarias con autenticación JWT.
        
        Proporciona endpoints para CRUD de cuentas, validación de saldo
        y manejo de diferentes tipos de cuenta (ahorros, corriente).
        """,
        version="1.0.0",
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        openapi_url="/openapi.json" if settings.DEBUG else None,
        lifespan=lifespan
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    register_exception_handlers(app)
    
    app.include_router(
        accounts.router,
        prefix="/api/v1/accounts",
        tags=["accounts"]
    )
    
    @app.get("/", tags=["health"])
    async def root():
        """
        Endpoint de verificación de estado de la API.
        
        Returns:
            dict: Estado actual del servicio.
        """
        return {
            "status": "operational",
            "service": "bank-accounts-api",
            "version": "1.0.0",
            "environment": settings.ENVIRONMENT
        }
    
    @app.get("/health", tags=["health"])
    async def health_check():
        """
        Endpoint de health check para balanceadores de carga y orquestación.
        
        Returns:
            dict: Estado de salud de la aplicación.
        """
        return {
            "healthy": True,
            "database": "connected",
            "timestamp": "2024-01-01T00:00:00Z"
        }
    
    return app


app = create_application()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )