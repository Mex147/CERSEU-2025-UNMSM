"""06. Elimina ahora todos los elementos de la lista creada previamente y mostrar
en consola la lista actualizada agregando tu nombre, apellido paterno, apellido
materno y edad.
"""

list = [2.3, 4, True, 8.9, True, .35, False, 56, 12, 78, 32,91.1,15.8]

print(f"Mi lista es : {list}")

list.clear()

print("Mi lista borrada es : ",list)

list.append("Arellano")
list.append("Huaman")
list.append(28)

print("Mi nueva lista es : ",list)
