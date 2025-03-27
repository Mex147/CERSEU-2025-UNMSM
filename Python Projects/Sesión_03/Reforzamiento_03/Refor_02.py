"""02 .Devuelve la cantidad de veces que se repite un curso que hayas
llevado en pregrado (agregarlos previamente a la lista con un mínimo de 5 cursos)
luego mostrarla, finalmente elimina el
segundo ítem de la lista usando debidamente su índice
y mostrar en consola tu lista actualizada
"""

cursos = []

cursos.append("Circuitos eléctricos II")
cursos.append("Circuitos eléctricos II")
cursos.append("Programación")
cursos.append("Estadística")
cursos.append("Coordinación de protecciones")
cursos.append("Sistemas digitales")
cursos.append("Programación I")
cursos.append("Programación II")

print(f"Cursos de Pregrado : {cursos}")
print(f"Cursos repetidos de Pregrado : {cursos.count("Circuitos eléctricos II")}")


curso_del = cursos[2]
del cursos[2]

print(f"Curso eliminado : {curso_del}")
print(f"Cursos de Pregrado actualizado : {cursos}")
