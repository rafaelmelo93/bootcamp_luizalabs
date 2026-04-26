from fastapi import APIRouter, Depends, status
from typing import List

from app.schemas import AccountCreate, AccountOut
from app.services import AccountService
from app.security import require_auth

router = APIRouter(prefix="/accounts", tags=["Contas"])
service = AccountService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut, dependencies=[Depends(require_auth)])
async def create_account(account: AccountCreate):
    """
    Cria uma nova conta corrente.
    Requer autenticação.
    """
    return await service.create_account(account)

@router.get("/", response_model=List[AccountOut], dependencies=[Depends(require_auth)])
async def list_accounts():
    """
    Lista todas as contas correntes.
    Requer autenticação.
    """
    return await service.list_accounts()

@router.get("/{account_id}", response_model=AccountOut, dependencies=[Depends(require_auth)])
async def get_account(account_id: int):
    """
    Obtém detalhes de uma conta específica.
    Requer autenticação.
    """
    return await service.get_account(account_id)
