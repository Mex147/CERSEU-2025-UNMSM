"""04. Crea dos listas (una de datos string y la otra de datos numéricos) para luego
usar los métodos de orden (los elementos tienen que estar desordenados),
mostrar las listas antes y después de aplicarle los métodos de orden
"""
list_str = ["Casa", "Perro", "Gato", "Ratón"]
list_num = [35, 53, 81, 15]

print(f"Mi lista antes de, es : {list_str}")
print(f"Mi lista antes de, es : {list_num}")

list_str.sort()
list_num.sort()

print(f"Mi lista ordenada es : {list_str}")
print(f"Mi lista ordenada es : {list_num}")