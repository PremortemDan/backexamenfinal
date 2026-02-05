from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from routes.user_routes import router as user_router
from routes.vehicle_routes import router as vehicle_router

app = FastAPI(
    title="Sistema de Gestión de Vehículos",
    description="API RESTful para gestión de vehículos con autenticación JWT",
    version="2.0.0"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas principales
@app.get("/")
async def root():
    """Endpoint raíz de la API."""
    return {
        "message": "API de Gestión de Vehículos",
        "version": "2.0.0",
        "docs": "/docs"
    }

# Incluir routers
app.include_router(user_router)
app.include_router(vehicle_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
