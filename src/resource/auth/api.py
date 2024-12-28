from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.resource.auth.schema import UserRequest, UserLoginRequest, Token
from src.functions.auth.auth import create_user, login_user
from database.database import Sessionlocal
from fastapi.responses import JSONResponse

auth_router = APIRouter()

# Dependency to get database session
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()

@auth_router.post("/signup", status_code=201)
def create_user_api(user_data: UserRequest, db: Session = Depends(get_db)):
    """
    Endpoint to create a new user.
    """
    try:
        user_info = create_user(user_data.model_dump(), db)
        return user_info
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={
                "status": False,
                "code": 500,
                "detail": f"Database error: {str(e)}",
                "data":{}
            },)


@auth_router.post("/login", status_code=201, response_model=Token)
def login_api(user_data: UserLoginRequest, db: Session = Depends(get_db)):
    """
    Endpoint to log in a user and return an access token.
    """
    try:
        user_info = login_user(user_data.model_dump(), db)
        return user_info
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={
                "status": False,
                "code": 500,
                "detail": f"Database error: {str(e)}",
                "data":{}
            },)
