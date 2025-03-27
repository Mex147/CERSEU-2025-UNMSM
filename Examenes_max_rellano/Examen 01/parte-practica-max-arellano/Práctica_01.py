# 01
nombre = "Max"
salario = 3550
edad = "28"
compañia = "Chinalco"

if int(edad) >= 30:
    print(f"{nombre}, Usted tiene un bono de 10% en el mes de diciembre")
    print(f"Su salario es : {salario} ")
    print("Bono final es : ",salario ** 2 + 10/100 * salario)
else:
    print(f"{nombre}, Usted tiene un bono de 5% en el mes de diciembre")
    print(f"Su salario es : {salario} ")
    print("Bono final es : ",salario ** 2 + 5 / 100 * salario)