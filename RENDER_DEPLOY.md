# Render Deployment

## 🚀 Configuración para Render

### ⚠️ IMPORTANTE: Versión de Python

Este proyecto requiere **Python 3.11.9** debido a la compatibilidad de dependencias.

### Opción 1: Blueprint con render.yaml (Recomendado)

El archivo `render.yaml` está configurado. Solo necesitas:

1. **Crear nuevo Blueprint en Render**
   - Ve a Dashboard → New → Blueprint
   - Conecta tu repositorio de GitHub
   - Render detectará automáticamente `render.yaml`

2. **Configura Variables de Entorno** (en el dashboard):
   ```env
   DATABASE_URL=postgresql://usuario:password@host/database
   SECRET_KEY=tu_clave_secreta_muy_segura_aqui
   CORS_ORIGINS=*
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=300
   ```

3. **Deploy** - Click "Apply" y listo

---

### Opción 2: Configuración Manual

Si prefieres configurar manualmente:

### Build Command
```bash
pip install --upgrade pip && pip install -r requirements.txt
```

### Start Command
```bash
sh start.sh
```

**O si prefieres más simple:**
```bash
python create_tables.py && alembic stamp head && uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Variables de Entorno en Render

**⚠️ CRÍTICO: Añade estas primero:**

```env
PYTHON_VERSION=3.11.9
PIP_NO_CACHE_DIR=1
```

**Luego añade las variables de tu aplicación:**

```env
DATABASE_URL=postgresql://usuario:password@host/database
SECRET_KEY=tu_clave_secreta_muy_segura_aqui
CORS_ORIGINS=*
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=300
```

**Nota:** `DATABASE_URL` se obtiene automáticamente de tu base de datos PostgreSQL en Render.

## 📝 Pasos para Desplegar

1. **Crear nuevo Web Service en Render**
   - Conecta tu repositorio de GitHub
   - Selecciona el directorio `backend`

2. **Configurar Build & Deploy**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `sh start.sh` o el comando largo arriba

3. **Variables de Entorno**
   - Agrega todas las variables listadas arriba
   - `DATABASE_URL` se configura automáticamente si conectaste una DB de Render

4. **Deploy**
   - Click en "Create Web Service"
   - Render automáticamente construirá y desplegará tu app

## 🔧 Comandos Útiles

### Ejecutar migraciones manualmente
```bash
alembic upgrade head
```

### Crear nueva migración
```bash
alembic revision --autogenerate -m "descripción"
```

### Verificar conexión a base de datos
```bash
python -c "from database.db import engine; print('Conectado:', engine.url)"
```

## 🌐 URL de Producción

Tu API estará disponible en: `https://tu-app.onrender.com`

Documentación automática:
- Swagger UI: `https://tu-app.onrender.com/docs`
- ReDoc: `https://tu-app.onrender.com/redoc`
