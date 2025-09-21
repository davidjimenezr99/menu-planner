from datetime import datetime
from typing import Optional, Literal, Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints, field_validator, ConfigDict

UsuarioStr = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, min_length=5, max_length=20
    ),
]

NombreStr = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, min_length=2, max_length=20
    )
]

ApellidosStr = Annotated[
    str,
    StringConstraints(
        strip_whitespace=True, min_length=2, max_length=30
    )
]

EdadInt = Annotated[int, Field(ge=14, le=90, description="Edad (14-90)")]
PesoDecimal = Annotated[float, Field(ge=30, le=200, description="Peso (30-200)")]
AlturaInt = Annotated[int, Field(ge=120, le=220, description="Altura (120-220)")]
SexoLiteral = Literal["hombre", "mujer"]


class CreacionUsuario(BaseModel):
    usuario: UsuarioStr
    nombre: NombreStr
    apellidos: Optional[ApellidosStr] = None
    email: EmailStr
    password: str
    edad: EdadInt
    sexo: SexoLiteral
    peso: PesoDecimal
    altura: AlturaInt

    @field_validator("usuario", mode="before")
    @classmethod
    def minusculas_usuario(cls, v: str) -> str:
        return v.strip().lower()

    @field_validator("email", mode="before")
    @classmethod
    def minusculas_email(cls, v: str) -> str:
        return v.strip().lower()

    @field_validator("email")
    @classmethod
    def longitud_email(cls, v: EmailStr) -> EmailStr:
        if len(str(v)) > 50:
            raise ValueError("email supera longitud permitida (50)")
        return v


class LoginUsuario(BaseModel):
    usuario_o_email: str
    password: str

    @field_validator("usuario_o_email", mode="before")
    @classmethod
    def email_o_usuario_minusculas(cls, v: str) -> str:
        return v.strip().lower()


class UserOut(BaseModel):
    id: int
    usuario: str
    nombre: str
    apellidos: Optional[str] = None
    email: EmailStr
    peso: float
    altura: int
    edad: int
    sexo: SexoLiteral
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class TokenOut(BaseModel):
    access_token: str
    token_type: Literal["Bearer"] = "Bearer"
