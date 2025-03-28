"""Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura ya
está cancelada” caso contrario “El número de factura no existe” Considerar que
cada vez que se realice algún pago o ingreso de una nueva factura se mostrará
inmediatamente al diccionario actualizado."""

fact_pend = {"00054":"2240.52"}

nueva_fact = input("Ingresar el código de factura cancelada : ")
valor_fact = int(input("Ingresar el monto cancelado : "))

fact_pend[nueva_fact] = valor_fact

print(fact_pend)

codigo = input("Ingresar el código de factura a buscar : ")

if codigo in fact_pend.keys():
    monto = fact_pend[codigo]
    print(f"El monto de la factura {codigo} fue cancelado con {monto} soles.")
else:
    print(f"El número de factura {codigo} no existe.")