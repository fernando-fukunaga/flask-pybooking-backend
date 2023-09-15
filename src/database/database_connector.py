import pyodbc

connection_string = (
    'DRIVER=MySQL ODBC 8.0 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=pybooking;'
    'UID=root;'
    'PWD=senha;'
    'charset=utf8mb4;'
)

connection = pyodbc.connect(connection_string)
