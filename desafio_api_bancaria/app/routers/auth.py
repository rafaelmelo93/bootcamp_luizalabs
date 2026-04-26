from fastapi import APIRouter, status
from app.schemas import LoginData
from app.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(data: LoginData):
    """
    Realiza o login de um usuário e retorna um token JWT.
    (Simulação simplificada utilizando apenas o ID do usuário)
    """
    return create_access_token(data.user_id)
