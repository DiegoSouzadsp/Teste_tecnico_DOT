from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"

# Criação do engine do SQLAlchemy
# connect_args={"check_same_thread": False} é necessário apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Sessão local para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
