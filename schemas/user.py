from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """Schema base para usuario."""
    username: str
    email: EmailStr

class UserCreate(UserBase):
    """Schema para crear usuario."""
    password: str

class UserLogin(BaseModel):
    """Schema para login."""
    username: str
    password: str

class UserResponse(UserBase):
    """Schema de respuesta para usuario."""
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    """Schema para token."""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Schema para datos del token."""
    username: str | None = None
