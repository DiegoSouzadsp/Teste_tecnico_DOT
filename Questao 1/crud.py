from sqlalchemy.orm import Session
from . import models, schemas

# Nota: schemas será importado de models se estiverem no mesmo arquivo ou separado.
# No meu models.py eu coloquei os schemas Pydantic também.
# Vou ajustar o import para refletir isso.
from .models import Book, BookCreate

def get_book(db: Session, book_id: int):
    """
    Busca um livro pelo ID.
    """
    return db.query(Book).filter(Book.id == book_id).first()

def get_books(db: Session, title: str = None, author: str = None):
    """
    Busca livros com filtros opcionais de título e autor.
    """
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    return query.all()

def create_book(db: Session, book: BookCreate):
    """
    Cria um novo livro no banco de dados.
    """
    db_book = Book(
        title=book.title,
        author=book.author,
        publication_date=book.publication_date,
        summary=book.summary
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
