class CuentaBancaria:
    def __init__(self):
        self.__titular = input("ingrese el nombre del titular: ")
        self.__saldo = float(input("ingrese el saldo inicial: "))
        print("cuenta creada correctamente.")

    def getters_saldo(self):
        return self.__saldo

    def setters_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("error: el saldo no puede ser negativo.")

    def depositar(self):
        monto = float(input("ingrese el monto a depositar: "))
        if monto > 0:
            self.__saldo += monto
            print("deposito  exitoso.")
        else:
            print("monto invalido.")

    def retirar(self):
        monto = float(input("ingrese monto a retirar: "))
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print("retiro exitoso.")
        else:
            print("error: saldo insuficiente o monto invalido.")

    def mostrar_informacion(self):
        print(f"\nTitular: {self.__titular}")
        print(f"Saldo: {self.__saldo}\n")

def menu():
    cuenta = CuentaBancaria()
    while True:
        print("---|SELECCIONE UNA OPCION|--- ")
        print("|1| depositar dinero + ")
        print("|2| retirar dinero - ")
        print("|3| mostrar información")
        print("|4| salir")

       

        opcion = input("ingrese opcion: ")

        if opcion == "1":
            cuenta.depositar()
        elif opcion == "2":
            cuenta.retirar()
        elif opcion == "3":
            cuenta.mostrar_informacion()
        elif opcion == "4":
            print("Gracias por usar el sistema bancario.")
            break
        else:
            print("opcion invalida. intente de nuevo.")
        
menu()
