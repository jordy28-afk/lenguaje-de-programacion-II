"""class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    #getters
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_precio(self):
        return self.__precio
    
    #setters
    def establecer_nombre(self, nombre):
        self.__nombre = nombre
    
    def establecer_precio(self, nuevo_precio):
        if nuevo_precio>0:
            self.__precio=nuevo_precio
        self.__precio = nuevo_precio
        print("el nuevo precio es:")
    
    def calcular_precio_con_igv(self):
        return self.__precio * 1.18
    
    def mostrar_info(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Precio con IGV: $. {self.calcular_precio_con_igv():.2f}")

producto = Producto("laptop", 2500)
producto.mostrar_info()
producto.establecer_precio(3000)
producto.mostrar_info()"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

class ProductoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión - Mi Mercado")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")  # Color de fondo azul claro
        
        # Colores
        self.color_azul = "#1e90ff"
        self.color_azul_oscuro = "#0066cc"
        self.color_blanco = "#ffffff"
        
        # Estilo
        self.estilo = ttk.Style()
        self.estilo.configure("TFrame", background=self.color_blanco)
        self.estilo.configure("Header.TLabel", background=self.color_azul, foreground=self.color_blanco, font=("Arial", 14, "bold"), padding=10)
        self.estilo.configure("TButton", background=self.color_azul, foreground=self.color_blanco, font=("Arial", 10, "bold"))
        self.estilo.map("TButton", background=[("active", self.color_azul_oscuro)])
        
        # Lista de productos
        self.productos = []
        
        # Crear componentes
        self.crear_header()
        self.crear_formulario()
        self.crear_tabla_productos()
        self.crear_panel_facturacion()
        
        # Agregar algunos productos de ejemplo
        self.agregar_productos_ejemplo()
    
    def crear_header(self):
        # Frame para el encabezado
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X)
        
        # Logo y nombre
        logo_label = ttk.Label(header_frame, text="MI MERCADO", style="Header.TLabel")
        logo_label.pack(fill=tk.X)
        
        # Menú
        menu_frame = ttk.Frame(self.root, style="TFrame")
        menu_frame.pack(fill=tk.X)
        
        btn_productos = ttk.Button(menu_frame, text="Productos", command=self.mostrar_productos)
        btn_productos.pack(side=tk.LEFT, padx=5, pady=5)
        
        btn_ventas = ttk.Button(menu_frame, text="Ventas", command=self.mostrar_ventas)
        btn_ventas.pack(side=tk.LEFT, padx=5, pady=5)
        
        btn_reportes = ttk.Button(menu_frame, text="Reportes", command=self.mostrar_reportes)
        btn_reportes.pack(side=tk.LEFT, padx=5, pady=5)
    
    def crear_formulario(self):
        # Frame para el formulario
        form_frame = ttk.Frame(self.root, padding=10, style="TFrame")
        form_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Título del formulario
        ttk.Label(form_frame, text="Registro de Productos", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        # Campos del formulario
        ttk.Label(form_frame, text="Nombre:").grid(row=1, column=0, sticky="w", pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.nombre_var, width=30).grid(row=1, column=1, sticky="w", pady=5)
        
        ttk.Label(form_frame, text="Precio:").grid(row=2, column=0, sticky="w", pady=5)
        self.precio_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.precio_var, width=30).grid(row=2, column=1, sticky="w", pady=5)
        
        # Botones
        btn_frame = ttk.Frame(form_frame, style="TFrame")
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Registrar", command=self.registrar_producto).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario).pack(side=tk.LEFT, padx=5)
    
    def crear_tabla_productos(self):
        # Frame para la tabla
        table_frame = ttk.Frame(self.root, padding=10, style="TFrame")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        ttk.Label(table_frame, text="Lista de Productos", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))
        
        # Crear Treeview (tabla)
        self.tabla = ttk.Treeview(table_frame, columns=("id", "nombre", "precio", "igv"), show="headings", height=8)
        
        # Configurar columnas
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("igv", text="Precio + IGV")
        
        self.tabla.column("id", width=50)
        self.tabla.column("nombre", width=200)
        self.tabla.column("precio", width=100)
        self.tabla.column("igv", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        
        # Posicionar tabla y scrollbar
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def crear_panel_facturacion(self):
        # Frame para la facturación
        fact_frame = ttk.Frame(self.root, padding=10, style="TFrame")
        fact_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Título
        ttk.Label(fact_frame, text="Facturación", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        # Subtotal, IGV y Total
        ttk.Label(fact_frame, text="Subtotal:").grid(row=1, column=0, sticky="w", pady=5)
        self.subtotal_var = tk.StringVar(value="S/. 0.00")
        ttk.Label(fact_frame, textvariable=self.subtotal_var).grid(row=1, column=1, sticky="w", pady=5)
        
        ttk.Label(fact_frame, text="IGV (18%):").grid(row=2, column=0, sticky="w", pady=5)
        self.igv_var = tk.StringVar(value="S/. 0.00")
        ttk.Label(fact_frame, textvariable=self.igv_var).grid(row=2, column=1, sticky="w", pady=5)
        
        ttk.Label(fact_frame, text="Total:").grid(row=3, column=0, sticky="w", pady=5)
        self.total_var = tk.StringVar(value="S/. 0.00")
        ttk.Label(fact_frame, textvariable=self.total_var, font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w", pady=5)
        
        # Botón de venta
        ttk.Button(fact_frame, text="Realizar Venta", command=self.realizar_venta).grid(row=4, column=0, columnspan=2, pady=10)
    
    def registrar_producto(self):
        try:
            nombre = self.nombre_var.get().strip()
            precio = float(self.precio_var.get().strip())
            
            if not nombre:
                messagebox.showerror("Error", "El nombre del producto no puede estar vacío")
                return
                
            if precio <= 0:
                messagebox.showerror("Error", "El precio debe ser mayor que cero")
                return
            
            # Crear producto
            producto = Producto(nombre, precio)
            self.productos.append(producto)
            
            # Añadir a la tabla
            precio_igv = producto.calcular_precio_con_igv()
            self.tabla.insert("", "end", values=(len(self.productos), nombre, f"S/. {precio:.2f}", f"S/. {precio_igv:.2f}"))
            
            # Limpiar formulario
            self.limpiar_formulario()
            
            messagebox.showinfo("Éxito", f"Producto '{nombre}' registrado correctamente")
            
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número válido")
    
    def limpiar_formulario(self):
        self.nombre_var.set("")
        self.precio_var.set("")
    
    def agregar_productos_ejemplo(self):
        ejemplos = [
            ("Arroz", 5.50),
            ("Leche", 4.20),
            ("Pan", 1.80),
            ("Manzanas", 6.50),
            ("Pollo", 15.90)
        ]
        
        for i, (nombre, precio) in enumerate(ejemplos, 1):
            producto = Producto(nombre, precio)
            self.productos.append(producto)
            
            precio_igv = producto.calcular_precio_con_igv()
            self.tabla.insert("", "end", values=(i, nombre, f"S/. {precio:.2f}", f"S/. {precio_igv:.2f}"))
        
        self.actualizar_totales()
    
    def actualizar_totales(self):
        subtotal = sum(p.obtener_precio() for p in self.productos)
        igv = subtotal * 0.18
        total = subtotal + igv
        
        self.subtotal_var.set(f"S/. {subtotal:.2f}")
        self.igv_var.set(f"S/. {igv:.2f}")
        self.total_var.set(f"S/. {total:.2f}")
    
    def realizar_venta(self):
        if not self.productos:
            messagebox.showwarning("Advertencia", "No hay productos para vender")
            return
        
        total = sum(p.obtener_precio() for p in self.productos) * 1.18
        messagebox.showinfo("Venta Realizada", f"Venta completada por un total de S/. {total:.2f}")
        
        # Reiniciar
        self.productos = []
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        self.actualizar_totales()
    
    def mostrar_productos(self):
        messagebox.showinfo("Productos", "Mostrando sección de productos")
    
    def mostrar_ventas(self):
        messagebox.showinfo("Ventas", "Mostrando sección de ventas")
    
    def mostrar_reportes(self):
        messagebox.showinfo("Reportes", "Mostrando sección de reportes")

class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    # getters
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_precio(self):
        return self.__precio
    
    # setters
    def establecer_nombre(self, nombre):
        self.__nombre = nombre
    
    def establecer_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            return True
        return False
    
    def calcular_precio_con_igv(self):
        return self.__precio * 1.18
    
    def mostrar_info(self):
        print(f"Producto: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Precio con IGV: $. {self.calcular_precio_con_igv():.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductoApp(root)
    root.mainloop()