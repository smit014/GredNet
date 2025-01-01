import uuid
from random import randint
from database.database import Sessionlocal
from src.resource.admin.model import Data ,OTP
from src.resource.user.model import User
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError
from fastapi.responses import JSONResponse
from datetime import timedelta, datetime
from sqlalchemy import or_
from src.utils.jwt_token import create_jwt_token
from src.utils.send_mail import send_email

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
                    "data": {},
                },
            )

        if not user_details.get("password"):
            return JSONResponse(
                status_code=422,
                content={
                    "status": False,
                    "code": 422,
                    "message": "Password is required",
                    "data": {},
                },
            )
        
        if not user_details.get("role"):
            return JSONResponse(
                status_code=422,
                content={
                    "status": False,
                    "code": 422,
                    "message": "Please, Select the Role",
                    "data": {},
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
                    "data": {},
                },
            )

        # Create new user
        user_info = User(
            id=id,
            name=user_details.get("name"),
            email=user_details.get("email"),
            phone_no=user_details.get("phone_no"),
            password=bcrypt_context.hash(user_details.get("password")),
            role=user_details.get("role"),
        )
        db.add(user_info)
        db.commit()

        return JSONResponse(
            content={
                "status": True,
                "code": 200,
                "message": "User created successfully",
                "data": {
                    "user": {
                        "user_id": id,
                        "name": user_details.get("name"),
                        "email": user_details.get("email"),
                        "phone_no": user_details.get("phone_no"),
                        "role": user_details.get("role"),
                    }
                },
            },
            status_code=200,
        )
    except SQLAlchemyError as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data": {},
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
                    "data": {},
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
                    "data": {},
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
                    "data": {},
                },
            )

        # Create the JWT token
        token = create_jwt_token(
            id=user_data.id,
            name=user_data.name,
            email=user_data.email,
            phone_no=user_data.phone_no,
            role = user_data.role,
            expires_delta=timedelta(days=7),
        )

        # Return success response with user details
        return JSONResponse(
            content={
                "status": True,
                "code": 200,
                "message": "Login successful",
                "data": {
                    "access_token": token,
                    "user": {
                        "id": user_data.id,
                        "name": user_data.name,
                        "email": user_data.email,
                        "phone_no": user_data.phone_no,
                        "role": user_data.role,
                        "created_at": (
                            user_data.created_at.isoformat()
                            if user_data.created_at
                            else None
                        ),
                        "updated_at": (
                            user_data.updated_at.isoformat()
                            if user_data.updated_at
                            else None
                        ),
                    },
                },
            },
            status_code=200,
        )
    except SQLAlchemyError as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data": {},
            },
        )
    

def verify_user(spid_no: int, db: Session):
    """
    Verify user using SPID number and OTP.
    """
    try:
        # Check if SPID exists in the datasources table
        alumni = db.query(Data).filter_by(spid_no=spid_no).first()
        if not alumni:
            return JSONResponse(
                status_code=404,
                content={
                    "status": False,
                    "code": 404,
                    "message": "SPID number not found in datasources",
                    "data": {},
                },
            )

        # Generate a random OTP
        otp_code = randint(100000, 999999)

        # Store OTP in the database
        otp_entry = OTP(
            id=str(uuid.uuid4()),
            email=alumni.email,
            otp=otp_code,
        )
        db.add(otp_entry)
        db.commit()

        # Send OTP via email
        email_body = f"Your OTP for verification is: {otp_code}"
        send_email(to_email=alumni.email, subject="Verification OTP", body=email_body)

        return JSONResponse(
            status_code=200,
            content={
                "status": True,
                "code": 200,
                "message": "OTP sent successfully",
                "data": {"spid_no": spid_no},
            },
        )
    except SQLAlchemyError as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data": {},
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Unexpected error: {str(e)}",
                "data": {},
            },
        )

def verify_otp(spid_no: int, otp: int, user:dict, db: Session):
    """
    Verify the OTP for the given SPID.
    """
    try:
        # Extract user details from the dictionary
        data = user.get("data")
        user_data = data.get("user")
        user_id = user_data.get("id")
        breakpoint()
        # Check if SPID exists in the datasources table
        alumni = db.query(Data).filter_by(spid_no=spid_no).first()
        if not alumni:
            return JSONResponse(
                status_code=404,
                content={
                    "status": False,
                    "code": 404,
                    "message": "SPID number not found in datasources",
                    "data": {},
                },
            )

        # Validate the OTP
        otp_entry = db.query(OTP).filter_by(email=alumni.email, otp=otp).first()
        if not otp_entry:
            return JSONResponse(
                status_code=401,
                content={
                    "status": False,
                    "code": 401,
                    "message": "Invalid OTP",
                    "data": {},
                },
            )

        # Update the user table for the verified alumni
        user = db.query(User).filter_by(id=user_id).first()
        if not user:
            return JSONResponse(
                status_code=404,
                content={
                    "status": False,
                    "code": 404,
                    "message": "User not found",
                    "data": {},
                },
            )

        user.is_verify = True
        user.updated_at = datetime.now()
        db.commit()

        return JSONResponse(
            status_code=200,
            content={
                "status": True,
                "code": 200,
                "message": "Verification successful",
                "data": {
                    "user": {
                        "id": user.id,
                        "name": user.name,
                        "email": user.email,
                        "phone_no": user.phone_no,
                        "role": user.role,
                        "is_verified": user.is_verify,
                    }
                },
            },
        )
    except SQLAlchemyError as e:
        db.rollback()
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Database error: {str(e)}",
                "data": {},
            },
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "status": False,
                "code": 500,
                "message": f"Unexpected error: {str(e)}",
                "data": {},
            },
        )

