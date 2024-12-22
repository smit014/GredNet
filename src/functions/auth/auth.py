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
            raise HTTPException(status_code=422, detail="Add email or phone number")
        if not user_details.get("password"):
            raise HTTPException(status_code=422, detail="Password is required")
        
        existing_user = db.query(User).filter_by(email=user_details.get("email"), is_active=True).first()
        if existing_user:
            raise HTTPException(status_code=403, detail="Email is already used, Please log in or Use another Email")
        
        user_info = User(
            id=id,
            name=user_details.get("name"),
            email=user_details.get("email"),
            phone_no=user_details.get("phone_no"),
            password=bcrypt_context.hash(user_details.get("password")),
        )
        db.add(user_info)
        db.commit()
        return JSONResponse({"Message": "User created successfully", "User_id": str(id)})
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


def login_user(user_details, db: Session):
    email = user_details.get("email")
    phone_no = user_details.get("phone_no")
    password = user_details.get("password")

    if email or phone_no:
        user_data = (
            db.query(User)
            .filter(
                or_((User.email == email), (User.phone_no == phone_no)),
                User.is_active == True,
                User.is_deleted == False,
            )
            .first()
        )
        if user_data:
            if bcrypt_context.verify(password, user_data.password):
                token = create_jwt_token(user_data.name, timedelta(days=7))
                return JSONResponse({"access_token": token, "type": "bearer"})
            else:
                raise HTTPException(status_code=401, detail="Incorrect password")
        else:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="Email or phone number is required")
