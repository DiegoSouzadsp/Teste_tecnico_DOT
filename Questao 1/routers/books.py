from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

# Importações relativas precisam de cuidado dependendo de como o app é executado.
# Como vamos rodar uvicorn main:app de dentro de Questao 1, imports devem ser relativos ao root do projeto ou absolutos.
# Usando imports absolutos baseados no sys.path ou relativos se estivermos dentro do pacote.
# Melhor abordagem para FastAPI simples: imports do mesmo diretório pai.

from .. import crud, models, database

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

# Dependência para obter a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=models.BookResponse)
def create_book(book: models.BookCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo livro na biblioteca.
    
    - **title**: Título do livro
    - **author**: Autor do livro
    - **publication_date**: Data de publicação (YYYY-MM-DD)
    - **summary**: Resumo do livro (opcional)
    """
    return crud.create_book(db=db, book=book)
