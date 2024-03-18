from flask import Blueprint, request, render_template, flash, redirect, url_for
from models.Usuarios import Usuario, db
from werkzeug.security import generate_password_hash

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def listar_usuarios():
    all_users = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=all_users)

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        usuario_data = {
            'nombre': request.form.get('nombre'),
            'apPat': request.form.get('apPat'),
            'apMat': request.form.get('apMat'),
            'password': request.form.get('password'),
            'email': request.form.get('email'),
            'superUser': request.form.get('superUser') == 'on'
        }

        if not all(usuario_data.values()):
            flash('Por favor, completa todos los campos para continuar.', 'warning')
            return render_template('agregar_usuario.html')

        usuario_data['password'] = generate_password_hash(usuario_data['password'])
        nuevo_usuario = Usuario(**usuario_data)

        db.session.add(nuevo_usuario)
        try:
            db.session.commit()
            flash('¡Nuevo usuario registrado exitosamente!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Ocurrió un error durante el registro: {e}', 'danger')

        return redirect(url_for('usuario.listar_usuarios'))

    return render_template('agregar_usuario.html')

@usuario_blueprint.route('/editar/<int:idUsuario>', methods=['GET', 'POST'])
def editar_usuario(idUsuario):
    target_usuario = Usuario.query.get_or_404(idUsuario)
    if request.method == 'POST':
        actualizaciones = {
            'nombre': request.form.get('nombre'),
            'apPat': request.form.get('apPat'),
            'apMat': request.form.get('apMat'),
            'email': request.form.get('email'),
            'superUser': request.form.get('superUser') == 'on'
        }

        if new_password := request.form.get('password'):
            actualizaciones['password'] = generate_password_hash(new_password)

        Usuario.query.filter_by(idUsuario=idUsuario).update(actualizaciones)
        try:
            db.session.commit()
            flash('Información del usuario actualizada correctamente.', 'info')
        except Exception as e:
            db.session.rollback()
            flash(f'Actualización fallida: {e}', 'danger')

        return redirect(url_for('usuario.listar_usuarios'))

    return render_template('editar_usuario.html', usuario=target_usuario)

@usuario_blueprint.route('/eliminar/<int:idUsuario>', methods=['POST'])
def eliminar_usuario(idUsuario):
    target_usuario = Usuario.query.get_or_404(idUsuario)
    try:
        db.session.delete(target_usuario)
        db.session.commit()
        flash('Usuario eliminado satisfactoriamente.', 'info')
    except Exception as e:
        db.session.rollback()
        flash(f'No se pudo eliminar el usuario: {e}', 'danger')

    return redirect(url_for('usuario.listar_usuarios'))
