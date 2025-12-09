from sqlmodel import SQLModel, create_engine, Session

sqllite_fichero = "database.db" #nombre base de datos
sqllite_url = f"sqlite:///{sqllite_fichero}" # URL para acceder a la bd

#crear engine de la bd

engine = create_engine(sqllite_url, echo=True) # echo=true es para depuracion

#creamos las tablas de la base de datos

def crear_tablas():
    SQLModel.metadata.create_all(engine)

#Gestion de la sesion con la base de datos
def get_session():
    with Session(engine) as session:
        yield session