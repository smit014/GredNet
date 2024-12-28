from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Token(BaseModel):
    access_token : str
    token_type : str


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    phone_no: str = Field(..., pattern="^\d{10}$")  # Ensures a valid 10-digit phone number
    password: str
    address: Optional[str]= None

class UserLoginRequest(BaseModel):
    phone_no: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str]