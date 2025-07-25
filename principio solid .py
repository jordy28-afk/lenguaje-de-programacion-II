from abc import ABC, abstractmethod
import math

class Distancia(ABC):
    @abstractmethod
    def calcular(self) -> float:
        pass

class TrianguloRectangulo:
    def __init__(self, cateto1: float, cateto2: float):
        self.cateto1 = cateto1
        self.cateto2 = cateto2

# O, L. Implementación concreta de Distancia usando el teorema de Pitágoras
class Hipotenusa(Distancia):
    def __init__(self, triangulo: TrianguloRectangulo):
        self.triangulo = triangulo

    def calcular(self) -> float:
        a = self.triangulo.cateto1
        b = self.triangulo.cateto2
        return math.sqrt(a ** 2 + b ** 2)

# D. Función de alto nivel que depende de la abstracción 'Distancia'
class Calculadora:
    def __init__(self, estrategia: Distancia):
        self.estrategia = estrategia

    def ejecutar(self) -> float:
        return self.estrategia.calcular()

# -------------------- USO --------------------

if __name__ == "__main__":
    cateto1 = float(input("Ingrese el primer cateto: "))
    cateto2 = float(input("Ingrese el segundo cateto: "))

    triangulo = TrianguloRectangulo(cateto1, cateto2)
    estrategia = Hipotenusa(triangulo)
    calculadora = Calculadora(estrategia)

    resultado = calculadora.ejecutar()
    print(f"La hipotenusa del triángulo es: {resultado:.2f}")
