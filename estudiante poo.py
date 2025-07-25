import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
     
    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def es_aprobado(self):
        return self.promedio() >= 10.5
    
    def mostrar_informacion(self):
        info = f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}\nNotas: {self.notas}\n"
        info += f"Promedio: {self.promedio():.2f}\nAprobado: {'Sí' if self.es_aprobado() else 'No'}"
        return info

class SistemaEstudiantes:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Estudiantes")
        self.root.geometry("1000x600")
        self.root.configure(bg="#3498db")  # Fondo azul
        
        # Lista de estudiantes
        self.estudiantes = []
        
        # Colores para la interfaz
        self.colores = {
            "fondo": "#3498db",         # Azul
            "botones": "#e74c3c",       # Rojo
            "texto": "#ecf0f1",         # Blanco grisáceo
            "destacado": "#f39c12",     # Naranja
            "aprobado": "#2ecc71",      # Verde
            "desaprobado": "#e74c3c",   # Rojo
            "frames": "#2980b9"         # Azul oscuro
        }
        
        # Crear estilos para ttk
        self.configurar_estilos()
        
        # Crear componentes de la interfaz
        self.crear_interfaz()
    
    def configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # Estilo para los botones
        style.configure("Colorful.TButton", 
                        background=self.colores["botones"], 
                        foreground=self.colores["texto"],
                        font=("Arial", 10, "bold"),
                        borderwidth=1)
        style.map("Colorful.TButton",
                 background=[('active', self.colores["destacado"])])
        
        # Estilo para las entradas
        style.configure("TEntry", 
                        fieldbackground="white",
                        font=("Arial", 10))
        
        # Estilo para las etiquetas
        style.configure("TLabel", 
                        background=self.colores["fondo"],
                        foreground=self.colores["texto"],
                        font=("Arial", 10, "bold"))
        
        # Estilo para el treeview
        style.configure("Treeview", 
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white")
        style.map("Treeview",
                 background=[('selected', self.colores["destacado"])])
        style.configure("Treeview.Heading", 
                        background=self.colores["frames"],
                        foreground=self.colores["texto"],
                        font=("Arial", 10, "bold"))
    
    def crear_interfaz(self):
        # Marco principal dividido en dos paneles
        self.panel_izquierdo = tk.Frame(self.root, bg=self.colores["frames"], 
                                        padx=10, pady=10, width=400)
        self.panel_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        
        self.panel_derecho = tk.Frame(self.root, bg=self.colores["frames"], 
                                      padx=10, pady=10)
        self.panel_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, 
                               padx=10, pady=10)
        
        # Configurar panel izquierdo (formulario de ingreso)
        self.crear_formulario_estudiante()
        
        # Configurar panel derecho (lista y detalles)
        self.crear_panel_lista_estudiantes()
    
    def crear_formulario_estudiante(self):
        # Título del formulario
        tk.Label(self.panel_izquierdo, text="REGISTRAR ESTUDIANTE", 
                 bg=self.colores["frames"], fg=self.colores["texto"],
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        # Campos para el estudiante
        frame_datos = tk.Frame(self.panel_izquierdo, bg=self.colores["frames"])
        frame_datos.pack(fill=tk.X, pady=5)
        
        # Nombre
        tk.Label(frame_datos, text="Nombre:", 
                bg=self.colores["frames"], fg=self.colores["texto"],
                font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nombre = ttk.Entry(frame_datos, width=30)
        self.entry_nombre.grid(row=0, column=1, sticky="w", pady=5, padx=5)
        
        # Edad
        tk.Label(frame_datos, text="Edad:", 
                bg=self.colores["frames"], fg=self.colores["texto"],
                font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_edad = ttk.Entry(frame_datos, width=30)
        self.entry_edad.grid(row=1, column=1, sticky="w", pady=5, padx=5)
        
        # Carrera
        tk.Label(frame_datos, text="Carrera:", 
                bg=self.colores["frames"], fg=self.colores["texto"],
                font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_carrera = ttk.Entry(frame_datos, width=30)
        self.entry_carrera.grid(row=2, column=1, sticky="w", pady=5, padx=5)
        
        # Sección de notas
        tk.Label(self.panel_izquierdo, text="NOTAS", 
                 bg=self.colores["frames"], fg=self.colores["texto"],
                 font=("Arial", 12, "bold")).pack(pady=10)
        
        # Frame para manejar las notas
        frame_notas = tk.Frame(self.panel_izquierdo, bg=self.colores["frames"])
        frame_notas.pack(fill=tk.X, pady=5)
        
        tk.Label(frame_notas, text="Nota:", 
                bg=self.colores["frames"], fg=self.colores["texto"],
                font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_nota = ttk.Entry(frame_notas, width=10)
        self.entry_nota.grid(row=0, column=1, sticky="w", pady=5, padx=5)
        
        ttk.Button(frame_notas, text="Agregar Nota", 
                  style="Colorful.TButton",
                  command=self.agregar_nota_actual).grid(row=0, column=2, padx=5, pady=5)
        
        # Mostrar las notas ingresadas
        tk.Label(self.panel_izquierdo, text="Notas ingresadas:", 
                bg=self.colores["frames"], fg=self.colores["texto"],
                font=("Arial", 10, "bold")).pack(anchor="w", pady=5)
        
        self.texto_notas = scrolledtext.ScrolledText(self.panel_izquierdo, 
                                                   width=30, height=4)
        self.texto_notas.pack(fill=tk.X, pady=5)
        self.notas_actuales = []
        
        # Botones de acción
        frame_botones = tk.Frame(self.panel_izquierdo, bg=self.colores["frames"])
        frame_botones.pack(fill=tk.X, pady=15)
        
        ttk.Button(frame_botones, text="Guardar Estudiante", 
                  style="Colorful.TButton",
                  command=self.guardar_estudiante).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_botones, text="Limpiar Formulario", 
                  style="Colorful.TButton",
                  command=self.limpiar_formulario).pack(side=tk.RIGHT, padx=5)
    
    def crear_panel_lista_estudiantes(self):
        # Título
        tk.Label(self.panel_derecho, text="LISTA DE ESTUDIANTES", 
                 bg=self.colores["frames"], fg=self.colores["texto"],
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        # Tabla de estudiantes
        frame_tabla = tk.Frame(self.panel_derecho, bg=self.colores["frames"])
        frame_tabla.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Scrollbar para la tabla
        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical")
        scroll_x = ttk.Scrollbar(frame_tabla, orient="horizontal")
        
        # Crear la tabla
        self.tabla_estudiantes = ttk.Treeview(frame_tabla, 
                                            columns=("ID", "Nombre", "Edad", "Carrera", "Promedio", "Estado"),
                                            yscrollcommand=scroll_y.set,
                                            xscrollcommand=scroll_x.set)
        
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.config(command=self.tabla_estudiantes.yview)
        scroll_x.config(command=self.tabla_estudiantes.xview)
        
        # Configurar columnas
        self.tabla_estudiantes.heading("ID", text="ID")
        self.tabla_estudiantes.heading("Nombre", text="Nombre")
        self.tabla_estudiantes.heading("Edad", text="Edad")
        self.tabla_estudiantes.heading("Carrera", text="Carrera")
        self.tabla_estudiantes.heading("Promedio", text="Promedio")
        self.tabla_estudiantes.heading("Estado", text="Estado")
        
        self.tabla_estudiantes.column("ID", width=40, anchor="center")
        self.tabla_estudiantes.column("Nombre", width=150)
        self.tabla_estudiantes.column("Edad", width=60, anchor="center")
        self.tabla_estudiantes.column("Carrera", width=150)
        self.tabla_estudiantes.column("Promedio", width=80, anchor="center")
        self.tabla_estudiantes.column("Estado", width=80, anchor="center")
        
        self.tabla_estudiantes['show'] = 'headings'  # ocultar la primera columna vacía
        self.tabla_estudiantes.pack(fill=tk.BOTH, expand=True)
        
        # Evento al seleccionar un estudiante
        self.tabla_estudiantes.bind("<ButtonRelease-1>", self.mostrar_detalle_estudiante)
        
        # Panel de detalles
        tk.Label(self.panel_derecho, text="DETALLE DEL ESTUDIANTE", 
                 bg=self.colores["frames"], fg=self.colores["texto"],
                 font=("Arial", 12, "bold")).pack(pady=5)
        
        self.detalle_estudiante = scrolledtext.ScrolledText(self.panel_derecho, 
                                                          width=40, height=8)
        self.detalle_estudiante.pack(fill=tk.X, pady=5)
        
        # Botones de estadísticas
        frame_estadisticas = tk.Frame(self.panel_derecho, bg=self.colores["frames"])
        frame_estadisticas.pack(fill=tk.X, pady=10)
        
        ttk.Button(frame_estadisticas, text="Ver Estadísticas", 
                  style="Colorful.TButton",
                  command=self.mostrar_estadisticas).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_estadisticas, text="Eliminar Estudiante", 
                  style="Colorful.TButton",
                  command=self.eliminar_estudiante).pack(side=tk.RIGHT, padx=5)
    
    def agregar_nota_actual(self):
        try:
            nota = float(self.entry_nota.get())
            if 0 <= nota <= 20:  # Validar rango de notas
                self.notas_actuales.append(nota)
                self.texto_notas.delete(1.0, tk.END)
                self.texto_notas.insert(tk.END, f"{self.notas_actuales}\n")
                self.entry_nota.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "La nota debe estar entre 0 y 20")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido")
    
    def guardar_estudiante(self):
        try:
            nombre = self.entry_nombre.get().strip()
            edad = int(self.entry_edad.get())
            carrera = self.entry_carrera.get().strip()
            
            # Validaciones
            if not nombre or not carrera:
                messagebox.showerror("Error", "Debe completar todos los campos")
                return
            
            if edad <= 0:
                messagebox.showerror("Error", "La edad debe ser un número positivo")
                return
            
            if not self.notas_actuales:
                messagebox.showerror("Error", "Debe ingresar al menos una nota")
                return
            
            # Crear estudiante
            estudiante = Estudiante(nombre, edad, carrera)
            for nota in self.notas_actuales:
                estudiante.agregar_nota(nota)
            
            # Añadir a la lista
            self.estudiantes.append(estudiante)
            
            # Actualizar tabla
            self.actualizar_tabla()
            
            # Limpiar formulario
            self.limpiar_formulario()
            
            messagebox.showinfo("Éxito", f"Estudiante {nombre} registrado con éxito")
            
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero")
    
    def limpiar_formulario(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self.entry_carrera.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)
        self.texto_notas.delete(1.0, tk.END)
        self.notas_actuales = []
    
    def actualizar_tabla(self):
        # Limpiar tabla
        for item in self.tabla_estudiantes.get_children():
            self.tabla_estudiantes.delete(item)
        
        # Agregar estudiantes
        for idx, estudiante in enumerate(self.estudiantes):
            promedio = f"{estudiante.promedio():.2f}"
            estado = "Aprobado" if estudiante.es_aprobado() else "Reprobado"
            
            # Insertar datos
            self.tabla_estudiantes.insert("", tk.END, values=(
                idx + 1,
                estudiante.nombre,
                estudiante.edad,
                estudiante.carrera,
                promedio,
                estado
            ))
            
            # Colorear filas según estado
            items = self.tabla_estudiantes.get_children()
            for item in items:
                valores = self.tabla_estudiantes.item(item, "values")
                if valores[5] == "Aprobado":
                    self.tabla_estudiantes.tag_configure("aprobado", background="#d4ffcc")
                    self.tabla_estudiantes.item(item, tags=("aprobado",))
                else:
                    self.tabla_estudiantes.tag_configure("reprobado", background="#ffcccc")
                    self.tabla_estudiantes.item(item, tags=("reprobado",))
    
    def mostrar_detalle_estudiante(self, event=None):
        # Obtener el estudiante seleccionado
        seleccion = self.tabla_estudiantes.selection()
        if not seleccion:
            return
        
        # Obtener el índice
        item = self.tabla_estudiantes.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        
        # Mostrar información
        estudiante = self.estudiantes[idx]
        info = estudiante.mostrar_informacion()
        
        # Mostrar en el área de detalles
        self.detalle_estudiante.delete(1.0, tk.END)
        self.detalle_estudiante.insert(tk.END, info)
    
    def eliminar_estudiante(self):
        seleccion = self.tabla_estudiantes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Debe seleccionar un estudiante")
            return
        
        item = self.tabla_estudiantes.item(seleccion[0])
        idx = int(item["values"][0]) - 1
        nombre = self.estudiantes[idx].nombre
        
        # Confirmar eliminación
        respuesta = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar a {nombre}?")
        if respuesta:
            del self.estudiantes[idx]
            self.actualizar_tabla()
            self.detalle_estudiante.delete(1.0, tk.END)
            messagebox.showinfo("Éxito", f"Estudiante {nombre} eliminado con éxito")
    
    def mostrar_estadisticas(self):
        if not self.estudiantes:
            messagebox.showinfo("Información", "No hay estudiantes registrados")
            return
        
        # Calcular estadísticas
        total = len(self.estudiantes)
        aprobados = sum(1 for e in self.estudiantes if e.es_aprobado())
        desaprobados = total - aprobados
        promedio_general = sum(e.promedio() for e in self.estudiantes) / total
        
        # Mostrar ventana de estadísticas
        ventana = tk.Toplevel(self.root)
        ventana.title("Estadísticas")
        ventana.geometry("400x300")
        ventana.configure(bg=self.colores["frames"])
        
        # Contenido
        tk.Label(ventana, text="ESTADÍSTICAS DEL CURSO", 
                bg=self.colores["frames"], fg=self.colores["texto"],
                font=("Arial", 14, "bold")).pack(pady=10)
        
        info = f"""
        Total de estudiantes: {total}
        Estudiantes aprobados: {aprobados} ({(aprobados/total*100):.1f}%)
        Estudiantes desaprobados: {desaprobados} ({(desaprobados/total*100):.1f}%)
        Promedio general del curso: {promedio_general:.2f}
        """
        
        texto_stats = scrolledtext.ScrolledText(ventana, width=35, height=10)
        texto_stats.pack(pady=10)
        texto_stats.insert(tk.END, info)
        
        ttk.Button(ventana, text="Cerrar", 
                  style="Colorful.TButton",
                  command=ventana.destroy).pack(pady=10)

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaEstudiantes(root)
    root.mainloop()