from pydantic import BaseModel, Field
from typing import Optional
import datetime


class Account(BaseModel):
    username: str
    email: str
    phone_number: str
    hobbies: str
    created_at: Optional[str] = Field(default_factory=lambda: datetime.now().strftime("%d-%m-%Y %H:%M:%S"))