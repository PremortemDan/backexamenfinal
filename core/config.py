from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Configuración de seguridad
    SECRET_KEY: str = "tu_clave_secreta_super_segura_12345"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Configuración CORS (será parseado desde string separado por comas)
    CORS_ORIGINS: str = "*"
    
    @property
    def cors_origins_list(self) -> list:
        """Convertir string de CORS_ORIGINS a lista."""
        if self.CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]
    
    # Configuración de Base de Datos PostgreSQL
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/vehiculos_db"
    
    # Alternativa: construir URL desde componentes
    POSTGRES_USER: Optional[str] = "user"
    POSTGRES_PASSWORD: Optional[str] = "password"
    POSTGRES_HOST: Optional[str] = "localhost"
    POSTGRES_PORT: Optional[str] = "5432"
    POSTGRES_DB: Optional[str] = "vehiculos_db"
    
    @property
    def database_url(self) -> str:
        """Construir URL de base de datos desde componentes o usar DATABASE_URL directamente."""
        if self.DATABASE_URL and "postgresql" in self.DATABASE_URL:
            return self.DATABASE_URL
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
