import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
import sqlalchemy as sa
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import metadata, database
from app.config import settings

# Ajustar para banco em memória nos testes
settings.database_url = "sqlite+aiosqlite:///:memory:"

@pytest_asyncio.fixture(autouse=True)
async def setup_db():
    engine = sa.create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    metadata.create_all(engine)
    
    # Precisamos usar a mesma URL em memória assíncrona
    await database.connect()
    
    yield
    
    await database.disconnect()
    metadata.drop_all(engine)

@pytest_asyncio.fixture
async def async_client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client
