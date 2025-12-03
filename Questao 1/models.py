from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional
from datetime import date

# Base para modelos SQLAlchemy
Base = declarative_base()

class Book(Base):
    """
    Modelo de dados para Livros no banco de dados SQLite.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author = Column(String, index=True, nullable=False)
    publication_date = Column(Date, nullable=False)
    summary = Column(String, nullable=True)

# Modelos Pydantic para validação de dados na API

class BookBase(BaseModel):
    title: str
    author: str
    publication_date: date
    summary: Optional[str] = None

class BookCreate(BookBase):
    """
    Schema para criação de um novo livro.
    """
    pass

class BookResponse(BookBase):
    """
    Schema para resposta de dados de um livro.
    """
    id: int

    class Config:
        from_attributes = True
