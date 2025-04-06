"""- Crear una clase llamada Empleado donde sus atributos deben ser nombre, edad,
saldo y de nacionalidad peruana, tendrá un método para solicitar su nombre y otro
para solicitar su edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en un año la
edad de la persona.
- Crear la instancia de la clase Persona y usar su nuevo método aumentoSueldo
para incrementar su sueldo en un 30% (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicho sueldo ya incrementado).
- Crear un siguiente método que retorne un mensaje donde indique que:
“En el año 2025 tendrá XX años”, el año se ingresará por parámetro y la edad es la
edad que ya se ingresó (Mostrar por pantalla este valor)"""


class Empleado:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = ""
        self.edad = 0
        self.sueldo = sueldo
        self.nacionalidad = "Peruana"

    def pedir_nombre(self):
        self.nombre = input("Ingresar nombre : ")

    def pedir_edad(self):
        self.edad = int(input("Ingresar su edad : "))

    def cumpleaños(self):
        self.edad = self.edad + 1
        print(f"¡Ha pasado un año {self.nombre} ahora tienes {self.edad} años.")

    def aumento_sueldo(self, porcentaje):
        aumento = self.sueldo * porcentaje / 100
        self.sueldo = self.sueldo + aumento
        print(f"Señor {self.nombre} su sueldo es {self.sueldo:.2f} soles. Recibió un {porcentaje}% de aumento.")

    def edad_futura(self, año_actual, año_futuro):
        pred = (año_futuro - año_actual) + self.edad
        print(f"En el año {año_futuro} el señor {self.nombre} tendrá {pred} años.")


emp1 = Empleado("", 0, 2000)
emp2 = Empleado("", 0, 2500)

for emp in [emp1, emp2]:
    emp.pedir_nombre()
    emp.pedir_edad()
    emp.aumento_sueldo(30)
    emp.aumento_sueldo(30)
    emp.edad_futura(2025, 2030)
    emp.cumpleaños()
    print(f"Señor {emp.nombre} usted tiene {emp.edad} años.")
    emp.cumpleaños()