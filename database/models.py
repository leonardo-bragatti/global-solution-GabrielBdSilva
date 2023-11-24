from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer,primary_key=True)
    name = Column(String(512))
    password = Column(String(128))
    email = Column(String(512))
    cpf = Column(Integer)
    phone = Column(Integer)
    birth = Column(String(128))

    triagens = relationship("Triagem", back_populates="users")

class Triagem(Base):
    __tablename__ = "triagem"

    id = Column(Integer, primary_key=True)
    status = Column(String(128))
    symptoms = Column(String(512))
    pain_level = Column(Integer)
    taking_medication = Column(String(512))
    breathing = Column(String(128)) #respiração
    fever = Column(String(128))
    temperature = Column(String(128))
    pressure = Column(String(128))
    user_id = Column(Integer,ForeignKey("usuario.id"))
    users = relationship("Usuario", back_populates="triagens")

class Profissional(Base):
    __tablename__ = "profissional"
    id = Column(Integer,primary_key=True)
    usuario = Column(String(512))
    password = Column(String(512))
