import mysql.connector
from mysql.connector import Error

def dbConnection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='libreria_db',
            user='root',  # Cambia esto por tus credenciales
            password=''   # Cambia esto por tu contraseña
        )
        return connection
    except Error as e:
        print(f'Error de conexión con la base de datos: {e}')
        return None