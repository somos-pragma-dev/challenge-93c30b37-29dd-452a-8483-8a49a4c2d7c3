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