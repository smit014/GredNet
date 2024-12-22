from src.config import Config
from datetime import datetime, timedelta
from jose import jwt

def create_jwt_token(username: str, expires_delta: timedelta):
    expire = datetime.now() + expires_delta
    payload = {
        "sub": username,
        "exp": expire.isoformat()  # Convert datetime to ISO 8601 string
    }
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.ALGORITHM)
    return token
