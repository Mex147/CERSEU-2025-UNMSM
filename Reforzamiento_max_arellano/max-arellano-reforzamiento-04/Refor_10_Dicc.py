"""Ingresar por consola 4 números mediante consola,
crear un diccionario donde los ‘key’ serán los números
indicados y los valores serán los cubos de las estos keys.
Mostrar finalmente este diccionario."""

dix_02 = {}

a = int(input("Ingrese un número : "))
b = int(input("Ingrese un número : "))
c = int(input("Ingrese un número : "))
d = int(input("Ingrese un número : "))

dix_02[a] = a**3
dix_02[b] = b**3
dix_02[c] = c**3
dix_02[d] = d**3

print(f"Mi diccionario es : {dix_02}")