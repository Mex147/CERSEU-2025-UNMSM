"""Crea correctamente un diccionario con los campos de: nombre, edad, salario y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la terminal."""

dix = {"nombre": "Max", "apellido" : "Arellano", "salario" : 2044, "edad" : 28}

print(f"Mi diccionario es : {dix}")

dix_01 = list(dix)

print(f"Las llaves de la lista es :{list(dix.keys())}")
print(f"Las valores de la lista es :{list(dix.values())}")

print(f"Mi diccionario convertido en lista es : {dix_01}")