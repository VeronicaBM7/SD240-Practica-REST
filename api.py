from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
from orm.config import generador_sesion
from sqlalchemy.orm import Session
import orm.repo as repo
import shutil
import os
import uuid
import orm.esquemas as esquemas

#Servidor
app = FastAPI()

#Decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }
    return respuesta

#get("/alumnos”)
#alumno_lista
@app.get("/alumnos")
def alumno_lista(sesion:Session=Depends(generador_sesion)):
    print("API Consultando todos los alumnos")
    return repo.alumno_lista(sesion)   

#get("/alumnos/{id})
#alumno_id
@app.get("/alumnos/{id}")
def alumno_id(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Consultando alumno por id: {id}")
    return repo.alumno_id(sesion, id)

#fotos_lista
@app.get("/fotos")
def fotos_lista(sesion: Session = Depends(generador_sesion)):
    print("API Consultando todas las fotos")
    return repo.fotos_lista(sesion)

#get("/fotos/{id}”)
#fotos_id
@app.get("/fotos/{id}")
def fotos_id(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Consultando foto por id: {id}")
    return repo.fotos_id(sesion, id)

#get("/alumnos/{id}/fotos")
#fotos_alumno
@app.get("/alumnos/{id}/fotos")
def fotos_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Consultando fotos de alumno por id: {id}")
    return repo.fotos_alumno(sesion, id)


#calipficaciones_lista
@app.get("/calificaciones")
def calificaciones_lista(sesion: Session = Depends(generador_sesion)):
    print("API Consultando todas las calificaciones")
    return repo.calificaciones_lista(sesion)

#get("/calificaciones/{id}”)
#calificaciones_id
@app.get("/calificaciones/{id}")
def calificaciones_id(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Consultando calificacion por id: {id}")
    return repo.calificaciones_id(sesion, id)

#get("/alumnos/{id}/calificaciones")
#calificaciones_alumno
@app.get("/alumnos/{id}/calificaciones")
def calificaciones_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Consultando calificaciones de alumno por id: {id}")
    return repo.calificaciones_alumno(sesion, id)

#delete("/alumnos/{id})
#alumno_eliminar
@app.delete("/alumnos/{id}")
def alumno_eliminar(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Eliminando alumno por id: {id}")
    repo.calificaciones_eliminar(sesion,id)
    repo.fotos_eliminar(sesion,id)
    repo.alumno_eliminar(sesion, id)
    return {"mensaje:","Alumno eliminado"}

#delete("/calificaciones/{id}”)
#calificaciones_eliminar
@app.delete("/calificaciones/{id}")
def calificaciones_eliminar(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Eliminando calificacion por id: {id}")
    return repo.calificaciones_eliminar(sesion, id)

#delete("/fotos/{id}"")
#fotos_eliminar
@app.delete("/fotos/{id}")
def fotos_eliminar(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Eliminando foto por id: {id}")
    return repo.fotos_eliminar(sesion, id)

#delete("/alumnos/{id}/calificaciones")
@app.delete("/alumnos/{id}/calificaciones")
def calificaciones_alumno_eliminar(id:int, sesion:Session = Depends(generador_sesion)):
    print(f"API Eliminando calificaciones de alumno por id: {id}")
    repo.calificaciones_alumno(sesion, id)

#delete("/alumnos/{id}/fotos")
@app.delete("/alumnos/{id}/fotos")
def fotos_alumno_eliminar(id:int, sesion:Session = Depends(generador_sesion)):
    print(f"API Eliminando fotos de alumno por id: {id}")
    repo.fotos_eliminar(sesion, id)

#post("/alumnos”)
@app.post("/alumnos")
def agregar_alumno(alumno:esquemas.AlumnoBase, sesion:Session = Depends(generador_sesion)):
    print("API Agregando alumno")
    return repo.guardar_alumno(sesion, alumno)

#put("/alumnos/{id})
@app.put("/alumnos/{id}")
def actualizar_alumno(id: int, sesion: Session = Depends(generador_sesion)):
    print(f"API Actualizando alumno por id: {id}")
    return repo.actualizar_alumno(sesion, id)

#post("/alumnos/{id}/calificaciones")
@app.post("/alumnos/{id}/calificaciones")
def agregar_calificacion(id: int, calf:esquemas.CalificacionBase, sesion: Session = Depends(generador_sesion)):
    print(f"API Agregando calificacion de alumno por id: {id}")
    return repo.guardar_calificacion(sesion, id, calf)

#put("/calificaciones/{id}")
@app.put("/calificaciones/{id}")
def actualizar_calificacion(id: int, calf:esquemas.CalificacionBase, sesion: Session = Depends(generador_sesion)):
    print(f"API Actualizando calificacion por id: {id}")
    return repo.actualizar_calificacion(sesion, id, calf)

#post("/alumnos/{id}/fotos")
@app.post("/alumnos/{id}/fotos")
def agregar_foto(id: int, foto:esquemas.FotosBase, sesion: Session = Depends(generador_sesion)):
    print(f"API Agregando foto de alumno por id: {id}")
    return repo.guardar_foto(sesion, id, foto)

#put("/fotos/{id}")
@app.put("/fotos/{id}")
def actualizar_foto(id: int, foto:esquemas.FotosBase, sesion: Session = Depends(generador_sesion)):
    print(f"API Actualizando foto por id: {id}")
    return repo.actualizar_foto(sesion, id, foto)