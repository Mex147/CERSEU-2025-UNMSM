"""05. Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas
el penúltimo y antepenúltimo valor (por índice). Reconocer cada uno de los tipos de datos
en esta lista creada y mostrar los resultados en consola.
"""

list = [2.3, 4, True, 8.9, True, .35, False, 56, 12, 78, 32,91.1,15.8]

print("El último valor es : ",list[-1])
print("El penúltimo valor es : ",list[-2])

print("------------------------------------------")
for i in list:
    print(f"El tipo de {i} es : {type(i)}")