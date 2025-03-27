"""
1. Crear 2 variables enteras, 2 variables flotantes, 1 variable string (solamente caracteres), 1 variable string
con contenido solamente numérico y 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numérica
(realizar conversiones si es necesario)
3. Obtener y mostar la suma de las 2 variables enteras más la variable string numérica y la
variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostarar el resultado entero o la parte entera de las 2 variables int: //
6. Obtener una pontencia usando una de las variables flotantes como base y la variable entera como potencia
"""

var1_int = 300
var2_int = 500
var3_float = 12.5
var4_float =3.5
var5_str = "Max"
var6_str = "200"
var7_bool = True


print("2. var1_int + int(var6_str) es :",var1_int + int(var6_str))
print("3. var1_int + var2_int + int(var6_str) + var3_float es :",var1_int + var2_int + int(var6_str) + var3_float)
print("4. var2_int % var1_int es :",var2_int % var1_int)
print("5. var2_int // var1_int es :",var2_int // var1_int)
print("6. var1_int ** var4_float es :",var1_int ** var4_float)