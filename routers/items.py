from fastapi import APIRouter, Depends
from pydantic import BaseModel
from database import get_session
from sqlmodel import Session, select
from models import Item


# creamos un router que gestione las rutas
router = APIRouter()

@router.post("/items")
def crear_item(item: Item,db: Session = Depends(get_session)):
    #item me lo da el usuario y db el get_session

    #añado el item a la db+
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

#Listas elementos db

@router.get("/items")
def get_items(db: Session = Depends(get_session)):
    items_list = db.exec(select(Item)).all() #consultar a la db
    return items_list

