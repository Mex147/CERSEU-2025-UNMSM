"""Crear un diccionario con 6 departamentos en el país.
Borrar cualquier departamento, usando la palabra reservada del.
Actualizar el penúltimo departamento por otro.
Comprobar que no existe este departamento borrado dentro del diccionario."""

dix_dep = {"dep0" : "Apurimac", "dep1" : "Junín", "dep2" : "Arequipa", "dep3" : "Cusco", "dep4" : "Loreto", "dep5" : "Cajamarca"}

del dix_dep["dep3"]
print(f"Mi diccionario actualizado es : {dix_dep}")

dix_dep["dep4"] = "Puno"
print(f"Mi diccionario actualizado es : {dix_dep}")