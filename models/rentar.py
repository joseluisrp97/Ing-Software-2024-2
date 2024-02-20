from sqlalchemy import Column, Integer, ForeignKey, DateTime, SmallInteger
from sqlalchemy.orm import relationship
from .usuarios import Base, Usuario
from .peliculas import Pelicula

class Rentar(Base):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(SmallInteger, default=0)

    usuario = relationship("Usuario")
    pelicula = relationship("Pelicula")

    def __repr__(self):
        return f"<Rentar(idRentar={self.idRentar}, fecha_renta={self.fecha_renta})>"
