import orm.modelos as modelos
import orm.esquemas as esquemas
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

#POST '/alumnos'
def guardar_alumno(sesion:Session, alm_nuevo:esquemas.AlumnoBase):
    #1.-Crear un nuevo objeto de la clase modelo Alumno
    alm_bd = modelos.Alumno()
    #2.-Llenado de datos
    alm_bd.nombre = alm_nuevo.nombre
    alm_bd.edad = alm_nuevo.edad
    alm_bd.domicilio = alm_nuevo.domicilio
    alm_bd.carrera = alm_nuevo.carrera
    alm_bd.trimestre = alm_nuevo.trimestre
    alm_bd.email = alm_nuevo.email
    alm_bd.password = alm_nuevo.password
    #3.-Insertar el nuevo objeto en la BD
    sesion.add(alm_bd)
    #4.-Guardar los cambios en la BD
    sesion.commit()
    #5.-Refresh
    sesion.refresh(alm_bd)
    return alm_bd

#POST '/alumnos/{id}/calificaciones
def guardar_calificacion(sesion:Session, id_alm:int, calif_nueva:esquemas.CalificacionBase):
    #1.-Verificar que exista el alumno
    alm_bd = alumno_id(sesion, id_alm)
    if alm_bd is not None:
        #2.-Crear un nuevo objeto de la clase modelo Calificacion
        calif_bd = modelos.Calificacion()
        #3.-Llenado de datos
        calif_bd.uea = calif_nueva.uea
        calif_bd.calificacion = calif_nueva.calificacion
        #4.-Insertar el nuevo objeto en la BD
        sesion.add(calif_bd)
        #4.-Guardar los cambios en la BD
        sesion.commit()
        #5.-Refresh
        sesion.refresh(calif_bd)
        return calif_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta

#POST "/alumnos/{id}/fotos"
def guardar_foto(sesion:Session, id_alm:int, foto_nueva:esquemas.FotosBase):
    #1.-Verificar que exista el alumno 
    alm_bd = alumno_id(sesion, id_alm)
    if alm_bd is not None:
        #2.-Crear un nuevo objeto de la clase modelo Fotos
        foto_bd = modelos.Foto()
        #3.-Llenado de datos
        foto_bd.titulo = foto_nueva.titulo
        foto_bd.descripcion = foto_nueva.descripcion
        foto_bd.ruta = foto_nueva.ruta
        #4.-Insertar el nuevo objeto en la BD
        sesion.add(foto_bd)
        #4.-Guardar los cambios en la BD
        sesion.commit()
        #5.-Refresh
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
#PUT app.almnos '/alumno/{id}'
# UPDATE app.usuarios
# SET nombre=alm_esquema.nombre, edad=alm_esquema.edad, 
# domicilio=alm_esquema.domicilio, email=alm_esquema.email,
# password=alm_esquema.password
# WHERE id = id_alumno
def actualizar_alumno(sesion:Session, id_alm:int,alm_esquema:esquemas.AlumnoBase):
    #1.-Verificar que exista el alumno y crear el objeto
    alm_bd = alumno_id(sesion, id_alm)
    if alm_bd is not None:
        #2.- Actualizar los datos
        alm_bd.nombre = alm_esquema.nombre
        alm_bd.edad = alm_esquema.edad
        alm_bd.domicilio = alm_esquema.domicilio
        alm_bd.carrera = alm_esquema.carrera
        alm_bd.trimestre = alm_esquema.trimestre
        alm_bd.email = alm_esquema.email
        alm_bd.password = alm_esquema.password
        #3.-Insertar el nuevo objeto en la BD
        sesion.add(alm_bd)
        #4.-Guardar los cambios en la BD
        sesion.commit()
        #5.-Refresh
        sesion.refresh(alm_bd)
        #6.-Imprimir los datos nuevos
        print(alm_esquema)
        return alm_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
#PUT app.calificaciones '/calificaciones/{id}'
# UPDATE app.calificaciones
# SET uea=cal_esquema.uea, calificacion=cal_esquema.calificacion
# WHERE id = id_calificacion 
def actualizar_calificacion(sesion:Session, id_cal:int,cal_esquema:esquemas.CalificacionBase):
    #1.-Verificar que exista el alumno
    calif_bd = calificaciones_id(sesion, id_cal)
    if calif_bd is not None:
        #2.-Crear un nuevo objeto de la clase modelo Calificacion
        calif_bd = modelos.Calificacion()
        #3.-Actualizar los datos del objeto
        calif_bd.uea = cal_esquema.uea
        calif_bd.calificacion = cal_esquema.calificacion
        #4.-Insertar el nuevo objeto en la BD
        sesion.add(calif_bd)
        #4.-Guardar los cambios en la BD
        sesion.commit()
        #5.-Refresh
        sesion.refresh(calif_bd)
        return calif_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta
    
#PUT app.fotos '/fotos/{id}'
# UPDATE app.fotos
# SET titulo=foto_esquema.uea, descripcion=des_esquema.calificacion, ruta=ruta_esquema.ruta 
# WHERE id = id_alumno
def actualizar_foto(sesion:Session, id_foto:int,foto_esquema:esquemas.FotosBase):
    #1.-Verificar que exista el alumno
    foto_bd = alumno_id(sesion, id_foto)
    if foto_bd is not None:
        #2.-Crear un nuevo objeto de la clase modelo Fotos
        foto_bd = modelos.Foto()
        #3.-Llenado de datos
        foto_bd.titulo = foto_esquema.titulo
        foto_bd.descripcion = foto_esquema.descripcion
        #4.-Insertar el nuevo objeto en la BD
        sesion.add(foto_bd)
        #4.-Guardar los cambios en la BD
        sesion.commit()
        #5.-Refresh
        sesion.refresh(foto_bd)
        return foto_bd
    else:
        respuesta = {"mensaje":"No existe el alumno"}
        return respuesta