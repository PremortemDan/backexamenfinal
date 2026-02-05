from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from schemas.vehicle import VehicleCreate, VehicleUpdate, VehicleResponse, VehicleStats
from controllers.vehicle_controller import vehicle_controller
from controllers.user_controller import user_controller
from database.db import get_db

router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"]
)

@router.post("", response_model=VehicleResponse, status_code=201)
async def crear_vehiculo(
    vehiculo: VehicleCreate,
    db: Session = Depends(get_db),
    current_user = Depends(user_controller.get_current_user)
):
    """
    Crear un nuevo vehículo.
    
    Requiere autenticación.
    
    - **marca**: Marca del vehículo
    - **modelo**: Modelo del vehículo
    - **año**: Año de fabricación
    - **tipo**: Tipo de vehículo (sedán, SUV, etc.)
    - **kilometraje**: Kilometraje actual del vehículo
    """
    return vehicle_controller.create_vehicle(vehiculo, db)

@router.get("", response_model=List[VehicleResponse])
async def listar_vehiculos(
    tipo: Optional[str] = Query(None, description="Filtrar por tipo de vehículo"),
    db: Session = Depends(get_db),
    current_user = Depends(user_controller.get_current_user)
):
    """
    Listar todos los vehículos.
    
    Requiere autenticación.
    
    - **tipo** (opcional): Filtrar por tipo de vehículo
    """
    return vehicle_controller.get_all_vehicles(db, tipo=tipo)

@router.get("/promedio-km", response_model=VehicleStats)
async def promedio_kilometraje(
    db: Session = Depends(get_db),
    current_user = Depends(user_controller.get_current_user)
):
    """
    Obtener estadísticas de kilometraje.
    
    Requiere autenticación.
    
    Retorna el promedio de kilometraje y el total de vehículos.
    """
    return vehicle_controller.get_vehicle_stats(db)

@router.get("/{vehiculo_id}", response_model=VehicleResponse)
async def obtener_vehiculo(
    vehiculo_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(user_controller.get_current_user)
):
    """
    Obtener un vehículo por ID.
    
    Requiere autenticación.
    
    - **vehiculo_id**: ID del vehículo
    """
    return vehicle_controller.get_vehicle_by_id(vehiculo_id, db)

@router.put("/{vehiculo_id}", response_model=VehicleResponse)
async def actualizar_vehiculo(
    vehiculo_id: int,
    vehiculo: VehicleUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(user_controller.get_current_user)
):
    """
    Actualizar un vehículo existente.
    
    Requiere autenticación.
    
    - **vehiculo_id**: ID del vehículo a actualizar
    - **vehiculo**: Datos actualizados del vehículo
    """
    return vehicle_controller.update_vehicle(vehiculo_id, vehiculo, db)

@router.delete("/{vehiculo_id}")
async def eliminar_vehiculo(
    vehiculo_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(user_controller.get_current_user)
):
    """
    Eliminar un vehículo.
    
    Requiere autenticación.
    
    - **vehiculo_id**: ID del vehículo a eliminar
    """
    return vehicle_controller.delete_vehicle(vehiculo_id, db)
