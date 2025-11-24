
# Cariables y tipos de datos
nombre: str = "Javi"
ciudad: str = 'Almachar'
edad: int = 19
altura_metros: float = 1.83
es_estudiante: bool = True

if es_estudiante:
    es_estudiante: str = "VERDAD"
else:
    es_estudiante: str = "FALSO"

resultado: str = (f"Mi nombre es {nombre}, tengo {edad} años y mido {altura_metros} metros. Vivo en {ciudad} y es {es_estudiante} que soy un estudiante.")
print(resultado)


# Listas 
tareas: list[str] = ["Estudiar Python", "Hacer la compra"]
numeros: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tareas.append("Lavar al gato")
tareas.remove("Estudiar Python")

print(numeros[5:9])
print(numeros[-5:9]) #no incluye el 5 por el -
print(tareas)

# Diccionarios
puntuaciones: dict[str, int] = {
"ana": 95,
"luis": 88,
"eva": 100
}

print(puntuaciones)
# Un diccionario más complejo, como un JSON
usuario: dict[str, str | int | bool] = {
"id": 101,
"nombre": "Ana",
"es_admin": False
}

print(usuario["id"])

#Condicionales
edad: int = 25
tiene_entrada: bool = True
if edad < 18:
    print("No puedes pasar (menor de edad).")
elif edad >= 18 and tiene_entrada == False:
    print("Puedes pasar, pero necesitas comprar una entrada.")
elif edad >= 65:
    print("Puedes pasar, tienes descuento de jubilado.")
else:
# Esta se ejecuta si edad >= 18 Y tiene_entrada == True
    print("¡Bienvenido! Puedes pasar.")


#Bucles
print()
notas_alumnos: dict[str, int] = {
    "Marcos": 8,
    "Lucía": 4,
    "Carlos": 10,
    "Sara": 6,
    "David": 3
}

for alumno, nota in notas_alumnos.items():
    if nota >= 5:
        print(f"{alumno} ha aprobado con un {nota}.")
    else:
        print(f"{alumno} ha suspendido con un {nota}.")