from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse, Token
from controllers.user_controller import user_controller
from database.db import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Registrar un nuevo usuario.
    
    - **username**: Nombre de usuario único
    - **email**: Email del usuario
    - **password**: Contraseña del usuario
    """
    return user_controller.register_user(user, db)

@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Login para obtener token de acceso.
    
    - **username**: Nombre de usuario
    - **password**: Contraseña
    """
    return user_controller.login_user(form_data.username, form_data.password, db)

@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user = Depends(user_controller.get_current_user)):
    """
    Obtener información del usuario actual autenticado.
    
    Requiere token de autenticación válido.
    """
    return UserResponse(
        username=current_user.username,
        email=current_user.email
    )
