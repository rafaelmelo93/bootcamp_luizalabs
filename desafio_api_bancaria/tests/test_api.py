import pytest

pytestmark = pytest.mark.asyncio

async def get_token(async_client):
    response = await async_client.post("/auth/login", json={"user_id": 1})
    assert response.status_code == 200
    token = response.json()["access_token"]
    return token

async def test_create_account(async_client):
    token = await get_token(async_client)
    headers = {"Authorization": f"Bearer {token}"}

    response = await async_client.post(
        "/accounts/",
        json={"user_id": 1},
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["balance"] == 0.0

async def test_create_transaction_deposit(async_client):
    token = await get_token(async_client)
    headers = {"Authorization": f"Bearer {token}"}

    # Criar conta primeiro
    acc_response = await async_client.post("/accounts/", json={"user_id": 1}, headers=headers)
    acc_id = acc_response.json()["id"]

    # Fazer depósito
    response = await async_client.post(
        "/transactions/",
        json={"account_id": acc_id, "type": "deposit", "amount": 150.0},
        headers=headers
    )
    assert response.status_code == 201
    data = response.json()
    assert data["amount"] == 150.0
    assert data["type"] == "deposit"

    # Checar saldo
    acc_check = await async_client.get(f"/accounts/{acc_id}", headers=headers)
    assert acc_check.json()["balance"] == 150.0

async def test_create_transaction_withdrawal(async_client):
    token = await get_token(async_client)
    headers = {"Authorization": f"Bearer {token}"}

    # Criar conta
    acc_response = await async_client.post("/accounts/", json={"user_id": 1}, headers=headers)
    acc_id = acc_response.json()["id"]

    # Fazer depósito de 100
    await async_client.post(
        "/transactions/",
        json={"account_id": acc_id, "type": "deposit", "amount": 100.0},
        headers=headers
    )

    # Fazer saque de 40
    response = await async_client.post(
        "/transactions/",
        json={"account_id": acc_id, "type": "withdrawal", "amount": 40.0},
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()["amount"] == 40.0

    # Checar saldo
    acc_check = await async_client.get(f"/accounts/{acc_id}", headers=headers)
    assert acc_check.json()["balance"] == 60.0

async def test_create_transaction_withdrawal_insufficient_funds(async_client):
    token = await get_token(async_client)
    headers = {"Authorization": f"Bearer {token}"}

    # Criar conta
    acc_response = await async_client.post("/accounts/", json={"user_id": 1}, headers=headers)
    acc_id = acc_response.json()["id"]

    # Tentar saque sem saldo
    response = await async_client.post(
        "/transactions/",
        json={"account_id": acc_id, "type": "withdrawal", "amount": 50.0},
        headers=headers
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Saldo insuficiente para o saque."

async def test_get_account_statement(async_client):
    token = await get_token(async_client)
    headers = {"Authorization": f"Bearer {token}"}

    # Criar conta
    acc_response = await async_client.post("/accounts/", json={"user_id": 1}, headers=headers)
    acc_id = acc_response.json()["id"]

    # Fazer algumas transações
    await async_client.post("/transactions/", json={"account_id": acc_id, "type": "deposit", "amount": 200.0}, headers=headers)
    await async_client.post("/transactions/", json={"account_id": acc_id, "type": "withdrawal", "amount": 50.0}, headers=headers)

    # Obter extrato
    response = await async_client.get(f"/transactions/{acc_id}/statement", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    # Estão em ordem decrescente, o primeiro é o saque
    assert data[0]["type"] == "withdrawal"
    assert data[1]["type"] == "deposit"
