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