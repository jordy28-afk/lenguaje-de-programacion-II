import sys
import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def validar(self):
        # un triangulo es válido si la suma de dos lados es mayor al tercer lado
        return (self.lado1 + self.lado2 > self.lado3 and
                self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1)
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def calcular_area(self):
        # formula de herrn
        s = self.calcular_perimetro() / 2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area

lado1 = float(input("Ingrese el lado |1|: "))
lado2 = float(input("Ingrese el lado |2|: "))
lado3 = float(input("Ingrese el lado |3|: "))

t1 = Triangulo(lado1, lado2, lado3)

if t1.validar():
   
    area = t1.calcular_area()
    perimetro = t1.calcular_perimetro()
    
    # mostrar  el resultados
    print(f"\nÁrea: {area:.2f}")
    print(f"Perímetro: {perimetro:.2f}")
    print("\nTamaño en memoria (bytes):")
    
    tamaño_objeto = sys.getsizeof(t1)
    tamaño_lado1 = sys.getsizeof(t1.lado1)
    tamaño_lado2 = sys.getsizeof(t1.lado2)
    tamaño_lado3 = sys.getsizeof(t1.lado3)
    tam_area = sys.getsizeof(t1.calcular_area)
    tam_perimetro = sys.getsizeof(t1.calcular_perimetro)
    tam_validar = sys.getsizeof(t1.validar)
    tam_class = sys.getsizeof(Triangulo)
    tam_area_valor = sys.getsizeof(area)
    tam_perimetro_valor = sys.getsizeof(perimetro)
    tam_s = sys.getsizeof(s) if 's' in locals() else 0
    
    # tamaños
    print(f"Objeto Triangulo: {tamaño_objeto} bytes")
    print(f"Atributo lado1: {tamaño_lado1} bytes")
    print(f"Atributo lado2: {tamaño_lado2} bytes")
    print(f"Atributo lado3: {tamaño_lado3} bytes")
    print(f"Método calcular_area: {tam_area} bytes")
    print(f"Método calcular_perimetro: {tam_perimetro} bytes")
    print(f"Método validar: {tam_validar} bytes")
    print(f"Clase Triangulo: {tam_class} bytes")
    print(f"Valor área: {tam_area_valor} bytes")
    print(f"Valor perímetro: {tam_perimetro_valor} bytes")
    print(f"Valor semiperímetro s: {tam_s} bytes")
    print(f"Tamaño total: {tamaño_objeto + tamaño_lado1 + tamaño_lado2 + tamaño_lado3 + tam_area + tam_perimetro + tam_validar + tam_class + tam_area_valor + tam_perimetro_valor + tam_s} bytes")
else:
    print("Los lados ingresados no forman un triángulo válido.")
