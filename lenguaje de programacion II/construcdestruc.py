class Suma:
    def __init__(self):
        self.a = int(input("ingrese el valor de a "  ))
        self.b = int(input("ingrese el valor de b "  ))
        self.resultado = self.a + self.b
        print(f"Constructor: Se creo la suma de {self.a} + {self.b} = {self.resultado}")
    
    def mostrar_resultado(self):
        print(f"El resultado de la suma es: {self.resultado}")

    def __del__(self):
        print(f"Destructor: Se elimino la suma de {self.a} + {self.b}")

suma = Suma()
suma.mostrar_resultado()
suma.__del__()