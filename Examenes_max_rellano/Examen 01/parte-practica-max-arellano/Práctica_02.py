#02


list_01 =  []

nombre = "Max"
apellido = "Arellano"
salario = 3550
edad = "28"
compañia = "Chinalco"
bono = salario ** 2 + 5/100 * salario
work = True

list_01.append(nombre)
print(list_01)
list_01.append(salario)
print(list_01)
list_01.append(edad)
print(list_01)
list_01.append(compañia)
print(list_01)
list_01.append(bono)
print(list_01)
list_01.append(work)
print(list_01)

print("---------------------------------------")
print("El tamaño de la lista nueva es : ",len(list_01))
print(f"El trabajador {nombre} {apellido} se encuentra trabajando actualmente en la compañia {compañia}")
print("---------------------------------------")
list_01.append("0 hijos")
print(list_01)

print("No cumple para obtener el bono familiar")