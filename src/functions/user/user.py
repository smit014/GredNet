from datetime import datetime
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from src.config import Config
from sqlalchemy.orm import Session
from src.resource.user.model import User
from sqlalchemy.exc import SQLAlchemyError


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



def update_user_details(user_data, user_id, db: Session):
    try:
        user = (
            db.query(User)
            .filter_by(id=user_id.get("id"), is_active=True, is_deleted=False)
            .first()
        )
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Update user details if provided
        if user_data.name is not None:
            user.name = user_data.name
        if user_data.phone_no is not None:
            user.phone_no = user_data.phone_no
        if user_data.address is not None:
            user.address = user_data.address

        user.updated_at = datetime.now()  # Set updated timestamp
        db.commit()

        return JSONResponse({"message": "User updated successfully"})
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of an error
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    



def delete_user(user_id: str, current_user: dict, db: Session):
    """
    Function to soft delete a user.
    """
    try:
        # Ensure the user is deleting their own account
        if user_id != current_user.get("id"):
            raise HTTPException(status_code=403, detail="Unauthorized action")

        # Query for the user
        user_data = (
            db.query(User)
            .filter_by(id=user_id, is_active=True, is_deleted=False)
            .first()
        )

        if not user_data:
            raise HTTPException(status_code=404, detail="User not found")

        # Soft delete the user
        user_data.is_active = False
        user_data.is_deleted = True
        user_data.updated_at = datetime.now()
        db.commit()

        return JSONResponse({"message": "User deleted successfully"})
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction on failure
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

