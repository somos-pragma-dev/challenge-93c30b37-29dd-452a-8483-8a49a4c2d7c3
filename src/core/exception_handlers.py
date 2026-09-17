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