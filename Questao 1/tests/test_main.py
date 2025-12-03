from httpx import AsyncClient, ASGITransport
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os
import pytest

# Adiciona o diretório pai ao sys.path para importar o main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from models import Base
from routers.books import get_db

# Banco de dados de teste em memória
# Cria o banco de teste no diretório do projeto (Questao 1)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override da dependência get_db para usar o banco de teste
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Cria as tabelas no banco de teste
Base.metadata.create_all(bind=engine)

@pytest.mark.asyncio
async def test_create_book():
    """
    Teste de criação de livro.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post(
            "/books/",
            json={
                "title": "Test Book",
                "author": "Test Author",
                "publication_date": "2023-01-01",
                "summary": "A test book summary"
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test Book"
        assert "id" in data

@pytest.mark.asyncio
async def test_read_books():
    """
    Teste de leitura de livros.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Cria um livro primeiro
        await client.post(
            "/books/",
            json={
                "title": "Another Book",
                "author": "Another Author",
                "publication_date": "2023-02-01",
                "summary": "Summary"
            },
        )
        
        response = await client.get("/books/")
        assert response.status_code == 200
        data = response.json()
        assert len(data) > 0

@pytest.mark.asyncio
async def test_read_books_filter():
    """
    Teste de filtro por autor.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/books/?author=Test Author")
        assert response.status_code == 200
        data = response.json()
        # Verifica se pelo menos um livro retornado tem o autor correto
        assert any(book["author"] == "Test Author" for book in data)
