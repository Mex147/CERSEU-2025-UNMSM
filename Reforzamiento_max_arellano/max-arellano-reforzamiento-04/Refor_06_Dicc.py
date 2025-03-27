"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor del salario y DNI en consola.
También elimina el key edad de tu diccionario, incluyendo su valor. Mostrar finalmente el diccionario actualizado."""

dix = {"nombre": "Max", "apellido" : "Arellano", "salario" : 2044, "edad" : 28}

dix["dni"] = 75209898

print(f"Mi diccionario actualizado es : {dix}")
print("-------------------------------------")
print(f"Mi dni es : {dix["dni"]} y mi edad es : {dix["edad"]}")


print("-------------------------------------")
print(f"Mi diccionario actualizado cuando se elimina la key de edad es :\n{dix}")