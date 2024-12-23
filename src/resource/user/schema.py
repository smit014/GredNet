from pydantic import BaseModel
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone_no: Optional[int] = None
    address: Optional[str] = None
