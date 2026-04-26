import databases
import sqlalchemy as sa

from app.config import settings

database = databases.Database(settings.database_url)
metadata = sa.MetaData()

if settings.environment == "production":
    engine = sa.create_engine(settings.database_url)
else:
    # Ajuste para o sqlite aceitar multithreading
    engine = sa.create_engine(
        settings.database_url.replace("+aiosqlite", ""), 
        connect_args={"check_same_thread": False}
    )
