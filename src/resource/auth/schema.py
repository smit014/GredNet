from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token : str
    token_type : str


class UserRequest(BaseModel):
    name: str
    phone_no: str
    email: str
    password: str
    address: Optional[str]= None

class UserLoginRequest(BaseModel):
    phone_no: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str]