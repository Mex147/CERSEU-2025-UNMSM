"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apeellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
 """

nombre = input("Ingresa tu nombre : ")
apellido = input("Ingresa tu apellido : ")

name_surname = nombre + " " + apellido
print(f"Su nombre y apellido es : {name_surname}")
print(f"el tamaño del nombre y apellido es : {len(name_surname)}")

print(f"Tu nombre y apellido en mayúscula es : {name_surname.upper()}")

if len(nombre) > len(apellido):
    print(f"El tamaño del nombre: {nombre} es mayor al apellido: {apellido}")
else:
    print(f"El tamaño del nombre: {nombre} es menor al apellido: {apellido}")