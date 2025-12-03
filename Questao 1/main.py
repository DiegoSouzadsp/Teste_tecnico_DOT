from fastapi import FastAPI
import models, database
from routers import books

# Cria as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Library API",
    description="API para gerenciamento de livros em uma biblioteca virtual.",
    version="1.0.0"
)

app.include_router(books.router)

@app.get("/")
def read_root():
    """
    Endpoint raiz para verificar se a API está online.
    """
    return {"message": "Bem-vindo à Library API!"}
