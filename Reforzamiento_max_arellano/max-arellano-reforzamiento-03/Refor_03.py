"""03. Crea una siguiente lista vacía y
agregue ítems a partir de variables (los cuales tendrán los siguientes
tipos de datos: 3 floats, 3 ints y 3 strings) (append).
Sumar las dos listas creadas anteriormente y mostrar el resultado
en consola.
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

curso_del = cursos[2]
del cursos[2]

print(cursos)

num_list = []

num_list.append(3.12)
num_list.append(4.5)
num_list.append(1.73)
num_list.append(5)
num_list.append(10)
num_list.append(11)
num_list.append("Casa")
num_list.append("Gato")
num_list.append("Perro")

print((num_list))

print("La suma de cursos y num_list es: ",num_list + cursos)