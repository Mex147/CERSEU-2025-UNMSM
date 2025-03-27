"""11. Ingresar compañías relacionadas con al mundo de TI, copia los elementos
de la lista en otra lista pero estarán orden inverso, y muestra sus
elementos por la terminal y la lista original también.
"""

list_ti = ["Texas Instruments","Apple", "Microsoft", "SAP", "Oracle"]

copy_list = list_ti.copy()

copy_list.reverse()

print(list_ti)
print(copy_list)