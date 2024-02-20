from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, LargeBinary, Boolean

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    password = Column(String(64))
    email = Column(String(500))
    profilePicture = Column(LargeBinary)
    superUser = Column(Boolean)

    def __repr__(self):
        return f"<Usuario(idUsuario={self.idUsuario}, nombre={self.nombre})>"
