import pymysql
from pymysql import MySQLError
from contextlib import closing
from datetime import datetime, timedelta

# Parámetros de conexión a la base de datos
db_params = {
    'host': 'localhost',
    'user': 'lab',
    'password': 'Developer123!',
    'db': 'lab_ing_software'
}

def insertar_usuario(nombre, password, email, superUser):
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO usuarios (nombre, password, email, superUser) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nombre, password, email, superUser))
                conn.commit()
    except MySQLError as e:
        print(f"Error al insertar usuario: {e}")

def insertar_pelicula(nombre, genero, duracion, inventario):
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (nombre, genero, duracion, inventario))
                conn.commit()
    except MySQLError as e:
        print(f"Error al insertar película: {e}")

def cambiar_genero_pelicula(idPelicula, nuevo_genero):
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                sql = "UPDATE peliculas SET genero = %s WHERE idPelicula = %s"
                cursor.execute(sql, (nuevo_genero, idPelicula))
                conn.commit()
    except MySQLError as e:
        print(f"Error al cambiar género de la película: {e}")

def eliminar_rentas_antiguas():
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                fecha_limite = datetime.now() - timedelta(days=3)
                sql = "DELETE FROM rentar WHERE fecha_renta < %s"
                cursor.execute(sql, (fecha_limite,))
                conn.commit()
    except MySQLError as e:
        print(f"Error al eliminar rentas antiguas: {e}")

# Ejemplo de uso de las funciones
insertar_usuario('Juan Perez', 'pass123', 'juan.perez@example.com', 0)
insertar_pelicula('Inception', 'Ciencia Ficción', 148, 5)
cambiar_genero_pelicula(1, 'Acción')
eliminar_rentas_antiguas()
