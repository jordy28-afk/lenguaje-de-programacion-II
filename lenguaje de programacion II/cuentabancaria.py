
class cuentabancaria:
    def __init__(self, titular, saldo_inicial):
        self._titular = titular
        self._saldo_inicial = saldo_inicial

    def consultar_saldo(self):
        print(f"saldo actual de {self._titular}: $ {self._saldo_inicial:.2f}")

    def depositar(self, monto):
        if monto > 0:
            self._saldo_inicial += monto
            print(f"deposito de $ {monto:.2f} realizado con exito")
        else:
            print("el monto ingresado debe ser positivo")

    def retirar_dinero(self, monto):
        if 0 < monto <= self._saldo_inicial:
            self._saldo_inicial -= monto  
            print(f"retiro de $ {monto:.2f} realizado con exito")
        else:
            print("fondos insuficientes o monto invalido")


cuenta = cuentabancaria("raul", 500.00)
cuenta.consultar_saldo()

cuenta.depositar(150)
cuenta.consultar_saldo()

cuenta.retirar_dinero(100)  
cuenta.consultar_saldo()

cuenta.depositar(-50)
cuenta.retirar_dinero(1000)