from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.Usuarios import db
from models.Rentar import Rentar
from datetime import datetime, timedelta

rentar_blueprint = Blueprint('rentar', __name__, url_prefix='/rentar')

@rentar_blueprint.route('/')
def listar_rentas():
    rentas = Rentar.query.all()
    fecha_actual = datetime.now()
    for renta in rentas:
        # Calculamos si la renta ha vencido comparando las fechas
        renta.vencida = (renta.fecha_renta + timedelta(days=renta.dias_de_renta)) < fecha_actual
    return render_template('listar_rentas.html', rentas=rentas)

@rentar_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        idUsuario = request.form.get('idUsuario', type=int)
        idPelicula = request.form.get('idPelicula', type=int)

        if not idUsuario or not idPelicula:
            flash('Por favor, completa todos los campos requeridos.', 'warning')
            return render_template('agregar_renta.html')

        fecha_renta = datetime.now()
        nueva_renta = Rentar(idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta)
        db.session.add(nueva_renta)
        try:
            db.session.commit()
            flash('Nueva renta registrada con éxito.', 'success')
        except Exception as e:
            db.session.rollback()
            flash('Ha ocurrido un error al registrar la renta.', 'danger')

        return redirect(url_for('rentar.listar_rentas'))

    return render_template('agregar_renta.html')

@rentar_blueprint.route('/actualizar/<int:idRentar>', methods=['GET', 'POST'])
def actualizar_renta(idRentar):
    renta = Rentar.query.get_or_404(idRentar)
    if request.method == 'POST':
        renta.estatus = not renta.estatus

        try:
            db.session.commit()
            flash('El estado de la renta ha sido actualizado.', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'Error durante la actualización: {e}', 'danger')

        return redirect(url_for('rentar.listar_rentas'))

    return render_template('actualizar_renta.html', renta=renta)
