import os

JWT_SECRET_KEY = os.getenv("jwt_secret_key")
DATABASE_HOST = os.getenv("db_host")
DATABASE_USER = os.getenv("db_usr")
DATABASE_PASSWORD = os.getenv("db_pwd")