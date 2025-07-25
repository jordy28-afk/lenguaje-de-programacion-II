"""class rectangulo:
    def __init__(self,altura,base):
        self._altura =altura
        self._base = base

    def calcular_area(self):
        return self._base * self._altura

    def calcular_perimetro(self):
        return 2 * (self._base + self._altura)

mi_rectangulo = rectangulo(altura=5, base=10)

area = mi_rectangulo.calcular_area()
perimetro = mi_rectangulo.calcular_perimetro()

print(f"el area del rectangulo es: {area}")
print(f"el perimetro del rectangulo es: {perimetro}")"""


class Rectangulo:
    def __init__(self, altura, base):
        self._altura = altura
        self._base = base

    def altura(self):
        return self._altura

    def base(self):
        return self._base

    def establecer_altura(self, nueva_altura):
        if nueva_altura > 0:
            self._altura = nueva_altura
        else:
            print()

    def establecer_base(self, nueva_base):
        if nueva_base > 0:
            self._base = nueva_base
        else:
            print()

    def area(self):
        return self._base * self._altura

    def perimetro(self):
        return 2 * (self._base + self._altura)

rect = Rectangulo(5, 10)
print(f"Altura: {rect.altura()}, Base: {rect.base()}")
print(f"Área: {rect.area()}, Perímetro: {rect.perimetro()}")

rect.establecer_altura(7)
rect.establecer_base(12)
print(f"nueva altura: {rect.altura()}, Nueva base: {rect.base()}")
print(f"nueva área: {rect.area()}, Nuevo perímetro: {rect.perimetro()}")