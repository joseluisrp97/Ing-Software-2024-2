from .usuarios import Base
from sqlalchemy import Column, Integer, String

class Pelicula(Base):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer)

    def __repr__(self):
        return f"<Pelicula(idPelicula={self.idPelicula}, nombre={self.nombre})>"
