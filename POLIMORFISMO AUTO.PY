"""import math

# Clase base
class Figura:
    def _init_(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

    def mostrar_info(self):
        print(f"Figura: {self.__nombre}")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro()}")

# Subclase: Círculo
class Circulo(Figura):
    def _init_(self, radio):
        super()._init_("Círculo")
        self.__radio = radio

    def calcular_area(self):
        return math.pi * self.__radio ** 2

    def calcular_perimetro(self):
        return round(2 * math.pi * self.__radio, 2)

# Subclase: Rectángulo
class Rectangulo(Figura):
    def _init_(self, base, altura):
        super()._init_("Rectángulo")
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return self._base * self._altura

    def calcular_perimetro(self):
        return 2 * (self._base + self._altura)

# Subclase: Triángulo
class Triangulo(Figura):
    def _init_(self, base, altura, lado2, lado3):
        super()._init_("Triángulo")
        self.__base = base
        self.__altura = altura
        self.__lado2 = lado2
        self.__lado3 = lado3

    def calcular_area(self):
        return (self._base * self._altura) / 2

    def calcular_perimetro(self):
        return self._base + self.lado2 + self._lado3


# Subclase: Cuadrado
class Cuadrado(Figura):
    def _init_(self, lado):
        super()._init_("Cuadrado")
        self.__lado = lado

    def calcular_area(self):
        return self.__lado ** 2

    def calcular_perimetro(self):
        return 4 * self.__lado

# Subclase: Trapecio
class Trapecio(Figura):
    def _init_(self, base_mayor, base_menor, altura, lado1, lado2):
        super()._init_("Trapecio")
        self.__base_mayor = base_mayor
        self.__base_menor = base_menor
        self.__altura = altura
        self.__lado1 = lado1
        self.__lado2 = lado2

    def calcular_area(self):
        return ((self._base_mayor + self.base_menor) * self._altura) / 2

    def calcular_perimetro(self):
        return self._base_mayor + self.base_menor + self.lado1 + self._lado2


# Menú principal
def menu():
    lista_figuras = []
    while True:
        print("\n--- SISTEMA DE FIGURAS GEOMÉTRICAS ---")
        print("1. Registrar círculo")
        print("2. Registrar rectángulo")
        print("3. Registrar triángulo")
        print("4. Registrar cuadrado")
        print("5. Registrar trapecio")
        print("6. Mostrar todas las figuras")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                radio = float(input("Ingrese el radio del círculo: "))
                circulo = Circulo(radio)
                lista_figuras.append(circulo)
                print("✔ Círculo registrado.")

            elif opcion == "2":
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                rectangulo = Rectangulo(base, altura)
                lista_figuras.append(rectangulo)
                print("✔ Rectángulo registrado.")

            elif opcion == "3":
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                triangulo = Triangulo(base, altura)
                lista_figuras.append(triangulo)
                print("✔ Triángulo registrado.")

            elif opcion == "4":
                lado = float(input("Ingrese el lado del cuadrado: "))
                cuadrado = Cuadrado(lado)
                lista_figuras.append(cuadrado)
                print("✔ Cuadrado registrado.")

            elif opcion == "5":
                base_mayor = float(input("Ingrese la base mayor del trapecio: "))
                base_menor = float(input("Ingrese la base menor del trapecio: "))
                altura = float(input("Ingrese la altura del trapecio: "))
                trapecio = Trapecio(base_mayor, base_menor, altura)
                lista_figuras.append(trapecio)
                print("✔ Trapecio registrado.")

            elif opcion == "6":
                if not lista_figuras:
                    print("❗ No hay figuras registradas.")
                else:
                    print("\n--- FIGURAS REGISTRADAS ---")
                    for i, figura in enumerate(lista_figuras, 1):
                        print(f"\nFigura #{i}")
                        figura.mostrar_info()

            elif opcion == "7":
                print("¡Hasta luego!")
                break

            else:
                print("❌ Opción inválida. Intenta de nuevo.")

        except ValueError:
            print("❌ Error: ingrese valores numéricos válidos.")

# Ejecutar
if _name_ == "_main_":
    menu()
"""
# Clase base
class Vehiculo:
    def _init_(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def get_tipo(self):
        return "Vehículo"

    def calcular_impuesto(self):
        # Impuesto genérico por defecto
        return 100.0

    def mostrar_info(self):
        print(f"Tipo: {self.get_tipo()}")
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Año: {self._anio}")
        print(f"Impuesto: S/. {self.calcular_impuesto():.2f}")

# Subclase: Auto
class Auto(Vehiculo):
    def _init_(self, marca, modelo, anio, puertas):
        super()._init_(marca, modelo, anio)
        self._puertas = puertas

    def get_tipo(self):
        return "Auto"

    def calcular_impuesto(self):
        return 500 if self._anio >= 2020 else 300

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self._puertas}")

# Subclase: Moto
class Moto(Vehiculo):
    def _init_(self, marca, modelo, anio, tipo_motor):
        super()._init_(marca, modelo, anio)
        self._tipo_motor = tipo_motor

    def get_tipo(self):
        return "Moto"

    def calcular_impuesto(self):
        return self.impuesto_base

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de motor: {self._tipo_motor}")

# Subclase: Camión
class Camion(Vehiculo):
    def _init_(self, marca, modelo, anio, carga_max):
        super()._init_(marca, modelo, anio)
        self._carga_max = carga_max

    def get_tipo(self):
        return "Camión"

    def calcular_impuesto(self):
        return 1000 + self._carga_max * 50

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de carga: {self._carga_max} toneladas")

# Menú principal
def menu():
    lista_vehiculos = []
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE VEHÍCULOS ---")
        print("1. Registrar Auto")
        print("2. Registrar Moto")
        print("3. Registrar Camión")
        print("4. Mostrar todos los vehículos")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                marca = input("Marca : ")
                modelo = input("Modelo : ")
                anio = int(input("Año : "))
                
                auto = Auto(marca, modelo, anio)
                lista_vehiculos.append(auto)
                print(" Auto registrado.")

            elif opcion == "2":
                marca = input("Marca : ")
                modelo = input("Modelo : ")
                anio = int(input("Año : "))
                impuesto_base =float( input("Tipo de motor (2T/4T): "))
                moto = Moto(marca, modelo, anio, impuesto_base)
                lista_vehiculos.append(moto)
                print(" Moto registrada.")

            elif opcion == "3":
                marca = input("Marca del camión: ")
                modelo = input("Modelo del camión: ")
                anio = int(input("Año del camión: "))
                carga_max = float(input("Capacidad de carga (toneladas): "))
                camion = Camion(marca, modelo, anio, carga_max)
                lista_vehiculos.append(camion)
                print(" Camión registrado.")

            elif opcion == "4":
                if not lista_vehiculos:
                    print(" No hay vehículos registrados.")
                else:
                    print("\n--- VEHÍCULOS REGISTRADOS ---")
                    for i, vehiculo in enumerate(lista_vehiculos, 1):
                        print(f"\nVehículo #{i}")
                        vehiculo.mostrar_info()

            elif opcion == "5":
                print("¡Hasta luego!")
                break

            else:
                print(" Opción inválida. Intenta de nuevo.")

        except ValueError:
            print(" Error: ingrese valores válidos.")

# Ejecutar
if __name__ == "_main_":
    menu()
