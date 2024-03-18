from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.Usuarios import db
from models.Peliculas import Pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/')
def listar_peliculas():
    lista_peliculas = Pelicula.query.all()
    return render_template('listar_peliculas.html', peliculas=lista_peliculas)

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        datos_pelicula = {
            'nombre': request.form.get('nombre'),
            'genero': request.form.get('genero'),
            'duracion': request.form.get('duracion', type=int),
            'inventario': request.form.get('inventario', default=1, type=int)
        }

        if not all([datos_pelicula['nombre'], datos_pelicula['genero'], datos_pelicula['duracion']]):
            flash('Nombre, género y duración son campos obligatorios.', 'warning')
            return render_template('agregar_pelicula.html')

        nueva_pelicula = Pelicula(**datos_pelicula)
        db.session.add(nueva_pelicula)
        try:
            db.session.commit()
            flash('¡Nueva película agregada exitosamente!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'No se pudo agregar la película debido a: {e}', 'danger')

        return redirect(url_for('pelicula.listar_peliculas'))

    return render_template('agregar_pelicula.html')

@pelicula_blueprint.route('/editar/<int:idPelicula>', methods=['GET', 'POST'])
def editar_pelicula(idPelicula):
    film = Pelicula.query.get_or_404(idPelicula)
    if request.method == 'POST':
        updates = {
            'nombre': request.form.get('nombre', film.nombre),
            'genero': request.form.get('genero', film.genero),
            'duracion': request.form.get('duracion', default=film.duracion, type=int),
            'inventario': request.form.get('inventario', default=film.inventario, type=int)
        }

        Pelicula.query.filter_by(idPelicula=idPelicula).update(updates)
        try:
            db.session.commit()
            flash('Información de la película actualizada con éxito.', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'La actualización falló debido a: {e}', 'danger')

        return redirect(url_for('pelicula.listar_peliculas'))

    return render_template('editar_pelicula.html', pelicula=film)

@pelicula_blueprint.route('/eliminar/<int:idPelicula>', methods=['POST'])
def eliminar_pelicula(idPelicula):
    film = Pelicula.query.get_or_404(idPelicula)
    try:
        db.session.delete(film)
        db.session.commit()
        flash('Película eliminada satisfactoriamente.', 'info')
    except Exception as e:
        db.session.rollback()
        flash(f'No fue posible eliminar la película debido a: {e}', 'danger')

    return redirect(url_for('pelicula.listar_peliculas'))
