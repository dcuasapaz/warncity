from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]
    
@app.get("/")
def index():
    return {"message": "Hola mundo"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"value": id}

@app.post("/libros/")
def insertar_libro(libro: Libro):
    return {"message": "libro {} insertado".format(libro.titulo)}

