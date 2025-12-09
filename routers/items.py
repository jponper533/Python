from fastapi import APIRouter
from pydantic import BaseModel

# creamos un router que gestione las rutas
router = APIRouter()

@router.get("/items")
def get_items():
    items_list = ["Hola"]
    return items_list