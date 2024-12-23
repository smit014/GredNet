from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from src.config import Config

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    """
    Decode the JWT token and return user details (email, phone_no, etc.) if valid.
    """
    try:
        # Decode the token
        payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.ALGORITHM])
        
        # Extract user details from the token
        id: str = payload.get("sub")
        name: str = payload.get("name")
        email: str = payload.get("email")
        phone_no: str = payload.get("phone_no")

        # Validate that all required fields are present
        if not id or not email or not phone_no:
            raise HTTPException(status_code=401, detail="Invalid token: Missing required user information.")

        # Return user details as a dictionary
        return {
            "id": id,
            "name": name,
            "email": email,
            "phone_no": phone_no
        }

    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Token validation error: {str(e)}")
