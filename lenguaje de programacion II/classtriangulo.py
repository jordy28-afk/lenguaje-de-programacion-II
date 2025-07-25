"""import math

class Triangulo:
    def __init__(self):
        self.base = int(input("Ingrese la base: "))
        self.altura = int(input("Ingrese la altura: "))
        self.area = (self.base * self.altura) / 2
        self.hipotenusa = math.sqrt(self.base**2 + self.altura**2)
        self.perimetro = self.base + self.altura + self.hipotenusa
        print(f"Constructor: Se creó el perímetro y área del triángulo con base {self.base} y altura {self.altura}")

    def mostrar_resultado(self):
        print(f"El resultado del área es: {self.area}")
        print(f"El resultado del perímetro es: {self.perimetro}")

    def __del__(self):
        print(f"Destructor: Se eliminó el triángulo con base {self.base} y altura {self.altura}")

triangulo = Triangulo()
triangulo.mostrar_resultado()"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

class AplicacionTriangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Graficador de Triángulo")
        self.root.geometry("800x600")
        
        # Crear marco para controles
        self.frame_controles = ttk.LabelFrame(root, text="Coordenadas del Triángulo")
        self.frame_controles.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)
        
        # Coordenadas para los tres vértices
        ttk.Label(self.frame_controles, text="Vértice A:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.frame_controles, text="X:").grid(row=0, column=1, padx=5, pady=5)
        self.ax = ttk.Entry(self.frame_controles, width=8)
        self.ax.grid(row=0, column=2, padx=5, pady=5)
        self.ax.insert(0, "100")
        ttk.Label(self.frame_controles, text="Y:").grid(row=0, column=3, padx=5, pady=5)
        self.ay = ttk.Entry(self.frame_controles, width=8)
        self.ay.grid(row=0, column=4, padx=5, pady=5)
        self.ay.insert(0, "100")
        
        ttk.Label(self.frame_controles, text="Vértice B:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(self.frame_controles, text="X:").grid(row=1, column=1, padx=5, pady=5)
        self.bx = ttk.Entry(self.frame_controles, width=8)
        self.bx.grid(row=1, column=2, padx=5, pady=5)
        self.bx.insert(0, "300")
        ttk.Label(self.frame_controles, text="Y:").grid(row=1, column=3, padx=5, pady=5)
        self.by = ttk.Entry(self.frame_controles, width=8)
        self.by.grid(row=1, column=4, padx=5, pady=5)
        self.by.insert(0, "100")
        
        ttk.Label(self.frame_controles, text="Vértice C:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Label(self.frame_controles, text="X:").grid(row=2, column=1, padx=5, pady=5)
        self.cx = ttk.Entry(self.frame_controles, width=8)
        self.cx.grid(row=2, column=2, padx=5, pady=5)
        self.cx.insert(0, "200")
        ttk.Label(self.frame_controles, text="Y:").grid(row=2, column=3, padx=5, pady=5)
        self.cy = ttk.Entry(self.frame_controles, width=8)
        self.cy.grid(row=2, column=4, padx=5, pady=5)
        self.cy.insert(0, "50")
        
        # Botón para dibujar
        self.btn_dibujar = ttk.Button(self.frame_controles, text="Dibujar Triángulo", command=self.dibujar_triangulo)
        self.btn_dibujar.grid(row=3, column=0, columnspan=5, padx=5, pady=10)
        
        # Botón para limpiar
        self.btn_limpiar = ttk.Button(self.frame_controles, text="Limpiar", command=self.limpiar_canvas)
        self.btn_limpiar.grid(row=4, column=0, columnspan=5, padx=5, pady=5)
        
        # Sección para mostrar los cálculos
        self.frame_info = ttk.LabelFrame(self.frame_controles, text="Información del Triángulo")
        self.frame_info.grid(row=5, column=0, columnspan=5, padx=5, pady=10, sticky="we")
        
        self.info_lado_a = ttk.Label(self.frame_info, text="Lado a: ")
        self.info_lado_a.grid(row=0, column=0, padx=5, pady=2, sticky="w")
        
        self.info_lado_b = ttk.Label(self.frame_info, text="Lado b: ")
        self.info_lado_b.grid(row=1, column=0, padx=5, pady=2, sticky="w")
        
        self.info_lado_c = ttk.Label(self.frame_info, text="Lado c: ")
        self.info_lado_c.grid(row=2, column=0, padx=5, pady=2, sticky="w")
        
        self.info_perimetro = ttk.Label(self.frame_info, text="Perímetro: ")
        self.info_perimetro.grid(row=3, column=0, padx=5, pady=2, sticky="w")
        
        self.info_area = ttk.Label(self.frame_info, text="Área: ")
        self.info_area.grid(row=4, column=0, padx=5, pady=2, sticky="w")
        
        # Área para dibujar el triángulo
        self.canvas = tk.Canvas(root, bg="white", width=500, height=500)
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    def limpiar_canvas(self):
        self.canvas.delete("all")
        # Limpieza de información
        self.info_lado_a.config(text="Lado a: ")
        self.info_lado_b.config(text="Lado b: ")
        self.info_lado_c.config(text="Lado c: ")
        self.info_perimetro.config(text="Perímetro: ")
        self.info_area.config(text="Área: ")
    
    def dibujar_triangulo(self):
        self.limpiar_canvas()
        
        try:
            # Obtener coordenadas
            ax = int(self.ax.get())
            ay = int(self.ay.get())
            bx = int(self.bx.get())
            by = int(self.by.get())
            cx = int(self.cx.get())
            cy = int(self.cy.get())
            
            # Verificar que los puntos forman un triángulo
            area = abs(0.5 * ((ax * (by - cy)) + (bx * (cy - ay)) + (cx * (ay - by))))
            if area == 0:
                messagebox.showerror("Error", "Los puntos introducidos no forman un triángulo")
                return
            
            # Dibujar el triángulo
            self.canvas.create_polygon(ax, ay, bx, by, cx, cy, fill="", outline="blue", width=2)
            
            # Etiquetar los vértices
            self.canvas.create_text(ax, ay-10, text=f"A({ax},{ay})")
            self.canvas.create_text(bx, by-10, text=f"B({bx},{by})")
            self.canvas.create_text(cx, cy-10, text=f"C({cx},{cy})")
            
            # Calcular longitudes de los lados
            lado_a = math.sqrt((bx - cx)**2 + (by - cy)**2)
            lado_b = math.sqrt((ax - cx)**2 + (ay - cy)**2)
            lado_c = math.sqrt((ax - bx)**2 + (ay - by)**2)
            
            # Calcular perímetro y área
            perimetro = lado_a + lado_b + lado_c
            
            # Actualizar información
            self.info_lado_a.config(text=f"Lado a: {lado_a:.2f}")
            self.info_lado_b.config(text=f"Lado b: {lado_b:.2f}")
            self.info_lado_c.config(text=f"Lado c: {lado_c:.2f}")
            self.info_perimetro.config(text=f"Perímetro: {perimetro:.2f}")
            self.info_area.config(text=f"Área: {area:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduzca valores numéricos válidos para las coordenadas")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTriangulo(root)
    root.mainloop()