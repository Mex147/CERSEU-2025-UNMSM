""""Diccionarios en Python"""
"""Los nombres de las key irán siempre en minusculas
   sin tildes (por convención o por buenas prácticas)"""

dix_01 = {"nombre" : "Max", "edad" : 29, "promedio" : 14.9}

print(f"Mi diccionario tiene el siguiente contenido : {dix_01}")

dix_01["distrito"] = "El Tambo"
dix_01["nombre"] = "Max"
dix_01["habilitado"] = True


print(f"Mi nuevo diccionario tiene el siguiente contenido : {dix_01}")

nombre = dix_01["nombre"]