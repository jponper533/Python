from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

class elemento(BaseModel):
    nombre: str
    precio: int

app = FastAPI()

base_datos = {
    1: {"nombre": "Portatil", "precio": 1000},
    2: {"nombre": "Teclado", "precio": 200},
    3: {"nombre": "Raton", "precio": 100},
    4: {"nombre": "Portatil", "precio": 1000},
    5: {"nombre": "Teclado", "precio": 200},
    6: {"nombre": "Raton", "precio": 100},
    7: {"nombre": "Portatil", "precio": 1000},
    8: {"nombre": "Teclado", "precio": 200},
    9: {"nombre": "Raton", "precio": 100},
    10: {"nombre": "Portatil", "precio": 1000},
}


@app.get("/items")
def items(salto: int, limite: int = 10):
    lista = list(base_datos)
    return lista[salto : salto + limite]

@app.get("/items/{id_items}")
def obtener_item(id_items : int): 
    return base_datos.get(id_items) 
    return base_datos[id_items] 

@app.post("/items")
def crear_items(item: elemento):
    return item