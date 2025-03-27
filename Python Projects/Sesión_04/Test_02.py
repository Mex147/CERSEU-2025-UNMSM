"""Diccionarios en Python"""
"""del :  Elimina una key y su valor del diccionario"""


dix_01 = {"nombre" : "Max", "edad" : 29, "promedio" : 14.9}

dix_01["distrito"] = "El Tambo"

del dix_01["edad"]
del dix_01["promedio"]

print(dix_01)