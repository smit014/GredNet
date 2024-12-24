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
        if not user_details.get("email") or not user_details.get("phone_no"):
            raise HTTPException(
                status_code=422,
                detail={
                    "status": "Unprocessable Content",
                    "code": 422,
                    "detail": "Add email or phone number",
                },
            )
        if not user_details.get("password"):
            raise HTTPException(
                status_code=422,
                detail={
                    "status": "Unprocessable Content",
                    "code": 422,
                    "detail": "Password is required",
                },
            )

        existing_user = (
            db.query(User)
            .filter_by(email=user_details.get("email"), is_active=True)
            .first()
        )
        if existing_user:
            raise HTTPException(
                status_code=403,
                detail={
                    "code": 403,
                    "detail": "Email is already used. Please log in or use another email.",
                },
            )

        user_info = User(
            id=id,
            name=user_details.get("name"),
            email=user_details.get("email"),
            phone_no=user_details.get("phone_no"),
            password=bcrypt_context.hash(user_details.get("password")),
        )
        db.add(user_info)
        db.commit()
        return JSONResponse(
            content={
                "status": "Success",
                "code": 201,
                "detail": "User created successfully",
                "data": {"user_id": str(id)},
            },
            status_code=201,
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Internal Server Error",
                "code": 500,
                "detail": f"Database error: {str(e)}",
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
            raise HTTPException(
                status_code=400,
                detail={
                    "status": "Bad Request",
                    "code": 400,
                    "detail": "Email or phone number is required",
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
            raise HTTPException(
                status_code=404,
                detail={
                    "status": "Not Found",
                    "code": 404,
                    "detail": "User not found",
                },
            )

        # Verify the provided password
        if not bcrypt_context.verify(password, user_data.password):
            raise HTTPException(
                status_code=401,
                detail={
                    "status": "Unauthorized",
                    "code": 401,
                    "detail": "Incorrect password",
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
                "status": "Success",
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
        raise HTTPException(
            status_code=500,
            detail={
                "status": "Internal Server Error",
                "code": 500,
                "detail": f"Database error: {str(e)}",
            },
        )
