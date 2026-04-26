# 💰 API Bancária - Gerenciamento de Contas e Transações

API REST desenvolvida com **FastAPI** para simular operações bancárias básicas, incluindo criação de contas, autenticação de usuários e gerenciamento de transações financeiras.

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de backend, como:

* Arquitetura em camadas
* Boas práticas com APIs REST
* Autenticação e segurança
* Manipulação de banco de dados com ORM
* Controle de migrações

---

## 🚀 Tecnologias utilizadas

* **Python 3**
* **FastAPI**
* **SQLAlchemy**
* **Alembic**
* **Poetry**
* **Pydantic**

---

## 📁 Estrutura do projeto

```id="dah7bt"
.
├── src/
│   ├── controllers/     # Intermediação entre rotas e regras de negócio
│   ├── services/        # Regras de negócio da aplicação
│   ├── models/          # Modelos do banco de dados (ORM)
│   ├── schemas/         # Validação de dados com Pydantic
│   ├── views/           # Definição das rotas da API
│   ├── security.py      # Autenticação e geração de tokens
│   ├── database.py      # Configuração do banco de dados
│   ├── config.py        # Configurações gerais
│   ├── exceptions.py    # Tratamento de erros
│   └── main.py          # Ponto de entrada da aplicação
│
├── migrations/          # Migrações do banco de dados (Alembic)
├── .env.example         # Variáveis de ambiente
├── pyproject.toml       # Dependências do projeto
└── alembic.ini          # Configuração do Alembic
```

---

## ⚙️ Como executar o projeto

### 1️⃣ Clonar o repositório

```bash id="b4lsbo"
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

---

### 2️⃣ Instalar dependências

```bash id="1dsohe"
poetry install
```

---

### 3️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` com base no `.env.example`:

```env id="jt1uxx"
DATABASE_URL=sqlite:///./database.db
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 4️⃣ Executar migrações

```bash id="btqc4j"
alembic upgrade head
```

---

### 5️⃣ Iniciar a aplicação

```bash id="s8gd3l"
poetry run uvicorn src.main:app --reload
```

---

## 🌐 Acessando a API

Após iniciar o servidor:

* Documentação interativa (Swagger):
  👉 http://localhost:8000/docs

* Documentação alternativa:
  👉 http://localhost:8000/redoc

---

## 🔑 Funcionalidades

### 👤 Conta

* Criar conta
* Listar contas
* Buscar conta por ID

### 🔐 Autenticação

* Login de usuário
* Geração de token JWT

### 💸 Transações

* Depósito
* Saque
* Transferência entre contas

---

## 📌 Exemplo de fluxo

1. Criar uma conta
2. Fazer login
3. Receber token JWT
4. Realizar operações financeiras autenticadas

---

## 🔒 Segurança

* Senhas protegidas com hash
* Autenticação via JWT
* Rotas protegidas por token

---

## 🧪 Melhorias futuras

* [ ] Testes automatizados (pytest)
* [ ] Dockerização do projeto
* [ ] Logs estruturados
* [ ] Rate limiting
* [ ] Deploy em nuvem

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais.
