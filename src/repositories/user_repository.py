from src.database.database_connector import connection, cursor
from src.models.user_model import User


class UserRepository:

    def insert_user(payload: dict) -> User:
        new_user = User(name=payload["name"],
                        email=payload["email"],
                        password=payload["password"])
        cursor.execute(
            "insert into users(name,email,password) values(?,?,?)",
            new_user.name,
            new_user.email,
            new_user.password
        )
        connection.commit()
        return new_user
