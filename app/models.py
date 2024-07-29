from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean,LargeBinary,TIMESTAMP,func, TEXT, Enum
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean,LargeBinary, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import ARRAY, TEXT
from enum import Enum as PythonEnum
from uuid import uuid4

Base = declarative_base()


class Users(Base):
    __tablename__ = 'tbl_users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)  # Age is optional
    phone_number = Column(String(15), unique=True, nullable=False)  # Assuming phone number is a string
    income = Column(Integer, nullable=False)  # Assuming income is an integer (e.g., cents or dollars)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True)) 