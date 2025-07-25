"""from typing import List
import math
class calculadora_estad:
    def __init__(self, datos: List[int]):
        self.datos = datos

    def promedio(self) -> float:
        return sum(self.datos) / len(self.datos)

    def maximo(self) -> int:
        return max(self.datos)

    def minimo(self) -> int:
        return min(self.datos)

    def desviacion_estandar(self) -> float:
        media = self.promedio()
        suma_cuadrados = sum((x - media) ** 2 for x in self.datos)
        return math.sqrt(suma_cuadrados / (len(self.datos) - 1))

datos = [10, 20, 15, 25, 30]
calc_ent = calculadora_estad(datos)
print(f"Datos: {datos}")
print(f"Promedio: {calc_ent.promedio():.2f}")
print(f"Máximo: {calc_ent.maximo()}")
print(f"Mínimo: {calc_ent.minimo()}")
print(f"Desviación estándar: {calc_ent.desviacion_estandar():.2f}")"""

from typing import List, TypeVar, Generic
import math

t = TypeVar('t', int, float)

class CalculadoraEstadistica(Generic[t]):
    def __init__(self, datos: List[t]):
        self.datos = datos

    def promedio(self) -> float:
        return sum(self.datos) / len(self.datos)

    def maximo(self) -> t:
        return max(self.datos)

    def minimo(self) -> t:
        return min(self.datos)

    def desviacion_estandar(self) -> float:
        media = self.promedio()
        suma_cuadrados = sum((x - media) ** 2 for x in self.datos)
        return math.sqrt(suma_cuadrados / (len(self.datos) - 1))

datos = [10, 20, 15, 25, 30]

calc_ent = CalculadoraEstadistica[int](datos)

print(f"Datos: {datos}")
print(f"Promedio: {calc_ent.promedio():.2f}")
print(f"Máximo: {calc_ent.maximo()}")
print(f"Mínimo: {calc_ent.minimo()}")
print(f"Desviación estándar: {calc_ent.desviacion_estandar():.2f}")
