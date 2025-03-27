"""09. Crear un programa en Python donde tendrás una lista con 5 departamentos,
ingresarás 2 departamentos adicionales por posición, el cual el segundo
departamento estará en la posición ‘1’ y el primero en penúltimo lugar,
finalmente mostrar la lista original y la lista actualizada en terminal
"""
list = ["Junín", "Cajamarca", "Lima", "Ayacucho", "Arequipa"]

print("Lista original : ",list)
list.insert(1,"Cusco")
list.insert(-1,"Apurimac")
print("Lista modificada :",list)
