# Backend - FastAPI + PostgreSQL

API REST modular para el sistema de gestión de vehículos con autenticación JWT y base de datos PostgreSQL.

## 🚀 Inicio Rápido

### Opción 1: Script Automático (Linux/Mac)

```bash
chmod +x setup.sh
./setup.sh
```

### Opción 2: Manual

```bash
# 1. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales de PostgreSQL

# 4. Crear base de datos PostgreSQL
sudo -u postgres psql
CREATE DATABASE vehiculos_db;
CREATE USER usuario WITH PASSWORD 'contraseña';
GRANT ALL PRIVILEGES ON DATABASE vehiculos_db TO usuario;
\q

# 5. Ejecutar migraciones
alembic upgrade head

# 6. Iniciar servidor
python main.py
```

## 📚 Documentación

- **[ARQUITECTURA.md](./ARQUITECTURA.md)** - Estructura del proyecto
- **[POSTGRES_SETUP.md](./POSTGRES_SETUP.md)** - Guía completa de PostgreSQL

## 🗄️ Base de Datos

Este proyecto usa **PostgreSQL** con **SQLAlchemy** como ORM y **Alembic** para migraciones.

### Configuración Rápida

1. Crea la base de datos:
```bash
createdb vehiculos_db
```

2. Configura `.env`:
```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/vehiculos_db
```

3. Ejecuta migraciones:
```bash
alembic upgrade head
```

## 🏗️ Estructura

```
backend/
├── main.py              # Punto de entrada
├── run.py              # Script de inicio
├── requirements.txt    # Dependencias
├── .env.example        # Template de variables de entorno
├── alembic.ini         # Configuración de migraciones
├── core/               # Configuración
│   ├── config.py      # Settings
│   └── security.py    # JWT, hashing
├── database/          # Base de datos
│   └── db.py         # SQLAlchemy setup
├── models/            # Modelos ORM
│   ├── user.py
│   └── vehicle.py
├── schemas/           # Validación Pydantic
│   ├── user.py
│   └── vehicle.py
├── controllers/       # Lógica de negocio
│   ├── user_controller.py
│   └── vehicle_controller.py
├── routes/            # Endpoints API
│   ├── user_routes.py
│   └── vehicle_routes.py
└── alembic/           # Migraciones
    └── versions/
```

## 🔌 Endpoints

### Autenticación (`/auth`)
- `POST /auth/register` - Registrar usuario
- `POST /auth/token` - Login (obtener JWT)
- `GET /auth/me` - Info usuario actual

### Vehículos (`/vehiculos`)
- `POST /vehiculos` - Crear vehículo
- `GET /vehiculos` - Listar vehículos (filtro opcional por tipo)
- `GET /vehiculos/promedio-km` - Estadísticas
- `GET /vehiculos/{id}` - Obtener por ID
- `PUT /vehiculos/{id}` - Actualizar
- `DELETE /vehiculos/{id}` - Eliminar

## 📖 Documentación API

FastAPI genera documentación interactiva automáticamente:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Autenticación

1. Registrarse: `POST /auth/register`
2. Login: `POST /auth/token`
3. Usar token en header: `Authorization: Bearer <token>`

## 🧪 Desarrollo

```bash
# Crear nueva migración
alembic revision --autogenerate -m "Descripción"

# Aplicar migraciones
alembic upgrade head

# Revertir migración
alembic downgrade -1

# Ver historial
alembic history
```

## 🛠️ Tecnologías

- **FastAPI** - Framework web moderno
- **PostgreSQL** - Base de datos relacional
- **SQLAlchemy** - ORM
- **Alembic** - Migraciones de BD
- **Pydantic** - Validación de datos
- **JWT** - Autenticación
- **Passlib** - Hashing de contraseñas

## 📝 Notas

- El puerto por defecto es **8000**
- La base de datos debe crearse manualmente
- Las migraciones se aplican automáticamente al iniciar (opcional)
- Todos los endpoints de vehículos requieren autenticación
