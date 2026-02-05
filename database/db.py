from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings

# Crear engine de SQLAlchemy
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # Verificar conexiones antes de usarlas
    echo=False  # Cambiar a True para debug SQL
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos ORM
Base = declarative_base()

def get_db():
    """
    Dependency para obtener sesión de base de datos.
    Se usa con Depends() en FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Inicializar base de datos creando todas las tablas.
    Solo para desarrollo. En producción usar Alembic.
    """
    # Importar todos los modelos para que Base los conozca
    from models.user import User
    from models.vehicle import Vehicle
    
    Base.metadata.create_all(bind=engine)
