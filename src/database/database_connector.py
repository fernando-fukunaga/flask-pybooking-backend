import pyodbc
from src.config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD

connection_string = (
    'DRIVER=MySQL ODBC 8.2 ANSI Driver;'
    'SERVER={0};'
    'DATABASE=pybooking;'
    'UID={1};'
#    'PWD={2};'
    'charset=utf8mb4;'.format(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD)
)

connection = pyodbc.connect(connection_string)
