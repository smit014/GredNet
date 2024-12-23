from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from src.functions.user.user import get_current_user,update_user_details,delete_user
from database.database import Sessionlocal
from src.resource.user.model import User
from src.resource.user.schema import UserUpdate

user_router = APIRouter()

# Dependency to get the database session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@user_router.get("/get_user", status_code=200)
def get_user(
    current_user: Annotated[dict, Depends(get_current_user)], 
    db: Session = Depends(get_db)
):
    """
    Get user details for the authenticated user.
    """
    # Query the database for user details using the username from the token
    user = db.query(User).filter(User.id == current_user.get("id")).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Return user details (excluding sensitive fields like password)
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone_no": user.phone_no,
    }

@user_router.put("/update_user", status_code=200)
def update_user_api(
    user_detail: UserUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    API to update user details.

    Args:
        user_detail (UserUpdate): The new data for the user.
        current_user (dict): The current authenticated user.
        db (Session): SQLAlchemy session.

    Returns:
        JSONResponse: Success or error message.
    """
    return update_user_details(user_data=user_detail, user_id=current_user, db=db)


@user_router.delete("/delete_user", status_code=200)
def delete_user_api(
    user_id: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    API to soft delete a user.

    Args:
        user_id (str): ID of the user to be deleted.
        current_user (dict): The current authenticated user.
        db (Session): SQLAlchemy session.

    Returns:
        JSONResponse: Success or error message.
    """
    return delete_user(user_id=user_id, current_user=current_user, db=db)
