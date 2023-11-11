from pyodbc import Connection
from src.providers.token_provider import jwt_decode
from jose import JWTError


def get_logged_in_user(token: str, connection: Connection) -> str:
    cursor = connection.cursor()

    try:
        jwt_decode(token)
    except JWTError as e:
        raise e