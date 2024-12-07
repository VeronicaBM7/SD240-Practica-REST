#Configuracion de la conexion a la BD
from sqlalchemy import create_engine
#Sessionmaker permite crear consultas 
from sqlalchemy.orm import sessionmaker
#Calse base para mapear laas tablas de la bd_alumnos
from sqlalchemy.ext.declarative import declarative_base

#1.- Configuracion de la conexion a la bd_alumnos
URL_BASE_DATOS = "postgresql://usuario-ejemplo:12345@localhost:5432/bd_alumnos"
#Conexion mediante el esquema app
engine = create_engine(URL_BASE_DATOS,
                            connect_args={
                                "options": "-csearch_path=app"
                            })

#2.- Clase para crear objetos del tipo session
SessionClass = sessionmaker(engine)
def generador_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()

#3.- Clase base para mapear
BaseClass = declarative_base()


#Terminado