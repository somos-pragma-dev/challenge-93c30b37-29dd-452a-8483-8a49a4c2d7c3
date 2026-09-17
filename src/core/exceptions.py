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