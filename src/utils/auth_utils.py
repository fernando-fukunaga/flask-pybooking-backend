from src.utils.current_user import current_user


def token_is_valid(token: str) -> bool:
    if token == current_user.token:
        return True
    else:
        return False
