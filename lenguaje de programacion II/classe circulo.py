
"""import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError()
        self.radio = radio

    def calcular_area(self):
        
        return math.pi * self.radio**2

    def calcular_perimetro(self):
    
        return 2 * math.pi * self.radio

mi_circulo = Circulo(radio=4)

area = mi_circulo.calcular_area()
perimetro = mi_circulo.calcular_perimetro()

print(f"el area del circulo es: {area:.2f}")
print(f"el perímetro del círculo es: {perimetro:.2f}")"""

import math

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self._radio = radio
    
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self._radio = nuevo_radio
    
    def calcular_area(self):
        return math.pi * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

mi_circulo = Circulo(radio=4)

area = mi_circulo.calcular_area()
perimetro = mi_circulo.calcular_perimetro()

print(f"el area del circulo es: {area:.2f}")
print(f"el perímetro del círculo es: {perimetro:.2f}")


print(f"Radio actual: {mi_circulo.radio}")
mi_circulo.radio = 5
print(f"Nuevo radio: {mi_circulo.radio}")
print(f"Nueva área: {mi_circulo.calcular_area():.2f}")
print(f"Nuevo perímetro: {mi_circulo.calcular_perimetro():.2f}")

