"""Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."""

dix_01 = {"nombre": "Max", "apellido" : "Arellano", "salario" : 2044, "edad" : 28}

list_dix = list(dix_01)
print(list_dix)

for i in dix_01.values():
    print(f"El tipo de los valores para {i} de mi lista es : {type(i)}")