from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from schemas import Roles
from sqlalchemy import Enum
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    username = Column(String, unique=True)
    role = Column(Enum(Roles))