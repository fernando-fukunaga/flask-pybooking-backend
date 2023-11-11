class CurrentUser:
    def __init__(self, email: str, token: str) -> None:
        self._email = email
        self._token = token

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email: str):
        if new_email:
            self._email = new_email

    @property
    def token(self):
        return self._token
    
    @token.setter
    def token(self, new_token: str):
        if new_token:
            self._token = new_token


current_user = CurrentUser("", "")
