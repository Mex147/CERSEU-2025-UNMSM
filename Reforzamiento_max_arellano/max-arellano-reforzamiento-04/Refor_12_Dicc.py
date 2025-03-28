"""Crear una agenda basada en un diccionario donde los key serán los nombres de las personas
y sus “values” serán los números de teléfono de c/u. Ingresarás por consola el nombre y el número
de cada persona que serán registrados en la agenda. El programa también te permitirá buscar
por nombre en el diccionario en caso no exista mostrar un mensaje de
“No se encuentra registrado en la agenda”
"""

num = int(input("Ingresar el número de personas : "))

agen_dix = {}

if num != 0:
    for i in range(num):
        pers = input(f"Ingrese el nombre de la persona N° {i + 1} : ")
        tel =  int(input(f"Ingrese el número de teléfono de la persona N° {i+ 1 } : "))
        agen_dix[pers] = tel
    print(f"La agenda generada es : {agen_dix}")
else:
    print(f"El número ingresado no es valido")

yn = input("¿Desea buscar un número? -si o no- : ")

if yn == "si":
    i = input("Ingresar el nombre a buscar : ")
    if i in agen_dix.keys():
        print(f"El número de teléfono de la persona {i} es : {agen_dix[i]}")
    else:
        print(f"No se encuentra registrado en la agenda")
else:
    print("Hasta la próxima")