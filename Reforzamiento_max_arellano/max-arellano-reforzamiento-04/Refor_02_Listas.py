"""Crear un programa en Python donde tendrás una lista con 5 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo departamento que
ingreses sustituirá al primero de la lista."""

departamentos = ["Ayacucho", "Junín", "Apurimac", "Loreto", "Arequipa"]

ant = departamentos.copy()

dep_1 = departamentos.append(input("Ingrese el nuevo departamento para agregar a la lista : "))
departamentos[0] = input("Ingrese un departamento para sustituir al primer valor de la lista : ")

print(f"Mi lista antigua es : {ant}")
print(f"Mi lista antigua es : {departamentos}")