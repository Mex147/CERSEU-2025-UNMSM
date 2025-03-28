"""Realizar un programa donde se ingresarán por consola
los nombres de los alumnos (indicar previamente la cantidad
de alumnos a ingresar) de un curso y las notas de c/u.
Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a “Pedro tiene la nota de 15”
y también la media de todas las notas."""

alm_01 = int(input("¿Cuántos alumnos ingresarán a la lista? : "))

alum_dix = {}

if alm_01 != 0:
    for i in range(alm_01):
        alumno = input(f"Ingrese el nombre del alumno N° {i + 1} : ")
        nota =  int(input(f"Ingrese la nota del alumno N° {i+ 1 } : "))
        alum_dix[alumno] = nota
    print(f"el diccionario de alumnos y sus notas es : {alum_dix}")
else:
    print(f"El número ingresado no es valido")

for i in alum_dix:
    print(f"{i} tiene la nota de {alum_dix[i]}")

med = sum(alum_dix.values())/len(alum_dix)
print(f"El promedio de notas es {med}")
