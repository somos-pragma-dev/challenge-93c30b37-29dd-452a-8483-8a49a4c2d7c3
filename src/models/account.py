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