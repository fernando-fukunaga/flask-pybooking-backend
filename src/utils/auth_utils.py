from src.providers.token_provider import jwt_decode
from src.models.user_model import User
from src.errors import errors
from src.repositories.user_repository import UserRepository
from jose import JWTError
from flask import request


def get_logged_in_user(token: str) -> User:
    try:
        email = jwt_decode(token)
    except JWTError:
        raise errors.error_401("Invalid or expired token!")
    
    if not email:
        raise errors.error_401("Invalid or expired token!")
    
    usuario = UserRepository.get_user_by_email(email)
    if not usuario:
        raise errors.error_401("Invalid or expired token!")
    
    return usuario


def verify_headers_and_retrieve_token(request: request) -> str:
    try:
        token = request.headers["Authorization"]
    except Exception:
        raise errors.error_400("Authorization header is required!")
    
    return token
