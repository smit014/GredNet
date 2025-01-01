from pydantic import BaseModel, EmailStr, Field

class DataEntryRequest(BaseModel):
    spid_no: int  # Integer, pattern cannot be applied
    name: str
    phone_no: int  # Integer, pattern cannot be applied
    email: EmailStr
