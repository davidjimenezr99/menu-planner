from sqlalchemy import Column, Integer, String, Text, Numeric
from .database import Base
from sqlalchemy.dialects.postgresql import ENUM


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    usuario = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(20), nullable=False)
    apellidos = Column(String(30), nullable=True)
    email = Column(String(50), unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    edad = Column(Integer, nullable=False)
    peso = Column(Numeric(5, 2), nullable=False)
    altura = Column(Integer, nullable=False)
    sexo = Column(ENUM("hombre", "mujer", name="sexo_enum"), nullable=False)
