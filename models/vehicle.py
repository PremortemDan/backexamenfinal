from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Vehicle(Base):
    """Modelo ORM para Vehículo."""
    __tablename__ = "vehicles"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    año = Column(Integer, nullable=False)
    tipo = Column(String(30), nullable=False, index=True)
    kilometraje = Column(Float, nullable=False)
    imagen_url = Column(String(500), nullable=True)
    
    # Si quisieras agregar ownership:
    # owner_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="vehicles")
