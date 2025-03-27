"""Requisitos

- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado (input)
- Distrito de residencia y su sueldo actual (inputs)
- Sueldo y calculo del bono final del año, que será el triple del sueldo mensualmenos el 10% del sueldo
- Todos estos datos van a ingresar en un diccionario
- Asignar a 3 variables usando asignación múltiple los valores del diccionario
- Mostrar por la terminal el mensaje de: "'Nombre' 'apellido', recibirá 'bono' soles de bono de fin de año"

"""
#Creación de diccionario vacío
dix_01 = {}
#Solicitar datos
name = input("Ingrese su nombre : ")
surname = input("Ingrese su apeliido paterno : ")
residencia = input("Ingrese su distrito de residencia : ")
sueldo = int(input("Ingrese su sueldo mensual : "))

#Cálculo del bono final
bono_final = 3 * sueldo - 10/100 * sueldo

dix_01["nombre"] = name
dix_01["apellido paterno"] = surname
dix_01["residencia"] = residencia
dix_01["sueldo"] = sueldo
dix_01["bono final"] = bono_final

print("--------------------------------------------")
#Diccionario creado
print(f"Mi nuevo diccionario es : {dix_01}")
print("--------------------------------------------")
#Asiganción multiple de variables
name_01, surname_01, residencia_01 = dix_01["nombre"], dix_01["apellido paterno"], dix_01["residencia"]
print(f"Mi asignación multiple es : {name_01}, {surname_01}, {residencia_01}")
print("--------------------------------------------")
print(f"{name} {surname} recibirá {bono_final} soles de fin de año.")
