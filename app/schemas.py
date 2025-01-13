from pydantic import BaseModel
from enum import Enum
from pydantic import EmailStr

class Roles(str, Enum):
    user = "user"
    admin = "admin"

class UserBase(BaseModel):
    username: str
    is_active: bool
    email: EmailStr
    role: Roles = "user"

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True