from jose import jwt
from src.config import JWT_SECRET_KEY

ALGORITHM = "HS256"


def jwt_encode(payload: dict) -> str:
    payload_copy = payload.copy()
    token = jwt.encode(payload_copy, JWT_SECRET_KEY, algorithm=ALGORITHM)

    return token


def jwt_decode(token: str) -> str:
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=ALGORITHM)

    return payload["email"]