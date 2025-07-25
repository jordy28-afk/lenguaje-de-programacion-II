"""import sys
import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()


t1 = TrianguloRectangulo(3, 4)

print(f"Área: {t1.calcular_area()}")
print(f"Hipotenusa: {t1.calcular_hipotenusa()}")
print(f"Perimetro: {t1.calcular_perimetro()}")
print("Tamaño en memoria (bytes):")

tamaño_objeto = sys.getsizeof(t1)
tamaño_base = sys.getsizeof(t1.base)
tamaño_altura = sys.getsizeof(t1.altura)
tammahipo_objeto
tam_area = sys.getsizeof(t1.calcular_area)
tam_perimetro = sys.getsizeof(t1.calcular_perimetro)
tam_class = sys.getsizeof(TrianguloRectangulo)
#imprimir
print(f"Objeto TrianguloRectangulo: {tamaño_objeto} bytes")
print(f"Atributo base: {tamaño_base} bytes")
print(f"Atributo altura: {tamaño_altura} bytes")
print(f"Método calcular_area: {tam_area} bytes")
print(f"Método calcular_perimetro: {tam_perimetro} bytes")
print(f"Clase TrianguloRectangulo: {tam_class} bytes")
print(f"Hipotenusa: {t1.calcular_hipotenusa()} bytes")"""

import sys
import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

# Entrada de datos desde teclado
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Crear objeto
t1 = TrianguloRectangulo(base, altura)

# Calcular valores
area = t1.calcular_area()
hipotenusa = t1.calcular_hipotenusa()
perimetro = t1.calcular_perimetro()

# Mostrar resultados
print(f"\nÁrea: {area:.2f}")
print(f"Hipotenusa: {hipotenusa:.2f}")
print(f"Perímetro: {perimetro:.2f}")
print("\nTamaño en memoria (bytes):")

# Tamaños en memoria
tamaño_objeto = sys.getsizeof(t1)
tamaño_base = sys.getsizeof(t1.base)
tamaño_altura = sys.getsizeof(t1.altura)
tam_area = sys.getsizeof(t1.calcular_area)
tam_hipotenusa = sys.getsizeof(hipotenusa)
tam_perimetro = sys.getsizeof(t1.calcular_perimetro)
tam_class = sys.getsizeof(TrianguloRectangulo)

# Imprimir tamaños
print(f"Objeto TrianguloRectangulo: {tamaño_objeto} bytes")
print(f"Atributo base: {tamaño_base} bytes")
print(f"Atributo altura: {tamaño_altura} bytes")
print(f"Valor hipotenusa: {tam_hipotenusa} bytes")
print(f"Método calcular_area: {tam_area} bytes")
print(f"Método calcular_perimetro: {tam_perimetro} bytes")
print(f"Clase TrianguloRectangulo: {tam_class} bytes")

