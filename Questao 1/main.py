from fastapi import FastAPI

app = FastAPI(
    title="Library API",
    description="API para gerenciamento de livros em uma biblioteca virtual.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """
    Endpoint raiz para verificar se a API está online.
    """
    return {"message": "Bem-vindo à Library API!"}
