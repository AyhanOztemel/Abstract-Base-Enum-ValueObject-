from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLAEnum
from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

class Status(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(SQLAEnum(Status), default=Status.ACTIVE)
