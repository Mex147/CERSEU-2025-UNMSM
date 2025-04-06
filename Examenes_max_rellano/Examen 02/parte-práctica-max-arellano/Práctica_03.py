"""El programa deberá considerar 2 cuentas bancarias para el constructor: 1 en soles y otra en dólares.
Considerar el nombre y apellido del titular
-Deberá tener un método para transferir entre sus cuentas, pero para realizar esto debe hacer una
conversión de monedas.
-Tendrá otro método para retirar dinero, esto debe actualizar ambas cuentas y mostrar en pantalla
los montos actualizados, a su vez validar si tiene fondos suficientes o no para el retiro, mostrar
un mensaje que indique no tiene suficientes en caso fuera el caso.
-Instanciar 3 veces los casos de transferencias para ver reflejado el uso de tus métodos creados."""

class BilleteraElectronica:
    def __init__(self, nombre_tit, apellido_tit, saldo_sol, saldo_dol):
        self.nombre_titular = nombre_tit
        self.apellido_titular = apellido_tit
        self.saldo_sol = saldo_sol
        self.saldo_dol = saldo_dol
        self.tipo_cambio = 3.8

    def transferir_entre_cuentas(self, monto, cuenta_1, cuenta_2):
        if cuenta_1 == "soles" and cuenta_2 == "dolares":
            if self.saldo_sol >= monto:
                self.saldo_sol = self.saldo_sol - monto
                self.saldo_dol = self.saldo_dol + monto/self.tipo_cambio
                return "La transferencia se realizó con éxito."
            else:
                return "Saldo en soles insuficiente"

        elif cuenta_1 == "dolares" and cuenta_2 == "soles":
            if self.saldo_dol >= monto:
                self.saldo_dol = self.saldo_dol - monto
                self.saldo_sol = self.saldo_sol + monto * self.tipo_cambio
                return "La transferencia se realizó con éxito."
            else:
                return "Saldo en dólares insuficiente"
        else:
            return "Operación no válida"

    def retirar_dinero(self, monto, moneda):
        if moneda == "soles":
            if self.saldo_sol >= monto:
                self.saldo_sol = self.saldo_sol - monto
                return f"Retiro exitoso. Nuevo saldo en soles: S/{self.saldo_sol:.2f}"
            else:
                return "Fondos insuficientes en cuenta de soles"
        elif moneda == "dolares":
            if self.saldo_dol >= monto:
                self.saldo_dol = self.saldo_dol - monto
                return f"Retiro exitoso. Nuevo saldo en dólares: ${self.saldo_dol:.2f}"
            else:
                return "Fondos insuficientes en cuenta de dólares"
        else:
            return "Moneda no válida"

    def mostrar_saldos(self):
        return f"Saldo en soles: S/{self.saldo_sol:.2f}, Saldo en dólares: ${self.saldo_dol:.2f}"


cuenta1_persona = BilleteraElectronica("Max", "Arel", 2000, 3150)
cuenta2_persona = BilleteraElectronica("Elisse", "Cárndenas", 5020, 254)
cuenta3_persona = BilleteraElectronica("Juan", "Velasquez", 150, 30)

print("\nBilletera 1:")
print(cuenta1_persona.mostrar_saldos())
print(cuenta1_persona.transferir_entre_cuentas(101, "soles", "dolares"))
print(cuenta1_persona.mostrar_saldos())

print("\nBilletera 2:")
print(cuenta2_persona.mostrar_saldos())
print(cuenta2_persona.transferir_entre_cuentas(502, "dolares", "soles"))
print(cuenta2_persona.mostrar_saldos())

print("\nBilletera 3:")
print(cuenta3_persona.mostrar_saldos())
print(cuenta3_persona.retirar_dinero(20, "soles"))
print(cuenta3_persona.mostrar_saldos())