"""from typing import TypeVar, Generic

T = TypeVar("T", int, float)

class OperacionMatematica(Generic[T]):
    def calculate(self, a: T, b: T) -> T:
        raise NotImplementedError("Método calcular() no implementado")

class Suma(OperacionMatematica[T]):
    def calculate(self, a: T, b: T) -> T:
        return a + b

def main():
    operacion = Suma()
    num1 = 5
    num2 = 7
    resultado = operacion.calculate(num1, num2)
    print(f"La suma de {num1} + {num2} es {resultado}")
ConnectionAbortedError  ()"""

"""from typing import TypeVar, Generic
import math

T = TypeVar("T", int, float)

class OperacionMatematica(Generic[T]):
    def calculate(self, a: T, b: T) -> T:
        raise NotImplementedError("Método calculate() no implementado")



class Pitagoras(OperacionMatematica[T]):
    def calculate(self, a: T, b: T) -> T:
        return math.sqrt(a**2 + b**2)

def main():

    operacion_pitagoras = Pitagoras()
    cateto1 = 3
    cateto2 = 4
    hipotenusa = operacion_pitagoras.calculate(cateto1, cateto2)
    print(f"La hipotenusa para catetos {cateto1} y {cateto2} es {hipotenusa}")
    
    cateto3 = 5.5
    cateto4 = 7.9
    hipotenusa2 = operacion_pitagoras.calculate(cateto3, cateto4)
    print(f"La hipotenusa para catetos {cateto3} y {cateto4} es {hipotenusa2}")

if __name__ == "__main__":
    main()"""
from typing import TypeVar, Generic

T = TypeVar("T", int, float)

class OperacionMatematica(Generic[T]):
    def calculate(self, a: T, b: T) -> T:
        raise NotImplementedError("Método calculate() no implementado")

class Factorial(OperacionMatematica[T]):
    def calculate(self, a: T, b: T = None) -> T:
        n = int(a) 
        if n < 0:
            raise ValueError()
        r = 1
        for i in range(1, n + 1):
            r *= i
        return r

def main():
    facto = Factorial()
    
    num1 = 5
    resultado = facto.calculate(num1)
    print(f"El factorial de {num1} es {resultado}")
    
    num2 = -3
    resultado2 = facto.calculate(num2)
    print(f"El factorial de {num2} es {resultado2}")

if __name__ == "__main__":
    main()