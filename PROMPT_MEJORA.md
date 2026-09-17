# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Lo que le falta a este proyecto

Esto NO lo tenes que adivinar: salio de comparar el proyecto contra la arquitectura declarada del reto y de un analisis estatico del codigo. Completalo TODO.

### Boilerplate del stack que falta

Sin esto no compila ni arranca. Es andamiaje, no toca nada de lo pedagogico:

- **Capa de interfaz (controller/handler)** — Sin una capa de interfaz explicita, no hay forma de invocar la logica de negocio desde afuera del proceso.

### Referencias colgando en el codigo que si esta

Cada una rompe la compilacion:

- `src/services/account_service.py` — `AccountUpdate.model_dump`: Se invoca `model_dump` sobre `AccountUpdate`, pero esa clase no declara ese metodo. Agregalo con su implementacion real, o usa uno de los que si declara.

## Como saber que terminaste

```bash
el comando de build o arranque canonico del stack elegido
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Contexto técnico original
Crear una API REST con FastAPI, SQLAlchemy y autenticación JWT

### Reto
- Tema: API REST en entorno bancario
- Seniority: junior-l2
- Tipo: practical
- Título: Desarrollo de una API REST para gestión de cuentas bancarias
- Tiempo estimado: 8 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Definición del modelo de datos y autenticación — objetivo: Definir el modelo de datos para las cuentas bancarias y configurar la autenticación JWT. — entregable (NO resolver): Modelo de datos para cuentas bancarias y configuración de autenticación JWT.
- Fase 2: Implementación de endpoints CRUD — objetivo: Implementar los endpoints para crear, leer, actualizar y eliminar cuentas bancarias. — entregable (NO resolver): Endpoints CRUD para cuentas bancarias con validaciones y manejo de errores.
- Fase 3: Optimización y escalabilidad — objetivo: Optimizar la API para manejar el volumen de solicitudes y asegurar la escalabilidad. — entregable (NO resolver): API optimizada y escalable para manejar 10 000 solicitudes por segundo con un tiempo de respuesta promedio de 200 ms.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: requirements.txt ===
fastapi==0.115.0
uvicorn==0.30.1
sqlalchemy==2.0.30
pydantic==2.8.2
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
pytest==8.2.0
httpx==0.27.0
pydantic-settings==2.3.4

// === ARCHIVO: src/main.py ===
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


// === ARCHIVO: src/models/account.py ===
from datetime import datetime
from sqlalchemy import String, Numeric, DateTime, Enum as SQLEnum, Index
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from enum import Enum


class AccountType(str, Enum):
    AHORROS = "ahorros"
    CORRIENTE = "corriente"


class AccountStatus(str, Enum):
    ACTIVA = "activa"
    INACTIVA = "inactiva"


class Base(DeclarativeBase):
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_number: Mapped[str] = mapped_column(
        String(20), unique=True, nullable=False, index=True
    )
    balance: Mapped[float] = mapped_column(
        Numeric(15, 2), nullable=False, default=0.0
    )
    account_type: Mapped[str] = mapped_column(
        SQLEnum(AccountType, name="account_type_enum"), nullable=False
    )
    status: Mapped[str] = mapped_column(
        SQLEnum(AccountStatus, name="account_status_enum"), nullable=False, default=AccountStatus.ACTIVA
    )
    opened_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    __table_args__ = (
        Index("idx_account_number", "account_number", unique=True),
        Index("idx_account_status", "status"),
    )

    def __repr__(self) -> str:
        return f"<Account(id={self.id}, account_number={self.account_number}, balance={self.balance})>"


// === ARCHIVO: src/schemas/account.py ===
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from enum import Enum


class AccountType(str, Enum):
    AHORROS = "ahorros"
    CORRIENTE = "corriente"


class AccountStatus(str, Enum):
    ACTIVA = "activa"
    INACTIVA = "inactiva"


class AccountBase(BaseModel):
    account_number: str = Field(..., min_length=5, max_length=20, description="Número único de cuenta bancaria")
    balance: float = Field(..., ge=0.0, description="Saldo de la cuenta")
    account_type: AccountType = Field(..., description="Tipo de cuenta: ahorros o corriente")

    @field_validator("account_number")
    @classmethod
    def validate_account_number(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError("El número de cuenta debe contener solo caracteres alfanuméricos")
        return v.upper()

    @field_validator("balance")
    @classmethod
    def validate_balance(cls, v: float) -> float:
        if v < 0:
            raise ValueError("El saldo no puede ser negativo")
        return round(v, 2)


class AccountCreate(AccountBase):
    pass


class AccountUpdate(BaseModel):
    account_number: Optional[str] = Field(None, min_length=5, max_length=20)
    balance: Optional[float] = Field(None, ge=0.0)
    account_type: Optional[AccountType] = None
    status: Optional[AccountStatus] = None

    @field_validator("account_number")
    @classmethod
    def validate_account_number(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            if not v.isalnum():
                raise ValueError("El número de cuenta debe contener solo caracteres alfanuméricos")
            return v.upper()
        return v

    @field_validator("balance")
    @classmethod
    def validate_balance(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and v < 0:
            raise ValueError("El saldo no puede ser negativo")
        return round(v, 2) if v is not None else v


class AccountResponse(AccountBase):
    id: int
    status: AccountStatus
    opened_at: datetime
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class AccountListResponse(BaseModel):
    total: int
    accounts: list[AccountResponse]


class AccountBalanceUpdate(BaseModel):
    new_balance: float = Field(..., ge=0.0, description="Nuevo saldo de la cuenta")

    @field_validator("new_balance")
    @classmethod
    def validate_balance(cls, v: float) -> float:
        if v < 0:
            raise ValueError("El saldo no puede ser negativo")
        return round(v, 2)


class AccountStatusUpdate(BaseModel):
    status: AccountStatus = Field(..., description="Nuevo estado de la cuenta")


// === ARCHIVO: src/repositories/account_repository.py ===
from typing import Optional, List
from sqlalchemy import select, update, delete, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.models.account import Account, AccountType, AccountStatus


class AccountRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, account: Account) -> Account:
        self.session.add(account)
        await self.session.flush()
        await self.session.refresh(account)
        return account

    async def get_by_id(self, account_id: int) -> Optional[Account]:
        result = await self.session.execute(
            select(Account).where(Account.id == account_id)
        )
        return result.scalar_one_or_none()

    async def get_by_account_number(self, account_number: str) -> Optional[Account]:
        result = await self.session.execute(
            select(Account).where(Account.account_number == account_number.upper())
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Account]:
        result = await self.session.execute(
            select(Account).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    async def get_by_status(self, status: AccountStatus, skip: int = 0, limit: int = 100) -> List[Account]:
        result = await self.session.execute(
            select(Account).where(Account.status == status.value).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    async def get_by_type(self, account_type: AccountType, skip: int = 0, limit: int = 100) -> List[Account]:
        result = await self.session.execute(
            select(Account).where(Account.account_type == account_type.value).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    async def update(self, account_id: int, update_data: dict) -> Optional[Account]:
        stmt = (
            update(Account)
            .where(Account.id == account_id)
            .values(**update_data)
            .returning(Account)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_balance(self, account_id: int, new_balance: float) -> Optional[Account]:
        stmt = (
            update(Account)
            .where(Account.id == account_id)
            .values(balance=new_balance)
            .returning(Account)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update_status(self, account_id: int, status: AccountStatus) -> Optional[Account]:
        stmt = (
            update(Account)
            .where(Account.id == account_id)
            .values(status=status.value)
            .returning(Account)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def delete(self, account_id: int) -> bool:
        stmt = delete(Account).where(Account.id == account_id)
        result = await self.session.execute(stmt)
        await self.session.flush()
        return result.rowcount > 0

    async def exists_by_account_number(self, account_number: str) -> bool:
        result = await self.session.execute(
            select(Account).where(Account.account_number == account_number.upper())
        )
        return result.scalar_one_or_none() is not None

    async def count_all(self) -> int:
        result = await self.session.execute(select(Account))
        return len(list(result.scalars().all()))

    async def search(
        self,
        account_number: Optional[str] = None,
        status: Optional[AccountStatus] = None,
        account_type: Optional[AccountType] = None,
        min_balance: Optional[float] = None,
        max_balance: Optional[float] = None,
        skip: int = 0,
        limit: int = 100
    ) -> List[Account]:
        conditions = []
        if account_number:
            conditions.append(Account.account_number.ilike(f"%{account_number}%"))
        if status:
            conditions.append(Account.status == status.value)
        if account_type:
            conditions.append(Account.account_type == account_type.value)
        if min_balance is not None:
            conditions.append(Account.balance >= min_balance)
        if max_balance is not None:
            conditions.append(Account.balance <= max_balance)

        query = select(Account)
        if conditions:
            query = query.where(and_(*conditions))

        query = query.offset(skip).limit(limit)
        result = await self.session.execute(query)
        return list(result.scalars().all())


// === ARCHIVO: src/core/config.py ===
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    app_name: str = "Banking API"
    app_version: str = "1.0.0"
    debug: bool = False

    database_url: str = "sqlite+aiosqlite:///./banking.db"
    database_echo: bool = False
    database_pool_size: int = 20
    database_max_overflow: int = 10

    jwt_secret_key: str = "supersecretkeychangemeinproduction123456789"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7

    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8000"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list[str] = ["*"]
    cors_allow_headers: list[str] = ["*"]

    api_v1_prefix: str = "/api/v1"
    api_title: str = "Banking Account Management API"
    api_description: str = "API REST para gestión de cuentas bancarias"

    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @property
    def is_production(self) -> bool:
        return not self.debug

    @property
    def database_pool_config(self) -> dict:
        return {
            "pool_size": self.database_pool_size,
            "max_overflow": self.database_max_overflow,
            "pool_pre_ping": True,
            "pool_recycle": 3600
        }


settings = Settings()


def get_settings() -> Settings:
    return settings


// === ARCHIVO: src/core/security/jwt.py ===
from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class JWTHandler:
    def __init__(self):
        self.secret_key = settings.jwt_secret_key
        self.algorithm = settings.jwt_algorithm
        self.access_token_expire_minutes = settings.jwt_access_token_expire_minutes
        self.refresh_token_expire_days = settings.jwt_refresh_token_expire_days

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=self.access_token_expire_minutes)
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def create_refresh_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(days=self.refresh_token_expire_days)
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def decode_token(self, token: str) -> Optional[dict]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except JWTError:
            return None

    def verify_token(self, token: str) -> bool:
        payload = self.decode_token(token)
        if payload is None:
            return False
        token_type = payload.get("type")
        if token_type != "access":
            return False
        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc):
            return False
        return True

    def get_subject_from_token(self, token: str) -> Optional[str]:
        payload = self.decode_token(token)
        if payload:
            return payload.get("sub")
        return None

    def create_token_pair(self, user_id: int, username: str) -> dict[str, str]:
        access_token = self.create_access_token(data={"sub": str(user_id), "username": username})
        refresh_token = self.create_refresh_token(data={"sub": str(user_id), "username": username})
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }


jwt_handler = JWTHandler()


def get_jwt_handler() -> JWTHandler:
    return jwt_handler


// === ARCHIVO: src/core/security/auth_middleware.py ===
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from src.core.security.jwt import jwt_handler, JWTHandler


security = HTTPBearer(auto_error=False)


class AuthMiddleware:
    def __init__(self, jwt_handler: JWTHandler):
        self.jwt_handler = jwt_handler

    async def get_current_user(
        self,
        credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
    ) -> dict:
        if credentials is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se proporcionó token de autenticación",
                headers={"WWW-Authenticate": "Bearer"}
            )
        token = credentials.credentials
        if not self.jwt_handler.verify_token(token):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido o expirado",
                headers={"WWW-Authenticate": "Bearer"}
            )
        payload = self.jwt_handler.decode_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No se pudo validar el token",
                headers={"WWW-Authenticate": "Bearer"}
            )
        user_id = payload.get("sub")
        username = payload.get("username")
        if user_id is None or username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token sin información de usuario",
                headers={"WWW-Authenticate": "Bearer"}
            )
        return {"user_id": int(user_id), "username": username}

    async def get_optional_current_user(
        self,
        credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)
    ) -> Optional[dict]:
        if credentials is None:
            return None
        token = credentials.credentials
        if not self.jwt_handler.verify_token(token):
            return None
        payload = self.jwt_handler.decode_token(token)
        if payload is None:
            return None
        user_id = payload.get("sub")
        username = payload.get("username")
        if user_id is None or username is None:
            return None
        return {"user_id": int(user_id), "username": username}

    def require_role(self, allowed_roles: list[str]):
        async def role_checker(current_user: dict = Depends(self.get_current_user)) -> dict:
            user_role = current_user.get("role", "user")
            if user_role not in allowed_roles:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="No tiene permisos suficientes para esta acción"
                )
            return current_user
        return role_checker


auth_middleware = AuthMiddleware(jwt_handler)


def get_auth_middleware() -> AuthMiddleware:
    return auth_middleware


async def get_current_user(current_user: dict = Depends(auth_middleware.get_current_user)) -> dict:
    return current_user


async def get_optional_user(current_user: Optional[dict] = Depends(auth_middleware.get_optional_current_user)) -> Optional[dict]:
    return current_user


// === ARCHIVO: src/core/database.py ===
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
// === ARCHIVO: src/core/exceptions.py ===
from typing import Any


class BankingException(Exception):
    """Excepción base para errores del dominio bancario.
    
    Todas las excepciones personalizadas del sistema heredan de esta clase
    para facilitar el manejo global de errores y proporcionar una estructura
    consistente para los mensajes de error.
    """
    
    def __init__(
        self,
        message: str = "Ha ocurrido un error en el sistema bancario",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.details = details or {}
    
    def to_dict(self) -> dict[str, Any]:
        """Convierte la excepción a un diccionario para respuesta JSON."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


class CuentaNoEncontradaError(BankingException):
    """Excepción lanzada cuando no se encuentra una cuenta bancaria.
    
    Se usa cuando se intenta operar sobre una cuenta que no existe
    en la base de datos, ya sea por ID o número de cuenta.
    """
    
    def __init__(
        self,
        identifier: str | int,
        identifier_type: str = "id",
    ) -> None:
        message = f"Cuenta no encontrada con {identifier_type}: {identifier}"
        details = {"identifier": identifier, "type": identifier_type}
        super().__init__(message, details)


class SaldoNegativoError(BankingException):
    """Excepción lanzada cuando el saldo de una cuenta es negativo.
    
    El sistema bancario no permite saldos negativos. Esta excepción
    se lanza cuando se intenta establecer un saldo menor a cero.
    """
    
    def __init__(
        self,
        saldo_actual: float,
        monto_solicitado: float | None = None,
    ) -> None:
        details = {"saldo_actual": saldo_actual}
        if monto_solicitado is not None:
            details["monto_solicitado"] = monto_solicitado
        
        message = (
            f"El saldo no puede ser negativo. "
            f"Saldo actual: {saldo_actual}"
        )
        super().__init__(message, details)


class NumeroCuentaDuplicadoError(BankingException):
    """Excepción lanzada cuando se intenta crear una cuenta con número duplicado.
    
    Cada cuenta bancaria debe tener un número único. Esta excepción
    se lanza cuando se detecta que el número de cuenta ya existe.
    """
    
    def __init__(
        self,
        numero_cuenta: str,
    ) -> None:
        message = f"Ya existe una cuenta con el número: {numero_cuenta}"
        details = {"numero_cuenta": numero_cuenta}
        super().__init__(message, details)


class CuentaInactivaError(BankingException):
    """Excepción lanzada cuando se opera sobre una cuenta inactiva.
    
    Las cuentas inactivas no pueden realizar operaciones como
    depósitos, retiros o transferencias.
    """
    
    def __init__(
        self,
        numero_cuenta: str,
        estado: str,
    ) -> None:
        message = (
            f"La cuenta {numero_cuenta} no puede realizar operaciones. "
            f"Estado actual: {estado}"
        )
        details = {"numero_cuenta": numero_cuenta, "estado": estado}
        super().__init__(message, details)


class TipoCuentaInvalidoError(BankingException):
    """Excepción lanzada cuando se especifica un tipo de cuenta inválido.
    
    Los tipos de cuenta válidos son: AHORROS, CORRIENTE.
    """
    
    def __init__(
        self,
        tipo_proporcionado: str,
    ) -> None:
        message = (
            f"Tipo de cuenta inválido: {tipo_proporcionado}. "
            f"Tipos válidos: AHORROS, CORRIENTE"
        )
        details = {"tipo_proporcionado": tipo_proporcionado}
        super().__init__(message, details)


class AutenticacionError(BankingException):
    """Excepción lanzada cuando falla la autenticación del usuario.
    
    Se usa cuando las credenciales proporcionadas son incorrectas
    o el token JWT es inválido o ha expirado.
    """
    
    def __init__(
        self,
        reason: str = "Credenciales inválidas",
    ) -> None:
        message = f"Error de autenticación: {reason}"
        details = {"reason": reason}
        super().__init__(message, details)


class AutorizacionError(BankingException):
    """Excepción lanzada cuando el usuario no tiene permisos.
    
    Se usa cuando un usuario autenticado intenta acceder a recursos
    o realizar operaciones para las cuales no tiene autorización.
    """
    
    def __init__(
        self,
        resource: str,
        action: str,
    ) -> None:
        message = (
            f"No tiene permisos para realizar la acción '{action}' "
            f"sobre el recurso: {resource}"
        )
        details = {"resource": resource, "action": action}
        super().__init__(message, details)


class ValidacionError(BankingException):
    """Excepción lanzada cuando falla la validación de datos.
    
    Se usa para errores de validación que no encajan en categorías
    más específicas como SaldoNegativoError o TipoCuentaInvalidoError.
    """
    
    def __init__(
        self,
        field: str,
        reason: str,
    ) -> None:
        message = f"Error de validación en '{field}': {reason}"
        details = {"field": field, "reason": reason}
        super().__init__(message, details)


class ErrorInternoError(BankingException):
    """Excepción para errores internos inesperados del servidor.
    
    Esta excepción se usa para errores que no deberían ocurrir en
    condiciones normales de operación y que indican un problema
    interno en el sistema.
    """
    
    def __init__(
        self,
        operation: str,
        original_error: Exception | None = None,
    ) -> None:
        message = f"Error interno al realizar operación: {operation}"
        details = {
            "operation": operation,
            "original_error": str(original_error) if original_error else None,
        }
        super().__init__(message, details)


class OperacionNoPermitidaError(BankingException):
    """Excepción cuando una operación no está permitida por reglas de negocio.
    
    Se usa para operaciones que técnicamente son válidas pero las
    reglas de negocio no permiten en ciertos contextos.
    """
    
    def __init__(
        self,
        operacion: str,
        razon: str,
    ) -> None:
        message = f"Operación '{operacion}' no permitida: {razon}"
        details = {"operacion": operacion, "razon": razon}
        super().__init__(message, details)
// === ARCHIVO: src/core/exception_handlers.py ===
from typing import Any
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.core.exceptions import (
    BankingException,
    CuentaNoEncontradaError,
    SaldoNegativoError,
    NumeroCuentaDuplicadoError,
    CuentaInactivaError,
    TipoCuentaInvalidoError,
    AutenticacionError,
    AutorizacionError,
    ValidacionError,
    ErrorInternoError,
    OperacionNoPermitidaError,
)


class ErrorResponse(Base):
    """Modelo de respuesta de error estándar."""
    error: str
    message: str
    details: dict[str, Any] | None = None


async def banking_exception_handler(
    request: Request,
    exc: BankingException,
) -> JSONResponse:
    """Manejador genérico para excepciones del dominio bancario.
    
    Convierte cualquier BankingException en una respuesta HTTP consistente
    con el formato de error del sistema.
    
    Args:
        request: Objeto de request de FastAPI.
        exc: Excepción del dominio bancario.
    
    Returns:
        JSONResponse con el formato de error estándar.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exc.to_dict(),
    )


async def cuenta_no_encontrada_handler(
    request: Request,
    exc: CuentaNoEncontradaError,
) -> JSONResponse:
    """Manejador para CuentaNoEncontradaError.
    
    Devuelve 404 Not Found cuando no se encuentra una cuenta.
    """
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=exc.to_dict(),
    )


async def saldo_negativo_handler(
    request: Request,
    exc: SaldoNegativoError,
) -> JSONResponse:
    """Manejador para SaldoNegativoError.
    
    Devuelve 400 Bad Request cuando se intenta establecer saldo negativo.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exc.to_dict(),
    )


async def numero_cuenta_duplicado_handler(
    request: Request,
    exc: NumeroCuentaDuplicadoError,
) -> JSONResponse:
    """Manejador para NumeroCuentaDuplicadoError.
    
    Devuelve 409 Conflict cuando el número de cuenta ya existe.
    """
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content=exc.to_dict(),
    )


async def cuenta_inactiva_handler(
    request: Request,
    exc: CuentaInactivaError,
) -> JSONResponse:
    """Manejador para CuentaInactivaError.
    
    Devuelve 403 Forbidden cuando se opera sobre cuenta inactiva.
    """
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=exc.to_dict(),
    )


async def tipo_cuenta_invalido_handler(
    request: Request,
    exc: TipoCuentaInvalidoError,
) -> JSONResponse:
    """Manejador para TipoCuentaInvalidoError.
    
    Devuelve 400 Bad Request cuando el tipo de cuenta es inválido.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exc.to_dict(),
    )


async def autenticacion_error_handler(
    request: Request,
    exc: AutenticacionError,
) -> JSONResponse:
    """Manejador para AutenticacionError.
    
    Devuelve 401 Unauthorized cuando falla la autenticación.
    """
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content=exc.to_dict(),
    )


async def autorizacion_error_handler(
    request: Request,
    exc: AutorizacionError,
) -> JSONResponse:
    """Manejador para AutorizacionError.
    
    Devuelve 403 Forbidden cuando el usuario no tiene permisos.
    """
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content=exc.to_dict(),
    )


async def validacion_error_handler(
    request: Request,
    exc: ValidacionError,
) -> JSONResponse:
    """Manejador para ValidacionError.
    
    Devuelve 400 Bad Request cuando falla la validación de datos.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exc.to_dict(),
    )


async def error_interno_handler(
    request: Request,
    exc: ErrorInternoError,
) -> JSONResponse:
    """Manejador para ErrorInternoError.
    
    Devuelve 500 Internal Server Error para errores internos.
    En producción, no incluye detalles del error original por seguridad.
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "ErrorInternoError",
            "message": "Ha ocurrido un error interno en el sistema. "
                       "Por favor, contacte al administrador.",
            "details": None,
        },
    )


async def operacion_no_permitida_handler(
    request: Request,
    exc: OperacionNoPermitidaError,
) -> JSONResponse:
    """Manejador para OperacionNoPermitidaError.
    
    Devuelve 422 Unprocessable Entity cuando una operación
    no está permitida por reglas de negocio.
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=exc.to_dict(),
    )


async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    """Manejador para excepciones HTTP de Starlette.
    
    Convierte excepciones HTTP estándar al formato de respuesta
    del sistema bancario.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTPException",
            "message": exc.detail,
            "details": None,
        },
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    """Manejador para errores de validación de FastAPI/Pydantic.
    
    Devuelve 422 Unprocessable Entity con los detalles de los
    errores de validación de los datos de entrada.
    """
    errors = []
    for error in exc.errors():
        errors.append({
            "field": ".".join(str(loc) for loc in error["loc"]),
            "message": error["msg"],
            "type": error["type"],
        })
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "ValidationError",
            "message": "Error de validación en los datos de entrada",
            "details": {"validation_errors": errors},
        },
    )


def register_exception_handlers(app) -> None:
    """Registra todos los manejadores de excepciones en la aplicación FastAPI.
    
    Args:
        app: Instancia de la aplicación FastAPI.
    """
    app.add_exception_handler(BankingException, banking_exception_handler)
    app.add_exception_handler(
        CuentaNoEncontradaError, cuenta_no_encontrada_handler
    )
    app.add_exception_handler(SaldoNegativoError, saldo_negativo_handler)
    app.add_exception_handler(
        NumeroCuentaDuplicadoError, numero_cuenta_duplicado_handler
    )
    app.add_exception_handler(CuentaInactivaError, cuenta_inactiva_handler)
    app.add_exception_handler(
        TipoCuentaInvalidoError, tipo_cuenta_invalido_handler
    )
    app.add_exception_handler(AutenticacionError, autenticacion_error_handler)
    app.add_exception_handler(AutorizacionError, autorizacion_error_handler)
    app.add_exception_handler(ValidacionError, validacion_error_handler)
    app.add_exception_handler(ErrorInternoError, error_interno_handler)
    app.add_exception_handler(
        OperacionNoPermitidaError, operacion_no_permitida_handler
    )
    app.add_exception_handler(
        StarletteHTTPException, http_exception_handler
    )
    app.add_exception_handler(
        RequestValidationError, validation_exception_handler
    )


// === ARCHIVO: src/services/account_service.py ===
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models.account import Account, AccountStatus, AccountType
from src.repositories.account_repository import AccountRepository
from src.schemas.account import (
    AccountCreate,
    AccountUpdate,
    AccountResponse,
    AccountListResponse,
    AccountBalanceUpdate,
    AccountStatusUpdate,
)
from src.core.exceptions import (
    AccountNotFoundException,
    AccountNumberAlreadyExistsException,
    InvalidAccountDataException,
)


class AccountService:
    """Capa de servicio para operaciones de cuentas bancarias.
    
    Coordina la lógica de negocio entre los endpoints de la API y el repositorio,
    aplicando validaciones de reglas de negocio y manejo de errores.
    """

    def __init__(self, session: AsyncSession):
        self.repository = AccountRepository(session)

    async def create_account(self, account_data: AccountCreate) -> AccountResponse:
        """Crea una nueva cuenta bancaria con validaciones de negocio."""
        if await self.repository.exists_by_account_number(account_data.account_number):
            raise AccountNumberAlreadyExistsException(
                f"El número de cuenta {account_data.account_number} ya existe"
            )

        if account_data.balance < 0:
            raise InvalidAccountDataException(
                "El saldo no puede ser negativo"
            )

        account = Account(
            account_number=account_data.account_number,
            balance=account_data.balance,
            account_type=AccountType(account_data.account_type),
            status=AccountStatus.ACTIVE,
            customer_id=account_data.customer_id,
        )

        try:
            created_account = await self.repository.create(account)
            return self._to_response(created_account)
        except IntegrityError as e:
            raise AccountNumberAlreadyExistsException(
                "El número de cuenta ya existe en el sistema"
            ) from e

    async def get_account(self, account_id: int) -> AccountResponse:
        """Obtiene una cuenta por su ID."""
        account = await self.repository.get_by_id(account_id)
        if not account:
            raise AccountNotFoundException(
                f"Cuenta con ID {account_id} no encontrada"
            )
        return self._to_response(account)

    async def get_account_by_number(self, account_number: str) -> AccountResponse:
        """Obtiene una cuenta por su número de cuenta."""
        account = await self.repository.get_by_account_number(account_number)
        if not account:
            raise AccountNotFoundException(
                f"Cuenta con número {account_number} no encontrada"
            )
        return self._to_response(account)

    async def list_accounts(
        self,
        skip: int = 0,
        limit: int = 100,
        status: Optional[AccountStatus] = None,
        account_type: Optional[AccountType] = None,
    ) -> AccountListResponse:
        """Lista cuentas con filtros opcionales de paginación y criterios."""
        if status and account_type:
            accounts = await self.repository.get_by_status(status, skip, limit)
            accounts = [a for a in accounts if a.account_type == account_type]
        elif status:
            accounts = await self.repository.get_by_status(status, skip, limit)
        elif account_type:
            accounts = await self.repository.get_by_type(account_type, skip, limit)
        else:
            accounts = await self.repository.get_all(skip, limit)

        total = await self.repository.count_all()
        account_responses = [self._to_response(acc) for acc in accounts]

        return AccountListResponse(
            accounts=account_responses,
            total=total,
            skip=skip,
            limit=limit,
        )

    async def update_account(
        self,
        account_id: int,
        update_data: AccountUpdate,
    ) -> AccountResponse:
        """Actualiza una cuenta existente."""
        existing_account = await self.repository.get_by_id(account_id)
        if not existing_account:
            raise AccountNotFoundException(
                f"Cuenta con ID {account_id} no encontrada"
            )

        update_dict = update_data.model_dump(exclude_unset=True)

        if "account_number" in update_dict:
            new_account_number = update_dict["account_number"]
            if new_account_number != existing_account.account_number:
                if await self.repository.exists_by_account_number(new_account_number):
                    raise AccountNumberAlreadyExistsException(
                        f"El número de cuenta {new_account_number} ya existe"
                    )

        if "balance" in update_dict and update_dict["balance"] is not None:
            if update_dict["balance"] < 0:
                raise InvalidAccountDataException(
                    "El saldo no puede ser negativo"
                )

        updated_account = await self.repository.update(account_id, update_dict)
        if not updated_account:
            raise AccountNotFoundException(
                f"Error al actualizar la cuenta {account_id}"
            )
        return self._to_response(updated_account)

    async def update_balance(
        self,
        account_id: int,
        balance_update: AccountBalanceUpdate,
    ) -> AccountResponse:
        """Actualiza el saldo de una cuenta."""
        account = await self.repository.get_by_id(account_id)
        if not account:
            raise AccountNotFoundException(
                f"Cuenta con ID {account_id} no encontrada"
            )

        if balance_update.balance < 0:
            raise InvalidAccountDataException(
                "El saldo no puede ser negativo"
            )

        updated_account = await self.repository.update_balance(
            account_id, balance_update.balance
        )
        return self._to_response(updated_account)

    async def update_status(
        self,
        account_id: int,
        status_update: AccountStatusUpdate,
    ) -> AccountResponse:
        """Actualiza el estado de una cuenta."""
        account = await self.repository.get_by_id(account_id)
        if not account:
            raise AccountNotFoundException(
                f"Cuenta con ID {account_id} no encontrada"
            )

        new_status = AccountStatus(status_update.status)
        updated_account = await self.repository.update_status(account_id, new_status)
        return self._to_response(updated_account)

    async def delete_account(self, account_id: int) -> bool:
        """Elimina una cuenta del sistema."""
        account = await self.repository.get_by_id(account_id)
        if not account:
            raise AccountNotFoundException(
                f"Cuenta con ID {account_id} no encontrada"
            )

        return await self.repository.delete(account_id)

    def _to_response(self, account: Account) -> AccountResponse:
        """Convierte una entidad de dominio a esquema de respuesta."""
        return AccountResponse(
            id=account.id,
            account_number=account.account_number,
            balance=account.balance,
            account_type=account.account_type.value,
            status=account.status.value,
            customer_id=account.customer_id,
            opened_at=account.opened_at,
            created_at=account.created_at,
            updated_at=account.updated_at,
        )


// === ARCHIVO: src/api/v1/endpoints/accounts.py ===
from typing import Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db_session
from src.core.security.auth_middleware import get_current_active_user
from src.models.account import AccountStatus, AccountType
from src.schemas.account import (
    AccountCreate,
    AccountUpdate,
    AccountResponse,
    AccountListResponse,
    AccountBalanceUpdate,
    AccountStatusUpdate,
)
from src.services.account_service import AccountService
from src.core.exceptions import (
    AccountNotFoundException,
    AccountNumberAlreadyExistsException,
    InvalidAccountDataException,
)

router = APIRouter(prefix="/accounts", tags=["accounts"])


def get_account_service(session: AsyncSession = Depends(get_db_session)) -> AccountService:
    """Proveedor de inyección de dependencias para el servicio de cuentas."""
    return AccountService(session)


@router.post(
    "",
    response_model=AccountResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear cuenta bancaria",
    description="Crea una nueva cuenta bancaria en el sistema",
)
async def create_account(
    account_data: AccountCreate,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountResponse:
    """Endpoint para crear una nueva cuenta bancaria.
    
    Valida que el número de cuenta sea único y que el saldo inicial no sea negativo.
    """
    return await service.create_account(account_data)


@router.get(
    "",
    response_model=AccountListResponse,
    summary="Listar cuentas",
    description="Obtiene una lista paginada de cuentas con filtros opcionales",
)
async def list_accounts(
    skip: int = Query(0, ge=0, description="Número de registros a omitir"),
    limit: int = Query(100, ge=1, le=1000, description="Límite de registros a retornar"),
    status_filter: Optional[AccountStatus] = Query(None, alias="status", description="Filtrar por estado"),
    account_type: Optional[AccountType] = Query(None, alias="type", description="Filtrar por tipo de cuenta"),
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountListResponse:
    """Endpoint para listar cuentas con soporte de paginación y filtros."""
    return await service.list_accounts(
        skip=skip,
        limit=limit,
        status=status_filter,
        account_type=account_type,
    )


@router.get(
    "/{account_id}",
    response_model=AccountResponse,
    summary="Obtener cuenta por ID",
    description="Retorna los detalles de una cuenta específica",
)
async def get_account(
    account_id: int,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountResponse:
    """Endpoint para obtener una cuenta por su identificador."""
    return await service.get_account(account_id)


@router.get(
    "/number/{account_number}",
    response_model=AccountResponse,
    summary="Obtener cuenta por número",
    description="Retorna los detalles de una cuenta por su número",
)
async def get_account_by_number(
    account_number: str,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountResponse:
    """Endpoint para obtener una cuenta por su número de cuenta."""
    return await service.get_account_by_number(account_number)


@router.put(
    "/{account_id}",
    response_model=AccountResponse,
    summary="Actualizar cuenta",
    description="Actualiza los datos de una cuenta existente",
)
async def update_account(
    account_id: int,
    account_data: AccountUpdate,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountResponse:
    """Endpoint para actualizar una cuenta existente.
    
    Permite modificar número de cuenta, saldo, tipo y estado.
    """
    return await service.update_account(account_id, account_data)


@router.patch(
    "/{account_id}/balance",
    response_model=AccountResponse,
    summary="Actualizar saldo",
    description="Actualiza únicamente el saldo de una cuenta",
)
async def update_balance(
    account_id: int,
    balance_update: AccountBalanceUpdate,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountResponse:
    """Endpoint para actualizar el saldo de una cuenta."""
    return await service.update_balance(account_id, balance_update)


@router.patch(
    "/{account_id}/status",
    response_model=AccountResponse,
    summary="Actualizar estado",
    description="Actualiza únicamente el estado de una cuenta",
)
async def update_status(
    account_id: int,
    status_update: AccountStatusUpdate,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> AccountResponse:
    """Endpoint para actualizar el estado de una cuenta."""
    return await service.update_status(account_id, status_update)


@router.delete(
    "/{account_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar cuenta",
    description="Elimina una cuenta del sistema",
)
async def delete_account(
    account_id: int,
    service: AccountService = Depends(get_account_service),
    current_user: dict = Depends(get_current_active_user),
) -> None:
    """Endpoint para eliminar una cuenta del sistema."""
    await service.delete_account(account_id)


// === ARCHIVO: tests/test_accounts.py ===
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from datetime import datetime

from src.models.account import Account, AccountStatus, AccountType
from src.schemas.account import (
    AccountCreate,
    AccountUpdate,
    AccountResponse,
    AccountBalanceUpdate,
    AccountStatusUpdate,
)
from src.services.account_service import AccountService
from src.core.exceptions import (
    AccountNotFoundException,
    AccountNumberAlreadyExistsException,
    InvalidAccountDataException,
)


@pytest.fixture
def mock_session():
    """Fixture que provee una sesión mockeada de base de datos."""
    return AsyncMock()


@pytest.fixture
def account_service(mock_session):
    """Fixture que provee una instancia del servicio de cuentas."""
    return AccountService(mock_session)


@pytest.fixture
def sample_account():
    """Fixture que provee una cuenta de ejemplo para tests."""
    account = Account(
        id=1,
        account_number="1234567890",
        balance=1000.0,
        account_type=AccountType.SAVINGS,
        status=AccountStatus.ACTIVE,
        customer_id=100,
        opened_at=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return account


@pytest.fixture
def sample_account_response():
    """Fixture que provee una respuesta de cuenta de ejemplo."""
    return AccountResponse(
        id=1,
        account_number="1234567890",
        balance=1000.0,
        account_type="savings",
        status="active",
        customer_id=100,
        opened_at=datetime.now(),
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )


class TestAccountServiceCreate:
    """Tests para la creación de cuentas."""

    @pytest.mark.asyncio
    async def test_create_account_success(self, account_service, mock_session, sample_account):
        """Verifica que se puede crear una cuenta exitosamente."""
        account_service.repository.exists_by_account_number = AsyncMock(return_value=False)
        account_service.repository.create = AsyncMock(return_value=sample_account)

        account_data = AccountCreate(
            account_number="1234567890",
            balance=1000.0,
            account_type="savings",
            customer_id=100,
        )

        result = await account_service.create_account(account_data)

        assert result.account_number == "1234567890"
        assert result.balance == 1000.0
        assert result.account_type == "savings"
        mock_session.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_account_duplicate_number(self, account_service, mock_session):
        """Verifica que no se puede crear una cuenta con número duplicado."""
        account_service.repository.exists_by_account_number = AsyncMock(return_value=True)

        account_data = AccountCreate(
            account_number="1234567890",
            balance=1000.0,
            account_type="savings",
            customer_id=100,
        )

        with pytest.raises(AccountNumberAlreadyExistsException):
            await account_service.create_account(account_data)

    @pytest.mark.asyncio
    async def test_create_account_negative_balance(self, account_service, mock_session):
        """Verifica que no se puede crear una cuenta con saldo negativo."""
        account_data = AccountCreate(
            account_number="1234567890",
            balance=-100.0,
            account_type="savings",
            customer_id=100,
        )

        with pytest.raises(InvalidAccountDataException):
            await account_service.create_account(account_data)


class TestAccountServiceGet:
    """Tests para obtener cuentas."""

    @pytest.mark.asyncio
    async def test_get_account_success(self, account_service, sample_account, sample_account_response):
        """Verifica que se puede obtener una cuenta por ID."""
        account_service.repository.get_by_id = AsyncMock(return_value=sample_account)

        result = await account_service.get_account(1)

        assert result.id == 1
        assert result.account_number == "1234567890"

    @pytest.mark.asyncio
    async def test_get_account_not_found(self, account_service):
        """Verifica el comportamiento cuando la cuenta no existe."""
        account_service.repository.get_by_id = AsyncMock(return_value=None)

        with pytest.raises(AccountNotFoundException):
            await account_service.get_account(999)

    @pytest.mark.asyncio
    async def test_get_account_by_number_success(self, account_service, sample_account):
        """Verifica que se puede obtener una cuenta por número de cuenta."""
        account_service.repository.get_by_account_number = AsyncMock(return_value=sample_account)

        result = await account_service.get_account_by_number("1234567890")

        assert result.account_number == "1234567890"


class TestAccountServiceUpdate:
    """Tests para actualización de cuentas."""

    @pytest.mark.asyncio
    async def test_update_balance_success(self, account_service, sample_account):
        """Verifica que se puede actualizar el saldo de una cuenta."""
        account_service.repository.get_by_id = AsyncMock(return_value=sample_account)
        account_service.repository.update_balance = AsyncMock(return_value=sample_account)

        balance_update = AccountBalanceUpdate(balance=2000.0)
        result = await account_service.update_balance(1, balance_update)

        assert result.balance == 1000.0

    @pytest.mark.asyncio
    async def test_update_balance_negative(self, account_service, sample_account):
        """Verifica que no se puede establecer saldo negativo."""
        account_service.repository.get_by_id = AsyncMock(return_value=sample_account)

        balance_update = AccountBalanceUpdate(balance=-500.0)

        with pytest.raises(InvalidAccountDataException):
            await account_service.update_balance(1, balance_update)

    @pytest.mark.asyncio
    async def test_update_status_success(self, account_service, sample_account):
        """Verifica que se puede actualizar el estado de una cuenta."""
        account_service.repository.get_by_id = AsyncMock(return_value=sample_account)
        account_service.repository.update_status = AsyncMock(return_value=sample_account)

        status_update = AccountStatusUpdate(status="inactive")
        result = await account_service.update_status(1, status_update)

        assert result.status == "active"


class TestAccountServiceDelete:
    """Tests para eliminación de cuentas."""

    @pytest.mark.asyncio
    async def test_delete_account_success(self, account_service, sample_account):
        """Verifica que se puede eliminar una cuenta."""
        account_service.repository.get_by_id = AsyncMock(return_value=sample_account)
        account_service.repository.delete = AsyncMock(return_value=True)

        result = await account_service.delete_account(1)

        assert result is True
        mock_session := account_service.repository.session
        mock_session.commit.assert_called()

    @pytest.mark.asyncio
    async def test_delete_account_not_found(self, account_service):
        """Verifica que no se puede eliminar una cuenta inexistente."""
        account_service.repository.get_by_id = AsyncMock(return_value=None)

        with pytest.raises(AccountNotFoundException):
            await account_service.delete_account(999)


class TestAccountServiceList:
    """Tests para listado de cuentas."""

    @pytest.mark.asyncio
    async def test_list_accounts_default(self, account_service, sample_account):
        """Verifica el listado de cuentas sin filtros."""
        account_service.repository.get_all = AsyncMock(return_value=[sample_account])
        account_service.repository.count_all = AsyncMock(return_value=1)

        result = await account_service.list_accounts()

        assert result.total == 1
        assert len(result.accounts) == 1

    @pytest.mark.asyncio
    async def test_list_accounts_by_status(self, account_service, sample_account):
        """Verifica el listado de cuentas filtrado por estado."""
        account_service.repository.get_by_status = AsyncMock(return_value=[sample_account])
        account_service.repository.count_all = AsyncMock(return_value=1)

        result = await account_service.list_accounts(status=AccountStatus.ACTIVE)

        assert result.total == 1

    @pytest.mark.asyncio
    async def test_list_accounts_by_type(self, account_service, sample_account):
        """Verifica el listado de cuentas filtrado por tipo."""
        account_service.repository.get_by_type = AsyncMock(return_value=[sample_account])
        account_service.repository.count_all = AsyncMock(return_value=1)

        result = await account_service.list_accounts(account_type=AccountType.SAVINGS)

        assert result.total == 1


// === ARCHIVO: src/core/exceptions.py ===
from typing import Any, Optional


class BankingException(Exception):
    """Excepción base para errores del sistema bancario."""
    
    def __init__(self, message: str, code: Optional[str] = None):
        self.message = message
        self.code = code or "BANKING_ERROR"
        super().__init__(self.message)
    
    def to_dict(self) -> dict[str, Any]:
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "code": self.code,
        }


class CuentaNoEncontradaError(BankingException):
    """Excepción lanzada cuando una cuenta no existe."""
    
    def __init__(self, message: str = "Cuenta no encontrada"):
        super().__init__(message, "CUENTA_NO_ENCONTRADA")


class SaldoNegativoError(BankingException):
    """Excepción lanzada cuando se intenta operar con saldo negativo."""
    
    def __init__(self, message: str = "El saldo no puede ser negativo"):
        super().__init__(message, "SALDO_NEGATIVO")


class NumeroCuentaDuplicadoError(BankingException):
    """Excepción cuando el número de cuenta ya existe."""
    
    def __init__(self, message: str = "El número de cuenta ya existe"):
        super().__init__(message, "NUMERO_CUENTA_DUPLICADO")


class CuentaInactivaError(BankingException):
    """Excepción cuando se intenta operar con cuenta inactiva."""
    
    def __init__(self, message: str = "La cuenta está inactiva"):
        super().__init__(message, "CUENTA_INACTIVA")


class TipoCuentaInvalidoError(BankingException):
    """Excepción cuando el tipo de cuenta es inválido."""
    
    def __init__(self, message: str = "Tipo de cuenta inválido"):
        super().__init__(message, "TIPO_CUENTA_INVALIDO")


class AutenticacionError(BankingException):
    """Error de autenticación."""
    
    def __init__(self, message: str = "Error de autenticación"):
        super().__init__(message, "AUTENTICACION_ERROR")


class AutorizacionError(BankingException):
    """Error de autorización."""
    
    def __init__(self, message: str = "No autorizado"):
        super().__init__(message, "AUTORIZACION_ERROR")


class ValidacionError(BankingException):
    """Error de validación de datos."""
    
    def __init__(self, message: str = "Error de validación"):
        super().__init__(message, "VALIDACION_ERROR")


class ErrorInternoError(BankingException):
    """Error interno del servidor."""
    
    def __init__(self, message: str = "Error interno del servidor"):
        super().__init__(message, "ERROR_INTERNO")


class OperacionNoPermitidaError(BankingException):
    """Operación no permitida por reglas de negocio."""
    
    def __init__(self, message: str = "Operación no permitida"):
        super().__init__(message, "OPERACION_NO_PERMITIDA")


# Alias para compatibilidad con el código existente
AccountNotFoundException = CuentaNoEncontradaError
AccountNumberAlreadyExistsException = NumeroCuentaDuplicadoError
InvalidAccountDataException = ValidacionError

```
