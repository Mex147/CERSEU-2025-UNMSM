"""Tienes una lista con 5 nombres de estudiantes. Crear un programa que te pedirá ingresar el nombre de un estudiante,
la cuál será eliminada de lista inicial en caso que no exista en la lista mostrar un mensaje donde indique que no se
encuentre en la lista y esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola."""

alumnos = ["Alex", "Stefany", "Max", "Elisse", "Gary"]

x = input("Ingrese el nombre de un alumno : ")

if x in alumnos:
    alumnos.remove(x)
    print(f"El alumno {x} fue removido de la lista.")
    print(f"La nueva lista es : {alumnos}")
else:
    alumnos.append(x)
    print(f"El alumno {x} no se encuentra y será agreado a la lista.")
    print(f"La nueva lista es : {alumnos}")
