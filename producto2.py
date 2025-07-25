class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print("\n--- Información de Producto ---")
        print("Nombre : ", self.nombre)
        print("Precio : ", self.precio)
        print("Stock  : ", self.stock)

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        print("\nPrecio actualizado correctamente")

    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
        print("\nStock actualizado correctamente")

    def aplicar_descuento(self, porcentuaje_descuento):
        descuento = self.precio*(porcentuaje_descuento/100)
        self.precio -= descuento
        print(f"Desceunto del {porcentuaje_descuento}% aplicado. Nuevo precio. S/. {self.precio}")

    def realizar_venta(self, cantidad):
        if cantidad <= self.stock:
            self.stock-= cantidad
            print(f"venta realizada: {cantidad}: unidades vendidas {cantidad * self.precio} " )
            print(f"stock restante para realizar la venta")
        else:
            print("No hay suficiente stock para realizar la venta")

# Crear objetos
producto1 = Producto("Arroz", 3.50, 100)
producto2 = Producto("Azúcar", 4.50, 50)


# Mostrar información
producto1.mostrar_informacion()
producto2.mostrar_informacion()

#aplicar descuento 
producto1.aplicar_descuento(10)
producto1.mostrar_informacion()

#
producto1.realizar_venta(20)
producto1.mostrar_informacion()


producto1.realizar_venta(90)