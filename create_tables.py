#!/usr/bin/env python3
"""
Script para crear las tablas en la base de datos remota
"""
import sys
from database.db import Base, engine
from models.user import User
from models.vehicle import Vehicle

def create_tables():
    """Crear todas las tablas en la base de datos."""
    print("Creando tablas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas exitosamente!")

if __name__ == "__main__":
    try:
        create_tables()
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")
        sys.exit(1)
