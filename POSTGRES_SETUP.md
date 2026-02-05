# Guía de Migración a PostgreSQL

## 📋 Pasos para Conectar a PostgreSQL

### 1. Instalar PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**macOS:**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
Descarga e instala desde: https://www.postgresql.org/download/windows/

### 2. Crear Base de Datos

```bash
# Acceder a PostgreSQL
sudo -u postgres psql

# Crear usuario (si no existe)
CREATE USER usuario WITH PASSWORD 'contraseña';

# Crear base de datos
CREATE DATABASE vehiculos_db;

# Dar permisos al usuario
GRANT ALL PRIVILEGES ON DATABASE vehiculos_db TO usuario;

# Salir
\q
```

### 3. Configurar Variables de Entorno

Copia el archivo `.env.example` a `.env`:

```bash
cp .env.example .env
```

Edita `.env` con tus credenciales:

```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/vehiculos_db

# O usando componentes individuales:
POSTGRES_USER=usuario
POSTGRES_PASSWORD=contraseña
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=vehiculos_db
```

### 4. Instalar Dependencias

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 5. Ejecutar Migraciones

```bash
# Crear migración inicial
alembic revision --autogenerate -m "Initial migration"

# Aplicar migraciones
alembic upgrade head
```

### 6. Iniciar Servidor

```bash
# Opción 1
python main.py

# Opción 2
python run.py

# Opción 3
uvicorn main:app --reload
```

## 🔄 Comandos Útiles de Alembic

```bash
# Ver historial de migraciones
alembic history

# Ver migración actual
alembic current

# Crear nueva migración automática
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar todas las migraciones pendientes
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Revertir todas las migraciones
alembic downgrade base

# Ver SQL sin ejecutar
alembic upgrade head --sql
```

## 🧪 Verificar Conexión

Puedes verificar la conexión creando un script de prueba:

```python
from database.db import engine

try:
    with engine.connect() as conn:
        print("✅ Conexión exitosa a PostgreSQL!")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
```

## 🔍 Consultar Base de Datos

```bash
# Conectar a la base de datos
psql -U usuario -d vehiculos_db

# Ver tablas
\dt

# Ver estructura de tabla
\d users
\d vehicles

# Consultar datos
SELECT * FROM users;
SELECT * FROM vehicles;

# Salir
\q
```

## 📊 Estructura de Tablas

### Tabla `users`
```sql
id              SERIAL PRIMARY KEY
username        VARCHAR(50) UNIQUE NOT NULL
email           VARCHAR(100) UNIQUE NOT NULL
hashed_password VARCHAR(255) NOT NULL
```

### Tabla `vehicles`
```sql
id          SERIAL PRIMARY KEY
marca       VARCHAR(50) NOT NULL
modelo      VARCHAR(50) NOT NULL
año         INTEGER NOT NULL
tipo        VARCHAR(30) NOT NULL
kilometraje FLOAT NOT NULL
```

## 🐛 Solución de Problemas

### Error: "could not connect to server"
- Verifica que PostgreSQL esté corriendo: `sudo systemctl status postgresql`
- Inicia el servicio: `sudo systemctl start postgresql`

### Error: "password authentication failed"
- Verifica las credenciales en el archivo `.env`
- Resetea la contraseña del usuario en PostgreSQL

### Error: "database does not exist"
- Crea la base de datos manualmente (ver paso 2)

### Error: "relation does not exist"
- Ejecuta las migraciones: `alembic upgrade head`

## 🔒 Seguridad

- **NUNCA** subas el archivo `.env` al repositorio
- Usa contraseñas seguras en producción
- Cambia `SECRET_KEY` en el archivo `.env`
- Considera usar variables de entorno del sistema en producción
