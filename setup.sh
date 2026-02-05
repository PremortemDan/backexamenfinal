#!/bin/bash

# Script de configuración inicial del backend

echo "🚀 Configurando Backend - Sistema de Gestión de Vehículos"
echo ""

# 1. Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv

# 2. Activar entorno virtual
echo "✅ Activando entorno virtual..."
source venv/bin/activate

# 3. Actualizar pip
echo "📥 Actualizando pip..."
pip install --upgrade pip

# 4. Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# 5. Configurar variables de entorno
if [ ! -f .env ]; then
    echo "⚙️  Creando archivo .env desde .env.example..."
    cp .env.example .env
    echo "⚠️  IMPORTANTE: Edita el archivo .env con tus credenciales de PostgreSQL"
else
    echo "✅ Archivo .env ya existe"
fi

echo ""
echo "✅ Configuración completada!"
echo ""
echo "📝 Próximos pasos:"
echo "   1. Edita el archivo .env con tus credenciales de PostgreSQL"
echo "   2. Crea la base de datos en PostgreSQL: CREATE DATABASE vehiculos_db;"
echo "   3. Ejecuta las migraciones: alembic upgrade head"
echo "   4. Inicia el servidor: python main.py o python run.py"
echo ""
