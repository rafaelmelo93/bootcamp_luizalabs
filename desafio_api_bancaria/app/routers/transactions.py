from fastapi import APIRouter, Depends, status
from typing import List

from app.schemas import TransactionCreate, TransactionOut
from app.services import TransactionService
from app.security import require_auth

router = APIRouter(prefix="/transactions", tags=["Transações"])
service = TransactionService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut, dependencies=[Depends(require_auth)])
async def create_transaction(transaction: TransactionCreate):
    """
    Cria uma nova transação (depósito ou saque).
    Requer autenticação.
    """
    return await service.create_transaction(transaction)

@router.get("/{account_id}/statement", response_model=List[TransactionOut], dependencies=[Depends(require_auth)])
async def get_account_statement(account_id: int):
    """
    Exibe o extrato de uma conta, mostrando todas as transações realizadas.
    Requer autenticação.
    """
    return await service.get_account_statement(account_id)
