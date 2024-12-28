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
            return JSONResponse(
                status_code=401,
                content={
                    "status": False,
                    "code": 401,
                    "message": "Invalid token: Missing required user information.",
                    "data":{}
                }
            )

        # Return success response with user details
        return JSONResponse({
            "status": "Success",
            "code": 200,
            "message": "Current user details.",
            "data": {
                "id": id,
                "name": name,
                "email": email,
                "phone_no": phone_no
            }
        })

    except JWTError as e:
        return JSONResponse(
            status_code=401,
            content={
                "status": False,
                "code": 401,
                "message": f"Token validation error: {str(e)}",
                "data":{}
            }
        )



def update_user_details(user_data, user_id, db: Session):
    """
    Function to update user details in the database.
    """
    try:
        id =user_id.get("data")
        user = (
            db.query(User)
            .filter_by(id=id.get("id"), is_active=True, is_deleted=False)
            .first()
        )
        if not user:
            return JSONResponse(
                status_code=200,
                content={
                    "status": False,
                    "code": 404,
                    "message": "User not found",
                    "data":{}
                }
            )

        # Update user details if provided
        if user_data.name is not None:
            user.name = user_data.name
        if user_data.phone_no is not None:
            user.phone_no = user_data.phone_no
        if user_data.address is not None:
            user.address = user_data.address

        user.updated_at = datetime.now()  # Set updated timestamp
        db.commit()

        # Return success response
        return JSONResponse(
            status_code=200,
            content={
                "status": True,
                "code": 200,
                "message": "User updated successfully",
                "data": {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "phone_no": user.phone_no,
                    "address": user.address,
                    "updated_at": user.updated_at.isoformat()
                }
            }
        )
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction in case of an error
        return JSONResponse(
            status_code=200,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data":{}
            }
        )



def delete_user(user_id: str, current_user: dict, db: Session):
    """
    Function to soft delete a user.
    """
    try:
        current_user = current_user.get("data")
        # Ensure the user is deleting their own account
        if user_id != current_user.get("id"):
            return JSONResponse(
                status_code=403,
                content={
                    "status": False,
                    "code": 403,
                    "message": "Unauthorized action",
                    "data":{}
                }
            )

        # Query for the user
        user_data = (
            db.query(User)
            .filter_by(id=user_id, is_active=True, is_deleted=False)
            .first()
        )

        if not user_data:
            return JSONResponse(
                status_code=404,
                content={
                    "status": False,
                    "code": 404,
                    "message": "User not found",
                    "data":{}
                }
            )

        # Soft delete the user
        user_data.is_active = False
        user_data.is_deleted = True
        user_data.updated_at = datetime.now()
        db.commit()

        # Return success response
        return JSONResponse(
            status_code=200,
            content={
                "status": True,
                "code": 200,
                "message": "User deleted successfully",
                "data": {
                    "id": user_data.id,
                    "name": user_data.name,
                    "email": user_data.email,
                    "phone_no": user_data.phone_no,
                    "updated_at": user_data.updated_at.isoformat()
                }
            }
        )
    except SQLAlchemyError as e:
        db.rollback()  # Rollback transaction on failure
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data":{}
            }
        )
