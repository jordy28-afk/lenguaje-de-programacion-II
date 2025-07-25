class rectangulo:
    def __init__(self):
        
        self.longitud = float(input("ingrese la longitudd: "))
        self.ancho = float(input("ngrese el ancho: "))

        self.area = self.longitud * self.ancho
        self.perimetro = 2 * (self.longitud + self.ancho)

        print(f"constructor: rectangulo creado con longitud {self.longitud} y ancho {self.ancho}")

    def mostrar_area(self):
        print(f"el area del rectangulo es: {self.area}")

    def mostrar_perimetro(self):
        print(f"el perimetro del rectangulo es: {self.perimetro}")

    def __del__(self):
        print("destructor: rectangulo eliminado.")

rect = rectangulo()
rect.mostrar_area()
rect.mostrar_perimetro()

