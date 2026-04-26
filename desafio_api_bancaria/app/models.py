from enum import Enum
import sqlalchemy as sa
from app.database import metadata

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"

accounts = sa.Table(
    "accounts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.Integer, nullable=False, index=True),
    sa.Column("balance", sa.Numeric(10, 2), nullable=False, default=0),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)

transactions = sa.Table(
    "transactions",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("account_id", sa.Integer, sa.ForeignKey("accounts.id"), nullable=False),
    sa.Column("type", sa.Enum(TransactionType, name="transaction_types"), nullable=False),
    sa.Column("amount", sa.Numeric(10, 2), nullable=False),
    sa.Column("timestamp", sa.TIMESTAMP(timezone=True), default=sa.func.now()),
)
