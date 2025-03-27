nombre = "Max"
ciudad = "Huancayo"
saldo = 5000
empresa = False
correo = "arelmax14gmail.com"
empleado = [nombre, saldo, empresa, ciudad]
empleado_d = {'nomb': nombre, "ciud": ciudad, "sald": saldo, "empre": empresa, "corr": correo}

print(f"Tipo de variable de {nombre} es: {type(nombre)}")
print(f"Tipo de variable de {ciudad} es: {type(ciudad)}")
print(f"Tipo de variable de {saldo} es: {type(saldo)}")
print(f"Tipo de variable de {empresa} es: {type(empresa)}")
print(f"Tipo de variable de {correo} es: {type(correo)}")
print(f"Tipo de variable de {empleado} es: {type(empleado)}")
print(f"Tipo de variable de {empleado_d} es: {type(empleado_d)}")