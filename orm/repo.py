import orm.modelos as modelos
from sqlalchemy.orm import Session

#SELECT * FROM app.alumnos
def alumno_lista(sesion:Session):
    print("SELECT * FROM app.alumnos")
    return sesion.query(modelos.Alumno).all()

#SELECT * FROM app.alumnos WHERE id={id_al}
def alumno_id(sesion:Session, id_al:int):
    print(f"SELECT * FROM app.alumnos WHERE id={id_al}")
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_al).first()

#SELECT * FROM app.fotos
def fotos_lista(sesion:Session):
    print("SELECT * FROM app.fotos")
    return sesion.query(modelos.Foto).all()

#SELECT * FROM app.fotos WHERE id={id_fo}
def fotos_id(sesion:Session, id_fo:int):
    print(f"SELECT * FROM app.fotos WHERE id={id_fo}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_fo).first()

#SELECT * FROM app.fotos WHERE id_alumnos={id_al}
def fotos_alumno(sesion:Session, id_al:int):
    print(f"SELECT * FROM app.fotos WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_al).all()

#SELECT * FROM app.calificaciones
def calificaciones_lista(sesion:Session):
    print("SELECT * FROM app.calificaciones")
    return sesion.query(modelos.Calificacion).all()

#SELECT * FROM app.calificaciones WHERE id={id_fo}
def calificaciones_id(sesion:Session, id_fo:int):
    print(f"SELECT * FROM app.calificaciones WHERE id={id_fo}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_fo).all()

#SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_alumno(sesion:Session, id_al:int):
    print(f"SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}")
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_al).all()

#DELETE FROM app.alumnos WHERE id_alumnos={id_al}
def alumno_eliminar(sesion:Session, id_al:int):
    print(f"DELETE FROM app.alumnos WHERE id_alumnos={id_al}")
    alum = alumno_id(sesion, id_al)
    if alum is not None:
        sesion.delete(alum)
        sesion.commit()
    respuesta = {
        "Mensaje":"Alumno eliminado"
    }
    return respuesta

#DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
def calificaciones_eliminar(sesion:Session, id_al:int):
    print(f"DELETE FROM app.calificaciones WHERE id_alumnos={id_al}")
    calif_alum = calificaciones_alumno(sesion, id_al)
    if calif_alum is not None:
        for calif in calif_alum:
            sesion.delete(calif)
        sesion.commit()
    respuesta = {
        "Mensaje":"Calificaciones eliminadas"
    }
    return respuesta

#DELETE FROM app.fotos WHERE id_alumnos={id_al}
def fotos_eliminar(sesion:Session, id_al:int):
    print(f"DELETE FROM app.fotos WHERE id_alumnos={id_al}")
    fotos_alum = fotos_alumno(sesion, id_al)
    if fotos_alum is not None:
        for foto in fotos_alum:
            sesion.delete(foto)
        sesion.commit()
    respuesta = {
        "Mensaje":"Fotos eliminadas"
        }
    return respuesta

#Terminado

