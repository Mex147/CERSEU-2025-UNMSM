"""Crear una clase llamada Persona y agregar un atributo saldo a esta clase
(ejercicio anterior).
-Crear un método transferencia y mostrar saldo (mostrará el saldo actual que tiene la persona)
para la clase mencionada
-El método transferencia hace que la clase Empleado que llame al método pueda transferir
la cantidad monto al objeto Empleado2 por consiguiente deberá ir actualizando también el
saldo o monto que tiene el otro empleado en su cuenta cada vez que use el método transferencia
-Comprobar si no se tiene dinero suficiente no se ejecuta la acción e imprimir
“Saldo insuficiente”. Comprobar instanciado la clase realizando una transferencia y
con dos personas."""

class Persona:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self._saldo = saldo

    def saldo(self, valor):
        if valor >= 0:
            self._saldo = valor
        else:
            print("El saldo no puede ser negativo")

    def mostrar_saldo(self):
        return f"Saldo actual de {self.nombre}: S/{self._saldo:.2f}"

    def transferencia(self, monto, otro_empleado):
        if self._saldo >= monto:
            self._saldo -= monto
            otro_empleado.saldo += monto
            return f"Transferencia exitosa. {self.mostrar_saldo()}"
        else:
            return "Saldo insuficiente"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, saldo):
        super().__init__(nombre, saldo)
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = "peruana"


empleado1 = Empleado("Max", 28, 3500, 5021)
empleado2 = Empleado("Elisse", 25, 2210, 3031)


print(empleado1.mostrar_saldo())
print(empleado2.mostrar_saldo())
print(empleado1.transferencia(1500, empleado2))
print(empleado1.mostrar_saldo())
print(empleado2.mostrar_saldo())

print(empleado2.transferencia(5000, empleado1))