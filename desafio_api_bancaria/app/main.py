from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import database, metadata, engine
from app.routers import accounts, transactions, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria as tabelas se não existirem
    metadata.create_all(engine)
    # Conecta no banco assincronamente
    await database.connect()
    yield
    # Desconecta do banco
    await database.disconnect()

app = FastAPI(
    title="Desafio API Bancária",
    version="1.0.0",
    description="Uma API Bancária Assíncrona utilizando FastAPI com operações de depósitos e saques vinculadas a contas correntes.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
