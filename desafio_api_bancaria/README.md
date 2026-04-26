# Desafio: API Bancária Assíncrona com FastAPI

Neste desafio, foi projetado e implementada uma API RESTful assíncrona usando FastAPI para gerenciar operações bancárias de depósitos e saques, vinculadas a contas correntes.

O projeto utiliza as seguintes tecnologias:
- **FastAPI**: Framework web moderno, rápido (alta performance), para construção de APIs com Python.
- **SQLAlchemy (Core)**: Toolkit SQL e ORM para mapeamento das tabelas.
- **Databases (aiosqlite)**: Suporte assíncrono para o banco de dados SQLite.
- **Pydantic**: Para validação de dados e conversão (schemas).
- **PyJWT**: Para implementação de autenticação usando JSON Web Tokens (JWT).
- **Pytest**: Framework para implementação de testes.

## Funcionalidades

1. **Autenticação com JWT**
   - Rota para realizar "login" e gerar um token de acesso que permite o consumo de rotas seguras.
2. **Contas Correntes**
   - Criar conta corrente.
   - Listar todas as contas correntes.
   - Obter detalhes de uma conta específica.
3. **Transações Bancárias**
   - Realizar depósito (aumenta o saldo).
   - Realizar saque (diminui o saldo). Valida se há saldo suficiente para o saque, assim como impede valores negativos de transação via validação do Pydantic.
4. **Extrato Bancário**
   - Obter o extrato detalhado de uma conta, mostrando todas as transações realizadas (depósitos e saques), ordenado das transações mais recentes para as mais antigas.

## Como Executar

### 1. Criar um Ambiente Virtual e Ativar

```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a Aplicação

```bash
uvicorn app.main:app --reload
```

A documentação interativa da API (Swagger) estará disponível em:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Como Rodar os Testes

Para garantir o funcionamento das rotas assíncronas, você pode rodar os testes utilizando o Pytest:

```bash
pytest tests/
```
