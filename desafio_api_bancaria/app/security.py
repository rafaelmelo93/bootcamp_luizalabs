import time
from uuid import uuid4
import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from typing import Annotated
from pydantic import BaseModel

from app.config import settings

class AccessToken(BaseModel):
    iss: str
    sub: int
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str

class JWTToken(BaseModel):
    access_token: AccessToken

def create_access_token(user_id: int) -> dict:
    now = time.time()
    payload = {
        "iss": "api-bancaria.com",
        "sub": user_id,
        "aud": "api-bancaria",
        "exp": now + (60 * 60),  # 1 hour
        "iat": now,
        "nbf": now,
        "jti": uuid4().hex,
    }
    token = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)
    return {"access_token": token}

async def decode_token(token: str) -> JWTToken | None:
    try:
        decoded_token = jwt.decode(token, settings.secret_key, audience="api-bancaria", algorithms=[settings.algorithm])
        _token = JWTToken.model_validate({"access_token": decoded_token})
        return _token if _token.access_token.exp >= time.time() else None
    except Exception:
        return None

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTToken:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")

        if credentials:
            if scheme.lower() != "bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Esquema de autenticação inválido. Use Bearer.",
                )

            payload = await decode_token(credentials)
            if not payload:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token inválido ou expirado.",
                )
            return payload
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Código de autorização inválido.",
            )

async def get_current_user(token: Annotated[JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
    return {"user_id": token.access_token.sub}

def require_auth(current_user: Annotated[dict[str, int], Depends(get_current_user)]):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso negado.")
    return current_user
