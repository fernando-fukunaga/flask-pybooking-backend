from src.database.database_connector import connection
from src.models.user_model import User
from werkzeug.exceptions import InternalServerError, BadRequest
from src.utils.current_user import current_user


class UserRepository:

    def _email_already_registered(self, email: str) -> bool:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from users where email=?",
                email
            )
            if cursor.fetchall():
                return True
            else:
                return False
            
        except Exception:
            raise InternalServerError(
                description="An internal connection error has occured!"
            )

    def insert_user(self, payload: dict) -> User:
        if self._email_already_registered(payload["email"]):
            raise BadRequest(description="E-mail already registered!")
        
        if len(payload["password"]) > 14:
            raise BadRequest(
                description="Password can't be longer than 14 characters!"
            )
        
        cursor = connection.cursor()
        new_user = User(name=payload["name"],
                        email=payload["email"],
                        password=payload["password"])

        try:
            cursor.execute(
                "insert into users(name,email,password) values(?,?,?)",
                new_user.name,
                new_user.email,
                new_user.password
            )
            connection.commit()

        except Exception:
            raise InternalServerError(
                description="An internal connection error has occured!"
            )
        
        return new_user

    def authenticate_user(self, payload: dict) -> User:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from users where email=? and password=?",
                payload["email"],
                payload["password"]
            )
            
        except Exception:
            raise InternalServerError(
                description="An internal connection error has occured!"
            )
        
        query_result = cursor.fetchone()

        if query_result:
            user = User("", payload["email"], "")
            current_user.email = payload["email"]
            current_user.token = "fake_token"
            return user
        else:
            raise BadRequest(
                description="Wrong e-mail or password, try again!"
            )

    def get_user_by_email(self, email: str) -> User:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from users where email = ?",
                email
            )

        except Exception:
            raise InternalServerError(
                description="An internal connection error has occured!"
            )
        
        query_result = cursor.fetchone()
        
        if query_result:
            user = User(query_result[1], query_result[2], query_result[3])
            return user
        else:
            raise BadRequest(
                description="User not found!"
            )
        