"""if ternarios"""

"""
Requisitos: 
 - Ingresar por teclado el sueldo de un empleado
 - Si el sueldo es mayor a 2500 y menor a 3500, imprimir "Su sueldo no tiene bonificación"
 y se le agregará el 10%, para luego mostrar el sueldo final con la bonificación
 - Caso contrario: "Su sueldo tiene bonificación este año y será de: 
 'sueldo_final'", sueldo_final= sueldo + 2% sueldo
"""

sueldo = int(input("Ingrese el sueldo del empleado : "))

if 2500 < sueldo < 3500:
    print("Su sueldo no tiene bonificación. 😂")
    sueldo_fin = sueldo * 1.1
    print(f"Su sueldo es de : {sueldo} y su sueldo final es de : {sueldo_fin:.2f} soles.")
else:
    sueldo_final = sueldo + 2/100 * sueldo
    print(f"Su sueldo tiene una bonificación este año y será de : {sueldo_final:.2f} soles.")