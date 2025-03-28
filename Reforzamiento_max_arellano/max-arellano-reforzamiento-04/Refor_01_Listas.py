"""Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
este tamaño servirá para ingresar una cantidad X de nombres de alumnos. Ingresarás
los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la lista
que fueron ingresados."""

import time as t

cant_01 = int(input("¿Cuántos alumnos ingresarán a la lista? : "))

alum_list = []

if cant_01 != 0:
    for i in range(cant_01):
        alumno = input(f"Ingrese el nombre del alumno N° {i + 1} : ")
        alum_list.append(alumno)
    print(f"El tamaño de la lista generada es : {cant_01}")
    t.sleep(0.5)
    print(f"La lista generada para {cant_01} alumnos es : {alum_list}")
    t.sleep(.5)
else:
    print(f"El número ingresado no es valido")


