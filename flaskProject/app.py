from flask import Flask, render_template
from models.Usuarios import db

from controllers.ControllerUsuario import usuario_blueprint
from controllers.ControllerPelicula import pelicula_blueprint
from controllers.ControllerRenta import rentar_blueprint


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Develooper123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

app.register_blueprint(usuario_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(rentar_blueprint)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)