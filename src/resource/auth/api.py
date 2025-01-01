from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.functions.user.user import get_current_user
from src.resource.auth.schema import UserRequest, UserLoginRequest, Token
from src.functions.auth.auth import create_user, login_user, verify_user, verify_otp
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


@auth_router.post("/login", status_code=201, response_model=Token)
def login_api(user_data: UserLoginRequest, db: Session = Depends(get_db)):
    """
    Endpoint to log in a user and return an access token.
    """
    try:
        user_info = login_user(user_data.model_dump(), db)
        return user_info
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


# $ API to send OTP for SPID verification
@auth_router.post("/verify-user")
def verify_user_api(spid_no: int, db: Session = Depends(get_db)):

    return verify_user(spid_no, db)


# $ API to verify OTP and update the user table.
@auth_router.post("/verify-otp")
def verify_otp_api(
    spid_no: int,
    otp: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """ """
    return verify_otp(spid_no, otp, current_user, db)
