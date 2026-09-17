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