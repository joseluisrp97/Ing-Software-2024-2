from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, LargeBinary, Boolean

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(100), nullable=False)
    apMat = Column(String(100), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(500), nullable=True, unique=True)
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Boolean, nullable=True, default=False)


    def __repr__(self):
        return f"<Usuario(idUsuario={self.idUsuario}, nombre={self.nombre})>"