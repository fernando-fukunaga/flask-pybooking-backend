import pyodbc

connection_string = (
    'DRIVER=MySQL ODBC 8.2 ANSI Driver;'
    'SERVER=localhost;'
    'DATABASE=pybooking;'
    'UID=root;'
    'charset=utf8mb4;'
)

connection = pyodbc.connect(connection_string)
