"""Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los datos mediante consola
también (5 compañías relacionadas con al mundo de TI) y harás una copia donde adrede agregarás nombres
que estarán repetidos (mediante consola) para que finalmente muestres otra lista donde solo se mostrará
los nombres no repetidos y también la lista inicial"""

cant_01 = int(input("¿Qué tamaño tendrá la lista? : "))

empresas = []

if cant_01 != 0:
    for i in range(cant_01):
        empresa = input(f"Ingrese la empresa N° {i + 1} : ")
        empresas.append(empresa)
    print(f"El tamaño de la lista generada es : {cant_01}")
    print(f"La lista generada para {cant_01} empresas es : {empresas}")
else:
    print(f"El número ingresado no es valido.")

empresas_copy = empresas.copy()
cant_02 = int(input("¿Cuantás empresas nuevas se agregará? : "))
print("---------------------------------------------")

if cant_02 != 0:
    for j in range(cant_02):
        empresa_copy = input(f"Ingrese la nueva empresa N° {j + 1} : ")
        empresas_copy.append(empresa_copy)
    print(f"La nueva lista generada {cant_02} empresa es {empresas_copy}")
else:
    print(f"El número ingresado no es válido.")

print("---------------------------------------------")
print(f"La lista inicial es : {empresas}")
print("---------------------------------------------")
print(f"La lista de valores únicos de la nueva lista es : {set(empresas_copy)}")
