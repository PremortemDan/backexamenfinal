# Backend - Sistema de Gestión de Vehículos

API RESTful modular con FastAPI para la gestión de vehículos con autenticación JWT.

## 📁 Estructura del Proyecto

```
backend/
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── core/                   # Configuración central
│   ├── __init__.py
│   ├── config.py          # Configuración de la aplicación
│   └── security.py        # Utilidades de seguridad (JWT, hashing)
├── database/              # Gestión de base de datos
│   ├── __init__.py
│   └── db.py             # Base de datos en memoria
├── models/                # Modelos de datos
│   ├── __init__.py
│   ├── user.py           # Modelo de usuario
│   └── vehicle.py        # Modelo de vehículo
├── schemas/               # Esquemas Pydantic (validación)
│   ├── __init__.py
│   ├── user.py           # Schemas de usuario
│   └── vehicle.py        # Schemas de vehículo
├── controllers/           # Lógica de negocio
│   ├── __init__.py
│   ├── user_controller.py      # Controlador de usuarios
│   └── vehicle_controller.py   # Controlador de vehículos
└── routes/                # Endpoints de la API
    ├── __init__.py
    ├── user_routes.py     # Rutas de autenticación
    └── vehicle_routes.py  # Rutas de vehículos
```

## 🏗️ Arquitectura

### **Separación de Responsabilidades**

1. **`core/`** - Configuración y utilidades compartidas
   - `config.py`: Variables de configuración (SECRET_KEY, CORS, etc.)
   - `security.py`: Funciones de seguridad (hashing de contraseñas, JWT)

2. **`database/`** - Capa de acceso a datos
   - `db.py`: Gestión de la base de datos en memoria

3. **`models/`** - Modelos de dominio
   - `user.py`: Clase User con métodos to_dict/from_dict
   - `vehicle.py`: Clase Vehicle con métodos to_dict/from_dict

4. **`schemas/`** - Validación de datos con Pydantic
   - `user.py`: UserCreate, UserResponse, Token
   - `vehicle.py`: VehicleCreate, VehicleUpdate, VehicleResponse, VehicleStats

5. **`controllers/`** - Lógica de negocio
   - `user_controller.py`: Registro, login, autenticación
   - `vehicle_controller.py`: CRUD de vehículos, estadísticas

6. **`routes/`** - Definición de endpoints
   - `user_routes.py`: `/auth/register`, `/auth/token`, `/auth/me`
   - `vehicle_routes.py`: CRUD en `/vehiculos`

## 🚀 Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python main.py
# o
uvicorn main:app --reload
```

## 📡 Endpoints

### **Autenticación** (`/auth`)

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Registrar nuevo usuario | No |
| POST | `/auth/token` | Login (obtener token JWT) | No |
| GET | `/auth/me` | Obtener usuario actual | Sí |

### **Vehículos** (`/vehiculos`)

| Método | Endpoint | Descripción | Auth |
|--------|----------|-------------|------|
| POST | `/vehiculos` | Crear vehículo | Sí |
| GET | `/vehiculos` | Listar vehículos (filtrar por tipo) | Sí |
| GET | `/vehiculos/promedio-km` | Estadísticas de kilometraje | Sí |
| GET | `/vehiculos/{id}` | Obtener vehículo por ID | Sí |
| PUT | `/vehiculos/{id}` | Actualizar vehículo | Sí |
| DELETE | `/vehiculos/{id}` | Eliminar vehículo | Sí |

## 🔐 Autenticación

La API usa **JWT (JSON Web Tokens)** para autenticación:

1. Registrarse con `/auth/register`
2. Hacer login con `/auth/token` para obtener un token
3. Incluir el token en el header: `Authorization: Bearer <token>`

## 📝 Documentación Interactiva

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔄 Migración desde versión anterior

### Cambios en las rutas:

| Antigua | Nueva |
|---------|-------|
| `/register` | `/auth/register` |
| `/token` | `/auth/token` |
| `/users/me` | `/auth/me` |
| `/vehiculos` | `/vehiculos` (sin cambios) |

### Ventajas de la nueva estructura:

✅ **Modularidad**: Código organizado por responsabilidades  
✅ **Mantenibilidad**: Fácil de encontrar y modificar funcionalidades  
✅ **Escalabilidad**: Simple añadir nuevas entidades  
✅ **Testabilidad**: Controllers y rutas separados facilitan testing  
✅ **Reutilización**: Lógica de negocio independiente de endpoints
