from jose import jwt
from src.config import JWT_SECRET_KEY
from datetime import datetime, timedelta

ALGORITHM = "HS256"
EXPIRES_IN_MIN = 60


def jwt_encode(payload: dict) -> str:
    payload_copy = payload.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)
    payload_copy["exp"] = expiration
    token = jwt.encode(payload_copy, JWT_SECRET_KEY, algorithm=ALGORITHM)

    return token


def jwt_decode(token: str) -> str:
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=ALGORITHM)

    return payload["email"]
