class User:
    
    def __init__(self, id: int, name: str, email: str, password: str) -> None:
        self._id = id
        self._name = name
        self._email = email
        self._password = password

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id: id):
        if new_id:
            self._id = new_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if new_name:
            self._name = new_name
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email: str):
        if new_email:
            self._email = new_email
