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