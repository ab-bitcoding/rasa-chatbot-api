from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from uuid import UUID
from datetime import datetime


class CreateUserData(BaseModel):
    username: str
    email: EmailStr
    age: int
    phone_number: str
    income: float

    @validator('username')
    def validate_username(cls, value):
        if not 1 <= len(value) <= 20:
            raise ValueError("Username length must be between 1 and 20 characters")
        if not value.isalpha():
            raise ValueError("Username must contain only alphabetic characters")
        return value

    @validator('email')
    def validate_email(cls, value):
        email_domains = [ 
            "gmail.com",
            "yahoo.com",
            'outlook.com'
        ]
        email_domain = value.split("@")[-1].lower()
        if email_domain not in email_domains:
            raise ValueError("Only emails from specific domains are allowed.")
        return value

    @validator('age')
    def validate_age(cls, value):
        if not 1 <= value <= 120:
            raise ValueError("Age is must be between 1 to 120 characters")
        return value

    @validator('phone_number')
    def validate_phone_number(cls, value):
        if not 9 < len(value) <= 15:
            raise ValueError("Phone Number must be atleast 10 digits long")
        if not value.isdigit():
            raise ValueError("Phone Number must be numeric")
        return value

    @validator('income')
    def validate_income(cls, value):
        if value <= 0:
            raise  ValueError("Income is must be a positive integer.") 
        return value



class UserData(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    age: int
    phone_number: str
    income: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None 

    class Config:
        orm_mode = True

class UpdateUserData(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    phone_number: Optional[str] = None
    income: Optional[float] = None
