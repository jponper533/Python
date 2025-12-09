from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


from database import crear_tablas #poner funcion para crear la bd y la tabla


from routers import items

app = FastAPI()

#crear la bse de datos al iniciar la app
@app.on_event("startup")
def on_startup():
    crear_tablas() #se ejecuta al iniciar la app


#incluir el gestor de rutas de la api
app.include_router(items.router)
# @app.post("/items")
# def crear_items():
#     return item