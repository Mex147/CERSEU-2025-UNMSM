"""01. Agregar 5 Objetos nuevos a tu lista (append) y quitar 2 elementos de esta lista por valor.
Mostrar la lista final en la terminal.
Obtén también la cantidad total ítems que tienes en tu lista ya creada para agregar este
valor a tu lista y mostrar también el resultado final de cantidad total de elemento
y la lista actualizada en consola.
"""

list_01 = []

list_01.append(1)
list_01.append(4)
list_01.append(32)
list_01.append(98)
list_01.append(12)

print(f"Mi nueva lista : {list_01}")
print("La cantidad de elementos es : ",len(list_01))


del list_01[4]
del list_01[3]
print(f"La nueva lista después de borrar 2 es : {list_01}")
print("La nueva cantidad de elementos es : ",len(list_01))