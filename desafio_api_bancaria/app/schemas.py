from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from app.models import TransactionType

class AccountCreate(BaseModel):
    user_id: int = Field(..., gt=0, description="O ID do usuário titular da conta")

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: datetime

class TransactionCreate(BaseModel):
    account_id: int = Field(..., gt=0, description="O ID da conta para a transação")
    type: TransactionType = Field(..., description="Tipo da transação: 'deposit' ou 'withdrawal'")
    amount: float = Field(..., gt=0, description="Valor da transação, deve ser positivo")

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("O valor deve ser positivo")
        return v

class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: float
    timestamp: datetime

class LoginData(BaseModel):
    user_id: int
