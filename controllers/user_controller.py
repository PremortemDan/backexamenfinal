from typing import Optional
from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from core.security import get_password_hash, verify_password, create_access_token, decode_access_token, oauth2_scheme
from database.db import get_db
from schemas.user import UserCreate, UserResponse, Token
from models.user import User

class UserController:
    """Controlador para operaciones de usuario."""
    
    def register_user(self, user_data: UserCreate, db: Session) -> UserResponse:
        """Registrar un nuevo usuario."""
        # Verificar si el usuario ya existe
        existing_user = db.query(User).filter(
            (User.username == user_data.username) | (User.email == user_data.email)
        ).first()
        
        if existing_user:
            if existing_user.username == user_data.username:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El usuario ya existe"
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El email ya está registrado"
                )
        
        # Hash de contraseña
        hashed_password = get_password_hash(user_data.password)
        
        # Crear usuario
        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password
        )
        
        # Guardar en BD
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return UserResponse(username=user.username, email=user.email)
    
    def authenticate_user(self, username: str, password: str, db: Session) -> Optional[User]:
        """Autenticar usuario."""
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
    
    def login_user(self, username: str, password: str, db: Session) -> Token:
        """Login de usuario."""
        user = self.authenticate_user(username, password, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Usuario o contraseña incorrectos",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Crear token
        access_token = create_access_token(data={"sub": user.username})
        return Token(access_token=access_token, token_type="bearer")
    
    def get_current_user(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
        """Obtener usuario actual desde token."""
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudo validar las credenciales",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        try:
            payload = decode_access_token(token)
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except:
            raise credentials_exception
        
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise credentials_exception
        
        return user
    
    def get_user_by_username(self, username: str, db: Session) -> Optional[User]:
        """Obtener usuario por username."""
        return db.query(User).filter(User.username == username).first()

# Instancia global del controlador
user_controller = UserController()
