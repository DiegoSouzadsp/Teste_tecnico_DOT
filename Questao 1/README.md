# Projeto 1: API de Biblioteca (FastAPI)

Este projeto implementa uma API RESTful para gerenciamento de livros em uma biblioteca virtual, conforme solicitado na Questão 1 da avaliação.

## Tecnologias Utilizadas
- **Linguagem**: Python 3.10+
- **Framework Web**: FastAPI
- **Banco de Dados**: SQLite (via SQLAlchemy)
- **Validação de Dados**: Pydantic
- **Testes**: Pytest

## Estrutura do Projeto
- `main.py`: Ponto de entrada da aplicação e configuração do FastAPI.
- `models.py`: Definição dos modelos de banco de dados e schemas Pydantic.
- `database.py`: Configuração da conexão com o banco de dados SQLite.
- `crud.py`: Camada de acesso a dados (Create, Read).
- `routers/books.py`: Definição dos endpoints da API.
- `tests/`: Suíte de testes unitários.

## Como Executar

### 1. Instalar Dependências
Certifique-se de estar na raiz do projeto ou dentro da pasta `Questao 1`.
```bash
pip install -r requirements.txt
```

### 2. Executar a API
Para iniciar o servidor de desenvolvimento:
```bash
# Estando dentro da pasta 'Questao 1'
uvicorn main:app --reload
```
A API estará acessível em `http://127.0.0.1:8000`.

### 3. Acessar a Documentação (Swagger UI)
O FastAPI gera automaticamente a documentação interativa. Acesse:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## Endpoints Disponíveis

### `POST /books/`
Cadastra um novo livro.
- **Body**:
  ```json
  {
    "title": "Título do Livro",
    "author": "Nome do Autor",
    "publication_date": "2023-10-27",
    "summary": "Breve resumo..."
  }
  ```
- **Respostas de Erro**:
  - `400 Bad Request`: Se tentar cadastrar um livro duplicado (mesmo título e autor).
  - `422 Validation Error`: Se campos obrigatórios estiverem vazios ou com formato inválido.

### `GET /books/`
Lista os livros cadastrados. Suporta filtros e paginação:
- `?title=termo`: Filtra livros cujo título contém "termo".
- `?author=nome`: Filtra livros cujo autor contém "nome".
- `?skip=0`: Pula os N primeiros registros (padrão 0).
- `?limit=100`: Limita o número de registros retornados (padrão 100).

## Tratamento de Erros e Boas Práticas (Senior Level)
- **Validação de Duplicidade**: Impede o cadastro de livros idênticos para manter a integridade dos dados.
- **Paginação**: Implementada no endpoint de listagem para garantir performance e escalabilidade.
- **Validação de Entrada**: Uso de Pydantic para garantir que campos como título e autor não sejam vazios.
- **Testes Isolados**: Uso de fixtures para limpar o banco de dados entre os testes, garantindo confiabilidade.

## Como Rodar os Testes
Para executar os testes unitários automatizados:
```bash
# A partir da raiz do repositório (d:\Projetos\DOTGROUP)
python -m pytest "Questao 1/tests"
```
Ou, se estiver dentro da pasta `Questao 1`:
```bash
pytest tests
```
