import pymysql
import faker
import secrets
import random
from pymysql import MySQLError
from contextlib import closing
from datetime import datetime, timedelta

# Parámetros de conexión a la base de datos
db_params = {
    'host': 'localhost',
    'user': 'lab',
    'password': 'Developer123!',
    'db': 'lab_ing_software' ,
    'charset': 'utf8mb4'
}
# Faker usado para generar nombres aletorios.
# Secrets para hacer una contraseña
# Random para seleccionar un género random
fake = faker.Faker()
generos_peliculas = ['Acción', 'Comedia', 'Drama', 'Fantasía', 'Horror', 'Misterio', 'Romance', 'Ciencia Ficción', 'Documental']

# Función para insertar 3 registros, uno por tabla, de una vez
def insertar_registros():
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                # Generar un nombre, apellidos, email y contraseña aleatorios
                nombre_aleatorio = fake.first_name()
                apPat_aleatorio = fake.last_name()
                apMat_aleatorio = fake.last_name()
                email_aleatorio = f"{nombre_aleatorio.lower()}.{apPat_aleatorio.lower()}_{datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"
                password_aleatorio = secrets.token_hex(8)  # Genera una contraseña aleatoria segura

                # Insertar un usuario con los datos aleatorios
                sql_usuario = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_usuario, (nombre_aleatorio, apPat_aleatorio, apMat_aleatorio, password_aleatorio, email_aleatorio, 0))
                id_usuario = cursor.lastrowid

                genero_aleatorio = random.choice(generos_peliculas)

                # Insertar una película con género aleatorio
                sql_pelicula = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql_pelicula, (fake.word().capitalize(), genero_aleatorio, 120, 10))
                id_pelicula = cursor.lastrowid

                # Insertar una renta
                sql_renta = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta) VALUES (%s, %s, NOW())"
                cursor.execute(sql_renta, (id_usuario, id_pelicula))

                conn.commit()
    except MySQLError as e:
        print(f"Error al insertar registros: {e}")

# Función que regresa los usuarios con apellido con cierta terminación, por parámetro
def filtrar_usuarios_por_apellido(apellido):
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
                cursor.execute(sql, ('%' + apellido, '%' + apellido))
                resultados = cursor.fetchall()
                for usuario in resultados:
                    print(usuario)
    except MySQLError as e:
        print(f"Error al filtrar usuarios por apellido: {e}")


# Función para cambiar el género de una película, por parámetro
def cambiar_genero_pelicula_por_nombre(nombre_pelicula, nuevo_genero):
    try:
        with closing(pymysql.connect(**db_params)) as conn:
            with conn.cursor() as cursor:
                # Primero, encontrar el ID de la película por su nombre
                sql_buscar = "SELECT idPelicula FROM peliculas WHERE nombre = %s"
                cursor.execute(sql_buscar, (nombre_pelicula,))
                pelicula = cursor.fetchone()
                if pelicula:
                    # Cambiar el género de la película
                    sql_actualizar = "UPDATE peliculas SET genero = %s WHERE idPelicula = %s"
                    cursor.execute(sql_actualizar, (nuevo_genero, pelicula[0]))
                    conn.commit()
                else:
                    print("Película no encontrada.")
    except MySQLError as e:
        print(f"Error al cambiar género de la película: {e}")

# Función que elimina las antiguas rentas con más de 3 días
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
insertar_registros()
filtrar_usuarios_por_apellido('a')
cambiar_genero_pelicula_por_nombre('Inception', 'Accion')
eliminar_rentas_antiguas()
