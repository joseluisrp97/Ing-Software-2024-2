from .Usuarios import db
from sqlalchemy import Column, Integer, String

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    genero = Column(String(45), nullable=True)
    duracion = Column(Integer, nullable=True)
    inventario = Column(Integer, nullable=False, default=1)

    def __repr__(self):
        return f"<Pelicula(idPelicula={self.idPelicula}, nombre={self.nombre})>"