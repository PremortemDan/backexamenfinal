from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from database.db import get_db
from schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse, VehicleStats
from models.vehicle import Vehicle

class VehicleController:
    """Controlador para operaciones de vehículos."""
    
    def create_vehicle(self, vehicle_data: VehicleCreate, db: Session) -> VehicleResponse:
        """Crear un nuevo vehículo."""
        # Crear vehículo
        vehicle = Vehicle(
            marca=vehicle_data.marca,
            modelo=vehicle_data.modelo,
            año=vehicle_data.año,
            tipo=vehicle_data.tipo,
            kilometraje=vehicle_data.kilometraje,
            imagen_url=vehicle_data.imagen_url
        )
        
        # Guardar en BD
        db.add(vehicle)
        db.commit()
        db.refresh(vehicle)
        
        return VehicleResponse(
            id=vehicle.id,
            marca=vehicle.marca,
            modelo=vehicle.modelo,
            año=vehicle.año,
            tipo=vehicle.tipo,
            kilometraje=vehicle.kilometraje,
            imagen_url=vehicle.imagen_url
        )
    
    def get_all_vehicles(self, db: Session, tipo: Optional[str] = None) -> List[VehicleResponse]:
        """Obtener todos los vehículos, opcionalmente filtrados por tipo."""
        query = db.query(Vehicle)
        
        # Filtrar por tipo si se proporciona
        if tipo:
            query = query.filter(Vehicle.tipo.ilike(f"%{tipo}%"))
        
        vehicles = query.all()
        
        return [VehicleResponse(
            id=v.id,
            marca=v.marca,
            modelo=v.modelo,
            año=v.año,
            tipo=v.tipo,
            kilometraje=v.kilometraje,
            imagen_url=v.imagen_url
        ) for v in vehicles]
    
    def get_vehicle_by_id(self, vehicle_id: int, db: Session) -> VehicleResponse:
        """Obtener un vehículo por ID."""
        vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if not vehicle:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehículo no encontrado"
            )
        return VehicleResponse(
            id=vehicle.id,
            marca=vehicle.marca,
            modelo=vehicle.modelo,
            año=vehicle.año,
            tipo=vehicle.tipo,
            kilometraje=vehicle.kilometraje,
            imagen_url=vehicle.imagen_url
        )
    
    def update_vehicle(self, vehicle_id: int, vehicle_data: VehicleUpdate, db: Session) -> VehicleResponse:
        """Actualizar un vehículo existente."""
        vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if not vehicle:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehículo no encontrado"
            )
        
        # Actualizar campos
        vehicle.marca = vehicle_data.marca
        vehicle.modelo = vehicle_data.modelo
        vehicle.año = vehicle_data.año
        vehicle.tipo = vehicle_data.tipo
        vehicle.kilometraje = vehicle_data.kilometraje
        vehicle.imagen_url = vehicle_data.imagen_url
        
        db.commit()
        db.refresh(vehicle)
        
        return VehicleResponse(
            id=vehicle.id,
            marca=vehicle.marca,
            modelo=vehicle.modelo,
            año=vehicle.año,
            tipo=vehicle.tipo,
            kilometraje=vehicle.kilometraje,
            imagen_url=vehicle.imagen_url
        )
    
    def delete_vehicle(self, vehicle_id: int, db: Session) -> dict:
        """Eliminar un vehículo."""
        vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if not vehicle:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vehículo no encontrado"
            )
        
        db.delete(vehicle)
        db.commit()
        
        return {"message": "Vehículo eliminado correctamente"}
    
    def get_vehicle_stats(self, db: Session) -> VehicleStats:
        """Obtener estadísticas de vehículos."""
        # Contar total de vehículos
        total = db.query(Vehicle).count()
        
        if total == 0:
            return VehicleStats(promedio_kilometraje=0.0, total_vehiculos=0)
        
        # Calcular promedio de kilometraje
        avg_km = db.query(func.avg(Vehicle.kilometraje)).scalar()
        
        return VehicleStats(
            promedio_kilometraje=round(float(avg_km), 2),
            total_vehiculos=total
        )

# Instancia global del controlador
vehicle_controller = VehicleController()
