from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    login: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    login: Optional[str]
    password: Optional[str]

class UserOut(BaseModel):
    id: int
    email: EmailStr
    login: str
    created_at: str
    updated_at: str

class PostCreate(BaseModel):
    author_id: int
    title: str
    content: str

class PostUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]

class PostOut(BaseModel):
    id: int
    author_id: int
    title: str
    content: str
    created_at: str
    updated_at: str
