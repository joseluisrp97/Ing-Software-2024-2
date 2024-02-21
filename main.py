from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models.usuarios import db

app = Flask(__name__)
# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost/lab_ing_software'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

# Importación de modelos después de la inicialización de la base de datos
from models.usuarios import Usuario
from models.peliculas import Pelicula
from models.rentar import Rentar

# Función para ver registros en una tabla
def ver_registros():
    print("\nSeleccione la tabla para ver registros:")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Rentar")
    tabla = input("Seleccione una opción: ")

    if tabla == '1':
        usuarios = Usuario.query.all()
        for usuario in usuarios:
            print(usuario)
    elif tabla == '2':
        peliculas = Pelicula.query.all()
        for pelicula in peliculas:
            print(pelicula)
    elif tabla == '3':
        rentas = Rentar.query.all()
        for renta in rentas:
            print(renta)
    else:
        print("Opción no válida.")

# Función para filtrar registros por ID
def filtrar_por_id():
    print("\nSeleccione la tabla para filtrar por ID:")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Rentar")
    tabla = input("Seleccione una opción: ")
    id_seleccionado = input("Ingrese el ID: ")

    try:
        if tabla == '1':
            usuario = Usuario.query.filter_by(idUsuario=id_seleccionado).first()
            print(usuario if usuario else "Usuario no encontrado.")
        elif tabla == '2':
            pelicula = Pelicula.query.filter_by(idPelicula = id_seleccionado).first()
            print(pelicula if pelicula else "Película no encontrada.")
        elif tabla == '3':
            renta = Rentar.query.filter_by(idRentar = id_seleccionado).first()
            print(renta if renta else "Renta no encontrada.")
        else:
            print("Opción no válida.")
    except Exception as e:
        print(f"Error al filtrar registros: {e}")

# Función para actualizar un registro
def actualizar_registro():
    print("\nSeleccione la tabla para actualizar un registro:")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Rentar")
    tabla = input("Seleccione una opción: ")
    id_seleccionado = input("Ingrese el ID del registro a actualizar: ")

    if tabla == '1':
        nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
        usuario = Usuario.query.filter(idUsuario = id_seleccionado).first()
        if usuario:
            usuario.nombre = nuevo_nombre
            db.session.commit()
            print("Usuario actualizado con éxito.")
        else:
            print("Usuario no encontrado.")

    elif tabla == '2':
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        pelicula = Pelicula.query.filter_by(idPelicula = id_seleccionado).first()
        if pelicula:
            pelicula.nombre = nuevo_nombre
            db.session.commit()
            print("Película actualizada con éxito.")
        else:
            print("Película no encontrada.")

    elif tabla == '3':
        nueva_fecha = input("Ingrese la nueva fecha de renta (YYYY-MM-DD): ")
        renta = Rentar.query.filter_by(idRentar = id_seleccionado).first()
        if renta:
            from datetime import datetime
            renta.fecha_renta = datetime.strptime(nueva_fecha, "%Y-%m-%d")
            db.session.commit()
            print("Fecha de renta actualizada con éxito.")
        else:
            print("Renta no encontrada.")
    else:
        print("Opción no válida.")

# Función para eliminar un registro
def eliminar_registro():
    print("\nSeleccione la tabla para eliminar registros:")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Rentar")
    tabla = input("Seleccione una opción: ")

    if tabla in ['1', '2', '3']:
        id_seleccionado = input("Ingrese el ID del registro a eliminar o 'TODOS' para eliminar todos los registros: ")
        if id_seleccionado.upper() == "TODOS":
            confirmacion = input("Está seguro que desea eliminar TODOS los registros? (s/n): ")
            if confirmacion.lower() == 's':
                if tabla == '1':
                    Usuario.query.delete()
                elif tabla == '2':
                    Pelicula.query.delete()
                elif tabla == '3':
                    Rentar.query.delete()
                db.session.commit()
                print("Todos los registros han sido eliminados.")
        else:
            if tabla == '1':
                usuario = Usuario.query.filter(idUsuario = id_seleccionado).first()
                if usuario:
                    db.session.delete(usuario)
                    db.session.commit()
                    print("Usuario eliminado con éxito.")
            elif tabla == '2':
                pelicula = Pelicula.query.filter_by(idPelicula = id_seleccionado).first()
                if pelicula:
                    db.session.delete(pelicula)
                    db.session.commit()
                    print("Película eliminada con éxito.")
            elif tabla == '3':
                renta = Rentar.query.filter_by(idRentar = id_seleccionado).first()
                if renta:
                    db.session.delete(renta)
                    db.session.commit()
                    print("Renta eliminada con éxito.")
    else:
        print("Opción no válida.")

# Función para mostrar el menú y manejar las opciones
def menu():
    while True:
        print("\nMenú:")
        print("1. Ver registros de una tabla")
        print("2. Filtrar registros por ID")
        print("3. Actualizar un registro")
        print("4. Eliminar un registro")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            ver_registros()
        elif opcion == '2':
            filtrar_por_id()
        elif opcion == '3':
            actualizar_registro()
        elif opcion == '4':
            eliminar_registro()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()


