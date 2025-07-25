import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from PIL import Image, ImageTk
import random

class Producto:
    def __init__(self, nombre, precio, stock, unidad_medida):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.unidad_medida = unidad_medida
    
    def mostrar_informacion(self):
        info = f"Nombre: {self.nombre}\nPrecio: S/. {self.precio:.2f} / {self.unidad_medida}\nStock: {self.stock} {self.unidad_medida}"
        return info
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        return "Precio actualizado correctamente"
    
    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
        return "Stock actualizado correctamente"
    
    def actualizar_unidad_medida(self, nueva_unidad):
        self.unidad_medida = nueva_unidad
        return "Unidad de medida actualizada correctamente"

class SistemaMercado:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Productos - Mi Mercado")
        self.root.geometry("1200x680")
        self.root.configure(bg="#FF9671")  # Fondo naranja melocotón
        self.root.resizable(True, True)
        
        # Lista de productos
        self.productos = []
        
        # Inicializar algunos productos de ejemplo
        self.productos.append(Producto("Arroz", 3.50, 100, "kg"))
        self.productos.append(Producto("Azúcar", 4.50, 50, "kg"))
        self.productos.append(Producto("Aceite", 8.00, 100, "L"))
        self.productos.append(Producto("Leche", 3.50, 100, "L"))
        
        # Lista de unidades de medida comunes
        self.unidades_medida = ["kg", "g", "L", "ml", "unidad(es)", "paquete(s)", "caja(s)", "botella(s)", "lata(s)"]
        
        # Colores para la interfaz
        self.colores = {
            "fondo_principal": "#FF9671",  # Naranja melocotón
            "fondo_panels": "#FFC75F",     # Amarillo mostaza
            "botones_principal": "#845EC2", # Púrpura
            "botones_secundario": "#F9F871", # Amarillo limón
            "texto_oscuro": "#2C73D2",      # Azul marino
            "texto_claro": "#FFFFFF",      # Blanco
            "destacado": "#008F7A",       # Verde azulado
            "bordes": "#4B4453"           # Gris oscuro
        }
        
        # Crear estilos para ttk
        self.configurar_estilos()
        
        # Crear componentes de la interfaz
        self.crear_interfaz()
    
    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Estilo para los botones principales
        style.configure("Principal.TButton", 
                      background=self.colores["botones_principal"], 
                      foreground=self.colores["texto_claro"],
                      font=("Arial", 11, "bold"),
                      borderwidth=1)
        style.map("Principal.TButton",
                background=[('active', "#6A4FB3")])  # Púrpura más oscuro
        
        # Estilo para los botones secundarios
        style.configure("Secundario.TButton", 
                      background=self.colores["botones_secundario"], 
                      foreground=self.colores["texto_oscuro"],
                      font=("Arial", 10, "bold"),
                      borderwidth=1)
        style.map("Secundario.TButton",
                background=[('active', "#EBE96A")])  # Amarillo más oscuro
        
        # Estilo para las entradas
        style.configure("TEntry", 
                      fieldbackground="white",
                      font=("Arial", 11))
        
        # Estilo para las etiquetas
        style.configure("TLabel", 
                      background=self.colores["fondo_panels"],
                      foreground=self.colores["texto_oscuro"],
                      font=("Arial", 11, "bold"))
        
        # Estilo para etiquetas de título
        style.configure("Titulo.TLabel", 
                      background=self.colores["fondo_panels"],
                      foreground=self.colores["texto_oscuro"],
                      font=("Arial", 16, "bold"))
        
        # Estilo para el treeview
        style.configure("Treeview", 
                      background="white",
                      foreground=self.colores["texto_oscuro"],
                      rowheight=30,
                      fieldbackground="white",
                      font=("Arial", 10))
        style.map("Treeview",
                background=[('selected', self.colores["destacado"])])
        style.configure("Treeview.Heading", 
                      background=self.colores["destacado"],
                      foreground=self.colores["texto_claro"],
                      font=("Arial", 11, "bold"))
        
        # Estilo para el combobox
        style.configure("TCombobox", 
                      background="white",
                      foreground=self.colores["texto_oscuro"],
                      fieldbackground="white",
                      font=("Arial", 11))
    
    def crear_interfaz(self):
        # Crear marco principal para la navegación
        self.frame_titulo = tk.Frame(self.root, bg=self.colores["fondo_panels"], 
                                   padx=10, pady=10, 
                                   highlightbackground=self.colores["bordes"],
                                   highlightthickness=2)
        self.frame_titulo.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(self.frame_titulo, text="SISTEMA DE GESTIÓN - MI MERCADO", 
                style="Titulo.TLabel").pack(side=tk.LEFT, padx=20)
        
        # Botones de navegación
        self.btn_productos = ttk.Button(self.frame_titulo, text="Productos", 
                                      style="Principal.TButton",
                                      command=self.mostrar_productos)
        self.btn_productos.pack(side=tk.RIGHT, padx=5)
        
        self.btn_ventas = ttk.Button(self.frame_titulo, text="Ventas", 
                                   style="Principal.TButton",
                                   command=self.mostrar_ventas)
        self.btn_ventas.pack(side=tk.RIGHT, padx=5)
        
        self.btn_estadisticas = ttk.Button(self.frame_titulo, text="Estadísticas", 
                                         style="Principal.TButton",
                                         command=self.mostrar_estadisticas)
        self.btn_estadisticas.pack(side=tk.RIGHT, padx=5)
        
        # Crear panel principal que cambiará según la navegación
        self.panel_principal = tk.Frame(self.root, bg=self.colores["fondo_principal"], 
                                      padx=10, pady=10)
        self.panel_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Mostrar por defecto la sección de productos
        self.mostrar_productos()
    
    def limpiar_panel_principal(self):
        # Eliminar todos los widgets del panel principal
        for widget in self.panel_principal.winfo_children():
            widget.destroy()
    
    def mostrar_productos(self):
        self.limpiar_panel_principal()
        
        # Dividir en dos paneles
        panel_izquierdo = tk.Frame(self.panel_principal, bg=self.colores["fondo_panels"], 
                                 padx=15, pady=15, 
                                 highlightbackground=self.colores["bordes"],
                                 highlightthickness=2)
        panel_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        
        panel_derecho = tk.Frame(self.panel_principal, bg=self.colores["fondo_panels"], 
                               padx=15, pady=15, 
                               highlightbackground=self.colores["bordes"],
                               highlightthickness=2)
        panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Panel izquierdo - Formulario de productos
        ttk.Label(panel_izquierdo, text="AGREGAR PRODUCTO", style="Titulo.TLabel").pack(pady=10)
        
        frame_form = tk.Frame(panel_izquierdo, bg=self.colores["fondo_panels"])
        frame_form.pack(fill=tk.X, pady=10)
        
        # Nombre
        ttk.Label(frame_form, text="Nombre del Producto:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.entry_nombre = ttk.Entry(frame_form, width=25)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        # Precio
        ttk.Label(frame_form, text="Precio (S/.):").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.entry_precio = ttk.Entry(frame_form, width=25)
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10)
        
        # Stock
        ttk.Label(frame_form, text="Stock:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.entry_stock = ttk.Entry(frame_form, width=25)
        self.entry_stock.grid(row=2, column=1, padx=10, pady=10)
        
        # Unidad de medida
        ttk.Label(frame_form, text="Unidad de Medida:").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.combo_unidad = ttk.Combobox(frame_form, values=self.unidades_medida, width=22)
        self.combo_unidad.grid(row=3, column=1, padx=10, pady=10)
        self.combo_unidad.current(0)  # Seleccionar la primera unidad por defecto
        
        # Botones
        frame_botones = tk.Frame(panel_izquierdo, bg=self.colores["fondo_panels"])
        frame_botones.pack(fill=tk.X, pady=20)
        
        ttk.Button(frame_botones, text="Agregar Producto", 
                 style="Principal.TButton",
                 command=self.agregar_producto).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_botones, text="Limpiar Campos", 
                 style="Secundario.TButton",
                 command=self.limpiar_formulario).pack(side=tk.RIGHT, padx=5)
        
        # Panel derecho - Lista de productos
        ttk.Label(panel_derecho, text="LISTA DE PRODUCTOS", style="Titulo.TLabel").pack(pady=10)
        
        # Tabla de productos
        frame_tabla = tk.Frame(panel_derecho, bg=self.colores["fondo_panels"])
        frame_tabla.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Scrollbar para la tabla
        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
        scroll_x = ttk.Scrollbar(frame_tabla, orient="horizontal")
        
        # Crear la tabla
        self.tabla_productos = ttk.Treeview(frame_tabla, 
                                          columns=("ID", "Nombre", "Precio", "Stock", "Unidad"),
                                          yscrollcommand=scroll_y.set,
                                          xscrollcommand=scroll_x.set)
        
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.config(command=self.tabla_productos.yview)
        scroll_x.config(command=self.tabla_productos.xview)
        
        # Configurar columnas
        self.tabla_productos.heading("ID", text="ID")
        self.tabla_productos.heading("Nombre", text="Nombre del Producto")
        self.tabla_productos.heading("Precio", text="Precio (S/.)")
        self.tabla_productos.heading("Stock", text="Stock")
        self.tabla_productos.heading("Unidad", text="Unidad")
        
        self.tabla_productos.column("ID", width=50, anchor="center")
        self.tabla_productos.column("Nombre", width=200)
        self.tabla_productos.column("Precio", width=100, anchor="center")
        self.tabla_productos.column("Stock", width=80, anchor="center")
        self.tabla_productos.column("Unidad", width=80, anchor="center")
        
        self.tabla_productos['show'] = 'headings'
        self.tabla_productos.pack(fill=tk.BOTH, expand=True)
        
        # Evento al seleccionar un producto
        self.tabla_productos.bind("<ButtonRelease-1>", self.seleccionar_producto)
        
        # Botones de acción
        frame_acciones = tk.Frame(panel_derecho, bg=self.colores["fondo_panels"])
        frame_acciones.pack(fill=tk.X, pady=10)
        
        ttk.Button(frame_acciones, text="Actualizar Precio", 
                 style="Principal.TButton",
                 command=self.actualizar_precio_producto).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_acciones, text="Actualizar Stock", 
                 style="Principal.TButton",
                 command=self.actualizar_stock_producto).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_acciones, text="Actualizar Unidad", 
                 style="Principal.TButton",
                 command=self.actualizar_unidad_producto).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_acciones, text="Eliminar Producto", 
                 style="Secundario.TButton",
                 command=self.eliminar_producto).pack(side=tk.RIGHT, padx=5)
        
        # Panel de detalles
        frame_detalles = tk.Frame(panel_derecho, bg=self.colores["fondo_panels"])
        frame_detalles.pack(fill=tk.X, pady=10)
        
        ttk.Label(frame_detalles, text="DETALLES DEL PRODUCTO", style="TLabel").pack(anchor=tk.W, pady=5)
        
        self.texto_detalles = scrolledtext.ScrolledText(frame_detalles, width=40, height=5)
        self.texto_detalles.pack(fill=tk.X, pady=5)
        
        # Cargar productos en la tabla
        self.actualizar_tabla_productos()
    
    def mostrar_ventas(self):
        self.limpiar_panel_principal()
        
        ttk.Label(self.panel_principal, text="Sistema de Ventas", 
                style="Titulo.TLabel").pack(pady=20)
        
        mensaje = "Esta sección está en desarrollo.\nAquí se implementará el sistema de ventas."
        
        mensaje_widget = scrolledtext.ScrolledText(self.panel_principal, width=40, height=10)
        mensaje_widget.pack(pady=20)
        mensaje_widget.insert(tk.END, mensaje)
        mensaje_widget.configure(state="disabled")
        
        ttk.Button(self.panel_principal, text="Volver a Productos", 
                 style="Principal.TButton",
                 command=self.mostrar_productos).pack(pady=20)
    
    def mostrar_estadisticas(self):
        self.limpiar_panel_principal()
        
        ttk.Label(self.panel_principal, text="Estadísticas del Mercado", 
                style="Titulo.TLabel").pack(pady=20)
        
        # Calcular estadísticas
        total_productos = len(self.productos)
        valor_total = sum(p.precio * p.stock for p in self.productos)
        stock_promedio = sum(p.stock for p in self.productos) / max(1, total_productos)
        precio_promedio = sum(p.precio for p in self.productos) / max(1, total_productos)
        
        # Producto más caro
        producto_mas_caro = max(self.productos, key=lambda p: p.precio) if self.productos else None
        # Producto con más stock
        producto_mas_stock = max(self.productos, key=lambda p: p.stock) if self.productos else None
        
        # Conteo por unidad de medida
        unidades_conteo = {}
        for p in self.productos:
            if p.unidad_medida in unidades_conteo:
                unidades_conteo[p.unidad_medida] += 1
            else:
                unidades_conteo[p.unidad_medida] = 1
        
        # Mostrar estadísticas en un panel
        frame_stats = tk.Frame(self.panel_principal, bg=self.colores["fondo_panels"], 
                             padx=15, pady=15, 
                             highlightbackground=self.colores["bordes"],
                             highlightthickness=2)
        frame_stats.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        ttk.Label(frame_stats, text="ESTADÍSTICAS DE INVENTARIO", 
                style="Titulo.TLabel").pack(pady=10)
        
        info = f"""
        Total de productos diferentes: {total_productos}
        
        Valor total del inventario: S/. {valor_total:.2f}
        
        Stock promedio por producto: {stock_promedio:.2f} unidades
        
        Precio promedio: S/. {precio_promedio:.2f}
        """
        
        if producto_mas_caro:
            info += f"\nProducto más caro: {producto_mas_caro.nombre} (S/. {producto_mas_caro.precio:.2f} / {producto_mas_caro.unidad_medida})"
        
        if producto_mas_stock:
            info += f"\nProducto con más stock: {producto_mas_stock.nombre} ({producto_mas_stock.stock} {producto_mas_stock.unidad_medida})"
        
        info += "\n\nProductos por unidad de medida:"
        for unidad, cantidad in unidades_conteo.items():
            info += f"\n  - {unidad}: {cantidad} producto(s)"
        
        stats_text = scrolledtext.ScrolledText(frame_stats, width=50, height=15)
        stats_text.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        stats_text.insert(tk.END, info)
        stats_text.configure(state="disabled")
        
        ttk.Button(frame_stats, text="Volver a Productos", 
                 style="Principal.TButton",
                 command=self.mostrar_productos).pack(pady=20)
    
    def agregar_producto(self):
        try:
            nombre = self.entry_nombre.get().strip()
            precio = float(self.entry_precio.get())
            stock = int(self.entry_stock.get())
            unidad_medida = self.combo_unidad.get()
            
            # Validaciones
            if not nombre:
                messagebox.showerror("Error", "Debe ingresar un nombre de producto")
                return
            
            if precio <= 0:
                messagebox.showerror("Error", "El precio debe ser un valor positivo")
                return
            
            if stock < 0:
                messagebox.showerror("Error", "El stock no puede ser negativo")
                return
            
            if not unidad_medida:
                messagebox.showerror("Error", "Debe seleccionar una unidad de medida")
                return
            
            # Verificar si ya existe un producto con el mismo nombre
            if any(p.nombre.lower() == nombre.lower() for p in self.productos):
                messagebox.showerror("Error", f"Ya existe un producto con el nombre '{nombre}'")
                return
            
            # Crear producto
            producto = Producto(nombre, precio, stock, unidad_medida)
            self.productos.append(producto)
            
            # Actualizar tabla
            self.actualizar_tabla_productos()
            
            # Limpiar formulario
            self.limpiar_formulario()
            
            messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente")
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para precio y stock")
    
    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        self.combo_unidad.current(0)
        self.texto_detalles.delete(1.0, tk.END)
    
    def actualizar_tabla_productos(self):
        # Limpiar tabla
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)
        
        # Agregar productos
        for idx, producto in enumerate(self.productos):
            self.tabla_productos.insert("", tk.END, values=(
                idx + 1,
                producto.nombre,
                f"{producto.precio:.2f}",
                producto.stock,
                producto.unidad_medida
            ))
    
    def seleccionar_producto(self, event=None):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            return
        
        item = self.tabla_productos.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        
        # Mostrar información
        producto = self.productos[idx]
        info = producto.mostrar_informacion()
        
        # Mostrar en el área de detalles
        self.texto_detalles.delete(1.0, tk.END)
        self.texto_detalles.insert(tk.END, info)
    
    def actualizar_precio_producto(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto")
            return
        
        item = self.tabla_productos.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        producto = self.productos[idx]
        
        # Pedir nuevo precio
        try:
            nuevo_precio = float(simpledialog.askstring("Actualizar Precio", 
                                                     f"Ingrese nuevo precio para {producto.nombre}:",
                                                     initialvalue=producto.precio))
            
            if nuevo_precio <= 0:
                messagebox.showerror("Error", "El precio debe ser un valor positivo")
                return
            
            # Actualizar precio
            mensaje = producto.actualizar_precio(nuevo_precio)
            
            # Actualizar tabla
            self.actualizar_tabla_productos()
            self.seleccionar_producto()
            
            messagebox.showinfo("Éxito", mensaje)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido")
        except TypeError:
            pass  # Usuario canceló la operación
    
    def actualizar_stock_producto(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto")
            return
        
        item = self.tabla_productos.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        producto = self.productos[idx]
        
        # Pedir nuevo stock
        try:
            nuevo_stock = int(simpledialog.askstring("Actualizar Stock", 
                                                  f"Ingrese nuevo stock para {producto.nombre}:",
                                                  initialvalue=producto.stock))
            
            if nuevo_stock < 0:
                messagebox.showerror("Error", "El stock no puede ser negativo")
                return
            
            # Actualizar stock
            mensaje = producto.actualizar_stock(nuevo_stock)
            
            # Actualizar tabla
            self.actualizar_tabla_productos()
            self.seleccionar_producto()
            
            messagebox.showinfo("Éxito", mensaje)
            
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico entero")
        except TypeError:
            pass  # Usuario canceló la operación
    
    def actualizar_unidad_producto(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto")
            return
        
        item = self.tabla_productos.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        producto = self.productos[idx]
        
        # Crear ventana de diálogo personalizada
        ventana_unidad = tk.Toplevel(self.root)
        ventana_unidad.title(f"Actualizar Unidad de Medida - {producto.nombre}")
        ventana_unidad.geometry("400x200")
        ventana_unidad.configure(bg=self.colores["fondo_panels"])
        ventana_unidad.resizable(False, False)
        ventana_unidad.transient(self.root)
        ventana_unidad.grab_set()
        
        ttk.Label(ventana_unidad, text=f"Seleccione nueva unidad de medida para {producto.nombre}:",
                style="TLabel").pack(pady=20)
        
        combo_nueva_unidad = ttk.Combobox(ventana_unidad, values=self.unidades_medida, width=25)
        combo_nueva_unidad.pack(pady=10)
        
        # Seleccionar la unidad actual
        try:
            idx_unidad = self.unidades_medida.index(producto.unidad_medida)
            combo_nueva_unidad.current(idx_unidad)
        except ValueError:
            combo_nueva_unidad.set(producto.unidad_medida)
        
        def confirmar_actualizacion():
            nueva_unidad = combo_nueva_unidad.get()
            if not nueva_unidad:
                messagebox.showerror("Error", "Debe seleccionar una unidad de medida", parent=ventana_unidad)
                return
            
            # Actualizar unidad
            mensaje = producto.actualizar_unidad_medida(nueva_unidad)
            
            # Actualizar tabla
            self.actualizar_tabla_productos()
            self.seleccionar_producto()
            
            messagebox.showinfo("Éxito", mensaje)
            ventana_unidad.destroy()
        
        frame_botones = tk.Frame(ventana_unidad, bg=self.colores["fondo_panels"])
        frame_botones.pack(fill=tk.X, pady=20)
        
        ttk.Button(frame_botones, text="Confirmar", 
                 style="Principal.TButton",
                 command=confirmar_actualizacion).pack(side=tk.LEFT, padx=20, pady=10)
        
        ttk.Button(frame_botones, text="Cancelar", 
                 style="Secundario.TButton",
                 command=ventana_unidad.destroy).pack(side=tk.RIGHT, padx=20, pady=10)
    
    def eliminar_producto(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto")
            return
        
        item = self.tabla_productos.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        producto = self.productos[idx]
        
        # Confirmar eliminación
        respuesta = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto '{producto.nombre}'?")
        if respuesta:
            del self.productos[idx]
            self.actualizar_tabla_productos()
            self.texto_detalles.delete(1.0, tk.END)
            messagebox.showinfo("Éxito", f"Producto '{producto.nombre}' eliminado correctamente")

# Importar simpledialog para ventanas de diálogo
from tkinter import simpledialog

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaMercado(root)
    root.mainloop()