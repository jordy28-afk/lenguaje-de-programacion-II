from abc import ABC, abstractmethod
from typing import List
# INTERFACES (ISP)
class Calculable(ABC):
    @abstractmethod
    def calcular_total(self) -> float:
        pass

class Imprimible(ABC):
    @abstractmethod
    def imprimir(self):
        pass
# SRP - Representa un cliente
class Cliente:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion
# SRP - Representa un producto
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
# SRP - Representa un ítem en la factura
class ItemFactura:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad
# OCP + LSP - Factura implementa interfaces sin cambiar el código base
class Factura(Calculable, Imprimible):
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.items: List[ItemFactura] = []

    def agregar_item(self, item: ItemFactura):
        self.items.append(item)

    def calcular_total(self) -> float:
        return sum(item.subtotal() for item in self.items)
    def imprimir(self):
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Dirección: {self.cliente.direccion}")
        print("\nDetalle de la factura:")
        for item in self.items:
            print(f"- {item.producto.nombre} x {item.cantidad} = S/ {item.subtotal():.2f}")
        print(f"\nTOTAL A PAGAR: S/ {self.calcular_total():.2f}")
# DIP - Clase de alto nivel que depende de una abstracción (Calculable)
class ProcesadorDePago:
    def __init__(self, calculable: Calculable):
        self.calculable = calculable

    def procesar_pago(self):
        total = self.calculable.calcular_total()
        print(f"\nProcesando pago de S/ {total:.2f}...")


if __name__ == "__main__":
    # Crear cliente
    cliente = Cliente("Anthony Jordy", "Av. Perú 123, Puno")

    # Crear productos
    producto1 = Producto("Laptop", 2500.00)
    producto2 = Producto("Mouse", 75.50)
    producto3 = Producto("USB 32GB", 40.00)

    # Crear factura
    factura = Factura(cliente)
    factura.agregar_item(ItemFactura(producto1, 1))
    factura.agregar_item(ItemFactura(producto2, 2))
    factura.agregar_item(ItemFactura(producto3, 3))

    # Imprimir factura
    factura.imprimir()

    # Procesar pago (DIP)
    procesador = ProcesadorDePago(factura)
    procesador.procesar_pago()
