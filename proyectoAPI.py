from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# ejercicio1
@app.get("/greet/{name}")
def nombre(name: str):
    return "message:" f"Hola, {name}"
    pass

# ejercicio2
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    return "product_id:" f"{product_id}", "in_stock:" " True"
    pass

@app.get("/prices/{prices}")
async def get_product(prices: float):
    return "original:" f"{prices}", "formatted:" f"${prices:.2f}"
    pass

# ejercicio3

@app.get("/users/me")
async def read_current_user():
    return {"user_id": "usuario_actual"}

@app.get("/users/admin")
async def read_admin():
    return {"user_id": "administrador"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


## Pregunta 1: nos pondra como user_id "me" alhaberlo puesto en la url
## Pregunta 2: ocurre lo mismo que en la pregunta una pero con admin
## Preguunta 3: asi ordenado al poner las rutas anteriores nos da su respectivo user_id


#Ejercicio 4

# Crea un Enum llamado Category con estos valores:
# - electronics
# - books
# - clothing
# - food

class Category(str, Enum):
        electronics = "electronics"
        books = "books"
        clothing = "clothing"
        food = "food"

@app.get("/categories/{category_name}")
async def get_category(category_name: Category):
    if category_name == Category.electronics:
        return "Productos tecnologicos"
    if category_name == Category.books:
        return "Libros y literatura"
    if category_name == Category.clothing:
        return "Ropa y moda"
    if category_name == Category.food:
        return "Alimentos y bebidas"

    # Devuelve diferentes mensajes según la categoría
    # electronics → "Productos tecnológicos"
    # books → "Libros y literatura"
    # clothing → "Ropa y moda"
    # food → "Alimentos y bebidas"
    pass
