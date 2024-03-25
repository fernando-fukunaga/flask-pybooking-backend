import psycopg
from src.config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD

connection = psycopg.connect(
    f"""host={DATABASE_HOST}
    dbname=pybooking
    user={DATABASE_USER}
    password={DATABASE_PASSWORD}"""
)
