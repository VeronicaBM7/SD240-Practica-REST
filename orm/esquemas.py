from pydantic import BaseModel

#Definicion del esquema alumno
class AlumnoBase(BaseModel):
    nombre: str
    edad: int
    domicilio: str
    carrera: str
    trimestre: str
    email: str
    password: str

#Definicion del esuquema calificaciones
class CalificacionBase(BaseModel):
    uea: str
    calificacion: str

#Definicion del esquema fotos
class FotosBase(BaseModel):
    titulo: str
    descripcion: str
    ruta: str


