"""08. Escribir un programa donde ingresará 8 nombres de países.
Se quiere hacer un clon de la lista, esta copia se le eliminará el primer
y penúltimo valor, mostrar finalmente el tamaño de la lista modificada,
la lista original y todos sus elementos de la lista modificada.
"""
list = ["Perú", "Colombia", "Ecuador", "Argentina", "Brasil", "Japón",]

nova_list = list.copy()

del nova_list[0]
del nova_list[-1]

print("Tamaño de la lista modificada : ",len(nova_list))
print("Lista original : ",list)
print("Nueva lista generada : ",nova_list)