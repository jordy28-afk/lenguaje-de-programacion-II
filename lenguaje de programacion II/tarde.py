import sys
import math

class Pitagoras:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def calcular_hipotenusa(self):
        return math.sqrt(self.c1**2 + self.c2**2)

t1 = Pitagoras(3, 4)

print(f"Hipotenusa: {t1.calcular_hipotenusa()}")
print("Tamaño en memoria (bytes):")

tamaño_objeto = sys.getsizeof(t1)
tamaño_objeto1 = sys.getsizeof(t1.c1)
tamaño_objeto2 = sys.getsizeof(t1.c2)
tam_tamaño = sys.getsizeof(t1.calcular_hipotenusa)
tam_tamaño_class = sys.getsizeof(Pitagoras)

print(f"Objeto triangulo: {tamaño_objeto} bytes")
print(f"Objeto c1: {tamaño_objeto1} bytes")
print(f"Objeto c2: {tamaño_objeto2} bytes")
print(f"Método calcular_hipotenusa: {tam_tamaño} bytes")
print(f"Clase Pitagoras: {tam_tamaño_class} bytes")
