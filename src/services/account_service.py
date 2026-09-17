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