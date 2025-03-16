from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime
import re
import bcrypt

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username must be between 3 and 50 characters")
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters long")
    email: EmailStr = Field(..., description="Must be a valid email address")
    phone_number: str = Field(..., description="Must be a valid phone number")
    hobby: str = Field(..., min_length=2, max_length=100, description="Hobby must be between 2 and 100 characters")
    created_at: Optional[str] = Field(default_factory=lambda: datetime.now().isoformat(), description="Timestamp of user creation")

    @validator("phone_number")
    def validate_phone_number(cls, value):
        phone_regex = r"^(\+62|62|0)8[1-9][0-9]{6,9}$"
        if not re.match(phone_regex, value):
            raise ValueError("Phone number must be a valid Indonesian phone number")
        return value

    @validator("password")
    def hash_password(cls, value):
        hashed_password = bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt())
        return hashed_password.decode("utf-8")