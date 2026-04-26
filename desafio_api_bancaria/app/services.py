from databases.interfaces import Record
from fastapi import HTTPException, status
from app.database import database
from app.models import accounts, transactions, TransactionType
from app.schemas import AccountCreate, TransactionCreate

class AccountService:
    async def create_account(self, data: AccountCreate) -> Record:
        query = accounts.insert().values(user_id=data.user_id, balance=0.0)
        account_id = await database.execute(query)
        select_query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(select_query)

    async def get_account(self, account_id: int) -> Record:
        query = accounts.select().where(accounts.c.id == account_id)
        account = await database.fetch_one(query)
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada.")
        return account

    async def list_accounts(self) -> list[Record]:
        query = accounts.select()
        return await database.fetch_all(query)

class TransactionService:
    @database.transaction()
    async def create_transaction(self, data: TransactionCreate) -> Record:
        # Busca a conta
        account_query = accounts.select().where(accounts.c.id == data.account_id)
        account = await database.fetch_one(account_query)
        
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada.")
            
        current_balance = float(account.balance)
        
        # Validar e calcular o saldo
        if data.type == TransactionType.WITHDRAWAL:
            if current_balance < data.amount:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="Saldo insuficiente para o saque."
                )
            new_balance = current_balance - data.amount
        else: # DEPOSIT
            new_balance = current_balance + data.amount
            
        # Registrar a transação
        transaction_query = transactions.insert().values(
            account_id=data.account_id,
            type=data.type,
            amount=data.amount,
        )
        transaction_id = await database.execute(transaction_query)
        
        # Atualizar o saldo da conta
        update_account_query = accounts.update().where(accounts.c.id == data.account_id).values(balance=new_balance)
        await database.execute(update_account_query)
        
        # Retornar a transação criada
        select_tx_query = transactions.select().where(transactions.c.id == transaction_id)
        return await database.fetch_one(select_tx_query)

    async def get_account_statement(self, account_id: int) -> list[Record]:
        # Valida se a conta existe
        account_query = accounts.select().where(accounts.c.id == account_id)
        account = await database.fetch_one(account_query)
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada.")

        query = transactions.select().where(transactions.c.account_id == account_id).order_by(transactions.c.timestamp.desc())
        return await database.fetch_all(query)
