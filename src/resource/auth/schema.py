from pydantic import BaseModel, EmailStr
from typing import Optional

class Token(BaseModel):
    access_token : str
    token_type : str


class UserRequest(BaseModel):
    name: str
    email: EmailStr
    phone_no: str 
    password: str
    role: Optional[str] = "alumni"

class UserLoginRequest(BaseModel):
    phone_no: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str]