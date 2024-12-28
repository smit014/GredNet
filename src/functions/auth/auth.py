from database.database import Sessionlocal
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy import or_
from datetime import timedelta
import uuid
from src.resource.user.model import User
from src.utils.jwt_token import create_jwt_token

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/token")


def get_db():
    """Provide a session context for database operations."""
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


def create_user(user_details, db: Session):
    try:
        id = str(uuid.uuid4())

        # Validate email and phone number presence
        if not user_details.get("email") or not user_details.get("phone_no"):
            return JSONResponse(
                status_code=422,
                content={
                    "status": False,
                    "code": 422,
                    "message": "Add email or phone number",
                    "data":{}
                },
            )

        if not user_details.get("password"):
            return JSONResponse(
                status_code=422,
                content={
                    "status": False,
                    "code": 422,
                    "message": "Password is required",
                    "data":{}
                },
            )

        # Check for existing user
        existing_user = (
            db.query(User)
            .filter_by(email=user_details.get("email"), is_active=True)
            .first()
        )
        if existing_user:
            return JSONResponse(
                status_code=403,
                content={
                    "status": False,
                    "code": 403,
                    "message": "Email is already used. Please log in or use another email.",
                    "data":{}
                },
            )

        # Create new user
        user_info = User(
            id=id,
            name=user_details.get("name"),
            email=user_details.get("email"),
            phone_no=user_details.get("phone_no"),
            password=bcrypt_context.hash(user_details.get("password")),
            address=user_details.get("address"),
        )
        db.add(user_info)
        db.commit()

        return JSONResponse(
            content={
                "status": True,
                "code": 201,
                "message": "User created successfully",
                "data": {
                    "user_id": id,
                    "name": user_details.get("name"),
                    "email": user_details.get("email"),
                    "phone_no": user_details.get("phone_no"),
                    "address": user_details.get("address"),
                },
            },
            status_code=201,
        )
    except SQLAlchemyError as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "detail": f"Database error: {str(e)}",
                "data":{}
            },
        )



def login_user(user_details, db: Session):
    """
    Authenticate a user using email or phone number and return a JWT token.
    """
    try:
        email = user_details.get("email")
        phone_no = user_details.get("phone_no")
        password = user_details.get("password")

        # Ensure either email or phone number is provided
        if not email and not phone_no:
            return JSONResponse(
                status_code=400,
                content={
                    "status": False,
                    "code": 400,
                    "message": "Email or phone number is required",
                    "data":{}
                },
            )

        # Query the user by email or phone number
        user_data = (
            db.query(User)
            .filter(
                or_(User.email == email, User.phone_no == phone_no),
                User.is_active == True,
                User.is_deleted == False,
            )
            .first()
        )

        # Check if the user exists
        if not user_data:
            return JSONResponse(
                status_code=404,
                content={
                    "status": False,
                    "code": 404,
                    "message": "User not found",
                    "data":{}
                },
            )

        # Verify the provided password
        if not bcrypt_context.verify(password, user_data.password):
            return JSONResponse(
                status_code=401,
                content={
                    "status": False,
                    "code": 401,
                    "message": "Incorrect password",
                    "data":{}
                },
            )

        # Create the JWT token
        token = create_jwt_token(
            id=user_data.id,
            name=user_data.name,
            email=user_data.email,
            phone_no=user_data.phone_no,
            expires_delta=timedelta(days=7),
        )

        # Return success response with user details
        return JSONResponse(
            content={
                "status": True,
                "code": 200,
                "detail": "Login successful",
                "data": {
                    "access_token": token,
                    "type": "bearer",
                    "user": {
                        "id": user_data.id,
                        "name": user_data.name,
                        "email": user_data.email,
                        "phone_no": user_data.phone_no,
                        "address": user_data.address,
                        "created_at": user_data.created_at.isoformat() if user_data.created_at else None,
                        "updated_at": user_data.updated_at.isoformat() if user_data.updated_at else None,
                    },
                },
            },
            status_code=200,
        )
    except SQLAlchemyError as e:
        return JSONResponse(
            status_code=500,
            content={
                "status":False,
                "code": 500,
                "detail": f"Database error: {str(e)}",
                "data":{}
            },
        )
