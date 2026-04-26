# 💰 API de Gerenciamento de Contas e Transações

Este projeto é uma API backend para gerenciamento de contas e transações financeiras. Ele permite criar contas, autenticar usuários e registrar operações como depósitos, saques e transferências.

---

## 🚀 Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* Alembic (migrações)
* Poetry (gerenciamento de dependências)

---

## 📁 Estrutura do projeto

```
.
├── src/
│   ├── controllers/     # Lógica de controle das rotas
│   ├── services/        # Regras de negócio
│   ├── models/          # Modelos do banco de dados
│   ├── schemas/         # Validação de dados (Pydantic)
│   ├── views/           # Definição das rotas
│   ├── config.py        # Configurações da aplicação
│   ├── database.py      # Conexão com banco de dados
│   ├── security.py      # Autenticação e segurança
│   ├── exceptions.py    # Tratamento de erros
│   └── main.py          # Ponto de entrada da aplicação
│
├── migrations/          # Controle de versões do banco (Alembic)
├── .env.example         # Exemplo de variáveis de ambiente
├── pyproject.toml       # Dependências (Poetry)
└── alembic.ini          # Configuração do Alembic
```

---

## ⚙️ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```

### 2. Instalar dependências

```bash
poetry install
```

### 3. Configurar variáveis de ambiente

Copie o arquivo `.env.example` e renomeie para `.env`, ajustando conforme necessário.

---

### 4. Rodar as migrações

```bash
alembic upgrade head
```

---

### 5. Iniciar a aplicação

```bash
poetry run uvicorn src.main:app --reload
```

---

## 📌 Funcionalidades

* ✅ Criação de contas
* 🔐 Autenticação de usuários
* 💸 Registro de transações

  * Depósitos
  * Saques
  * Transferências
* 📊 Consulta de saldo e histórico

---

## 🔒 Segurança

* Autenticação baseada em tokens
* Validação de dados com schemas
* Separação de responsabilidades (controllers, services, models)

---

## 🧪 Possíveis melhorias

* Adicionar testes automatizados
* Implementar rate limiting
* Melhorar logs e monitoramento
* Documentação mais detalhada dos endpoints

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo e desenvolvimento.
