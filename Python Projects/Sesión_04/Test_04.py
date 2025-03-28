""""Diccionarios en Python"""

dix_3 = {"nombre" :"MYSQL", "tipo" : "BD relacional"}

#convertir en lista

lista_01 = list(dix_3)
print(f"Mi diccionario convertido es el siguiente: {lista_01}")

lista_02 = list(dix_3.values())
print(lista_02)

keys = list(dix_3.keys())
print(keys)

lista_03 = list(dix_3.items())
print(lista_03)