from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class VehicleBase(BaseModel):
    """Schema base para vehículo."""
    marca: str = Field(..., description="Marca del vehículo")
    modelo: str = Field(..., description="Modelo del vehículo")
    año: int = Field(..., gt=1900, lt=2100, description="Año de fabricación")
    tipo: str = Field(..., description="Tipo de vehículo (sedán, SUV, etc.)")
    kilometraje: float = Field(..., ge=0, description="Kilometraje del vehículo")
    imagen_url: Optional[str] = Field(None, description="URL de la imagen del vehículo")

class VehicleCreate(VehicleBase):
    """Schema para crear vehículo."""
    pass

class VehicleUpdate(VehicleBase):
    """Schema para actualizar vehículo."""
    pass

class VehicleResponse(VehicleBase):
    """Schema de respuesta para vehículo."""
    id: int = Field(..., description="ID único del vehículo")
    
    class Config:
        from_attributes = True

class VehicleStats(BaseModel):
    """Schema para estadísticas de vehículos."""
    promedio_kilometraje: float = Field(..., description="Promedio de kilometraje")
    total_vehiculos: int = Field(..., description="Total de vehículos")
