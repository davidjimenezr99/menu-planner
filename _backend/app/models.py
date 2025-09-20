from sqlalchemy import Column, Integer, String, Text, Numeric, CheckConstraint, DateTime
from .database import Base
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import func


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
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    __table_args__ = (
        CheckConstraint("edad BETWEEN 14 AND 90", name="chk_usuarios_edad"),
        CheckConstraint("peso BETWEEN 30 AND 200", name="chk_usuarios_peso"),
        CheckConstraint("altura BETWEEN 120 AND 220", name="chk_usuarios_altura"),
        CheckConstraint("email=lower(email)", name="chk_usuarios_email_minusculas"),
        CheckConstraint("usuario=lower(usuario)", name="chk_usuarios_usuario_minusculas"),
    )
