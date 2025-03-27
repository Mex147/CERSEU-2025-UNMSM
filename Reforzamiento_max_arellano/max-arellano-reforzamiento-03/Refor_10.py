"""10. Tienes una lista con 7 diferentes nombres de BD relacionales.
De la cual 3 BDs estarán repetidas adrede (en posiciones no consecutivas),
sacar la base de datos repetidas uno por valor y le otro por índice.
Finalmente mostrar la lista actualizada en consola."""

lista = ["Cara", "Sello", "Casa", "Maratón", "Cara", "Cara", "Manzana"]

list_uni = list(set(lista))
print("La lista original es : ", lista)
print("La lista actualizada con valores únicos es :", list_uni)

print(f"\nPara la lista de valores únicos : ")
for i in list_uni:
    print(f"El índice para {i}, es : {list_uni.index(i)}")
