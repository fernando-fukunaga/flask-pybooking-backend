from src.repositories.user_repository import insert_user, select_user_by_email, select_user_by_email_and_password
from src.schemas.user_schemas import UserNoPassword, SucessfulSignIn
from src.models.user_model import User
from src.errors import errors
from src.providers.hash_provider import hash_password
from src.providers.token_provider import jwt_encode


def _email_already_registered(email: str) -> bool:
    if select_user_by_email(email):
        return True
    else:
        return False
    

def sign_up_service(payload: dict) -> UserNoPassword:
    user = User(name=payload["name"],
                email=payload["email"],
                password=payload["password"])
    
    if _email_already_registered(user.email) == True:
        raise errors.error_400("E-mail already registered!")
    
    if len(user.password) > 14:
        raise errors.error_400("Password can't be longer than 14 characters!")

    user.password = hash_password(user.password)
    response_payload = UserNoPassword()
    return response_payload.dump(insert_user(user))


def sign_in_service(payload: dict) -> SucessfulSignIn:
    user = select_user_by_email_and_password(payload["email"],
                                             payload["password"])
    if user:
        response_payload = SucessfulSignIn()
        jwt_payload = {"email": user.email}
        token = jwt_encode(jwt_payload)
        response_payload.email = user.email
        response_payload.access_token = token
        return response_payload.dump(response_payload)
    else:
        raise errors.error_400("Wrong e-mail or password, please try again!")
