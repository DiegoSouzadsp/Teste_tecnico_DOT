from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite
# Garante que o DB seja criado no mesmo diretório deste arquivo
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Permite configuração via variável de ambiente, com default para SQLite local
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'library.db')}")

# Criação do engine do SQLAlchemy
# connect_args={"check_same_thread": False} é necessário apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sessão local para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
