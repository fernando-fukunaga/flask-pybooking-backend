from src.database.database_connector import connection
from src.models.user_model import User
from src.errors import errors


def insert_user(user: User) -> User:
    cursor = connection.cursor()
    try:
        cursor.execute(
            "insert into users(name,email,password) values(%s,%s,%s)",
            (user.name,
             user.email,
             user.password)
        )
        connection.commit()

    except Exception:
        raise errors.error_500("An internal connection error has occurred!")
    
    return user


def select_user_by_email(email: str) -> User:
    cursor = connection.cursor()
    try:
        cursor.execute(
            "select * from users where email=%s",
            [email]
        )
        
    except Exception:
        raise errors.error_500("An internal connection error has occurred!")

    query_result = cursor.fetchone()

    if query_result:
        user = User(query_result[1], query_result[2], query_result[3])
        return user
    else:
        return None
    

def select_user_by_email_and_password(email: str, password: str) -> User:
    cursor = connection.cursor()
    try:
        cursor.execute(
            "select * from users where email=? and password=?",
            email,
            password
        )

    except Exception:
        raise errors.error_500("An internal connection error has occurred!")
    
    query_result = cursor.fetchone()

    if query_result:
        user = User(query_result[1], query_result[2], query_result[3])
        return user
    else:
        return None 

'''class UserRepository:

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
            raise errors.error_500(
                "An internal connection error has occured!"
            )

    def insert_user(self, payload: dict) -> User:
        if self._email_already_registered(payload["email"]):
            raise errors.error_400("E-mail already registered!")
        
        if len(payload["password"]) > 14:
            raise errors.error_400(
                "Password can't be longer than 14 characters!"
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
            raise errors.error_500(
                "An internal connection error has occured!"
            )
        
        return new_user

    def sign_in_user(self, payload: dict) -> SucessfulSignIn:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from users where email=? and password=?",
                payload["email"],
                payload["password"]
            )
            
        except Exception:
            raise errors.error_500(
                "An internal connection error has occured!"
            )

        if cursor.fetchone():
            jwt_payload = {"email":payload["email"]}
            token = jwt_encode(jwt_payload)
            schema = SucessfulSignIn()
            schema.email = payload["email"]
            schema.access_token = token
            response = schema.dump(schema)
            return response
        else:
            raise errors.error_400(
                "Wrong e-mail or password, try again!"
            )

    @staticmethod
    def get_user_by_email(email: str) -> User:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from users where email = ?",
                email
            )

        except Exception:
            raise errors.error_500(
                "An internal connection error has occured!"
            )
        
        query_result = cursor.fetchone()
        
        if query_result:
            user = User(query_result[1], query_result[2], query_result[3])
            return user
        else:
            raise errors.error_404("User not found!")
'''