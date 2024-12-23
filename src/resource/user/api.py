from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from src.functions.user.user import get_current_user
from database.database import Sessionlocal
from src.resource.user.model import User

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
    breakpoint()
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
