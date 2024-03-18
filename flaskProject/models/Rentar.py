from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .Usuarios import db

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, nullable=True, default=5)
    estatus = Column(Boolean, nullable=True, default=False)

    usuario = relationship("Usuario")
    pelicula = relationship("Pelicula")

    def __repr__(self):
        return f"<Rentar(idRentar={self.idRentar}, fecha_renta={self.fecha_renta})>"