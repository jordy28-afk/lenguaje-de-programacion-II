import math

class Figura:
    def __init__(self, color):
        self.color = color

    def mostrar_info(self):
        print(f"Color de la figura: {self.color}")


class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def mostrar_info(self):
        print(f"\n|Círculo de radio: {self.radio}, Color: {self.color}|")
        print(f"Área: {self.calcular_area():.2f}\nPerímetro: {self.calcular_perimetro():.2f}")
        super().mostrar_info()


# Prueba del programa
c1 = Circulo(5, "rojo")


c1.mostrar_info()

