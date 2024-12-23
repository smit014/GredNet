from src.config import Config
from datetime import datetime, timedelta
from jose import jwt

def create_jwt_token(id: str, name: str, email: str, phone_no: str, expires_delta: timedelta):
    """
    Generate a JWT token with user details.
    """
    expire = datetime.now() + expires_delta
    payload = {
        "sub": id,  # Unique identifier for the user (user_id)
        "name": name,
        "email": email,
        "phone_no": phone_no,
        "exp": expire
    }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.ALGORITHM)
    return token
