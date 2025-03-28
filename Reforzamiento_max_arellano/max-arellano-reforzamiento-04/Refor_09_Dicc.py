"""Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a una variable c/u"""

dix_01 = {"nombre": "Max", "apellido" : "Arellano", "salario" : 2044, "edad" : 28}

dix_01["facultad"] = "Ingenieria Eléctrica"

name, fac = dix_01["nombre"], dix_01["facultad"]

print(f"Mi nombre es {name} y soy de la facultad de {fac}")