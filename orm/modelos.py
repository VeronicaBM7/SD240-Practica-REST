# Las clases modelo mapean a las tablas
from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float

#Tabla alumnos
class Alumno(BaseClass):
    __tablename__ = "alumnos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    domicilio = Column(String(100))
    carrera = Column(String(100))
    email = Column("email", String(100))
    password = Column(String(100))
    fecha_registro = Column(DateTime(timezone=True), default=DateTime.datatime.now)

#Tabla calificaciones
class Calificacion(BaseClass):
    __tablename__ = "calificaciones"
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id"))
    uea = Column(String(100))
    calificacion = Column(String(100))

#Tabla fotos
class Foto(BaseClass):
    __tablename__ = "fotos"
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id"))
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(100))

#Terminado