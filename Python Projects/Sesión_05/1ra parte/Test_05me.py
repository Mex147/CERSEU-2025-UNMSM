"""Uso del 'for'"""

ingenierias = ["Software", "Sistemas", "Industrial", "Química", "Mecánica", "Mecatrónica"]

print("El tamaño de la lista es: {}".format(len(ingenierias)))


for ingenieria in ingenierias:
    print(f"Ingeniería de {ingenieria} tiene el valor de : {ingenierias.index(ingenieria)}")

print("La lista actualizada es: {}".format(ingenierias))