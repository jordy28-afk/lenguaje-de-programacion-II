"""class persona :
    def __init__(self,nombre):
        self.nombre = nombre 
        
p1 = persona ("Maria")
p2 = p1 

p2.nombre = 'carla'

print(p1.nombre)"""

#clas precio

"""class precio:
    def __init__(self,precio):
        self.precio = precio

    def aplicar_descuento(self,porcentaje):
        self.precio -= self.precio*(porcentaje/100)

p = Producto(100)

p.aplicar_descuento(10)
print(p.precio)"""


# CIUDAD
"""
import math

class Ciudad:
    def __init__(self):
        self.nombre = input("nombre de la ciudad: ")
        self.x = float(input("ingrese la cordenada x-->"))
        self.y = float(input("ingrese la cordenada y-->"))      

    def distancia(self, otra_ciudad):
        dx = self.x - otra_ciudad.x
        dy = self.y - otra_ciudad.y
        return math.sqrt(dx**2 + dy**2)

ciudad1 = Ciudad()
ciudad2 = Ciudad()

distancia_km =ciudad1.distancia(ciudad2)


print(f"distancia entre {ciudad1.nombre} y {ciudad2.nombre}: {distancia_km} unidades")"""
#rectangulo
"""class Rectangulo:
    def __init__(self):
        self.base = float(input("Ingrese la base del rectángulo: "))
        self.altura = float(input("Ingrese la altura del rectángulo: "))
        self.color = input("Ingrese el color del rectángulo: ")

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def mostrar_info(self):
        print(f"Rectángulo de base {self.base}, altura {self.altura}, color {self.color}")

rectangulo1 = Rectangulo()
rectangulo2 = Rectangulo()

rectangulo1.mostrar_info()
print(f"Área: {rectangulo1.calcular_area()}, Perímetro: {rectangulo1.calcular_perimetro()}, Color: {rectangulo1.color}")

rectangulo2.mostrar_info()
print(f"Área: {rectangulo2.calcular_area()}, Perímetro: {rectangulo2.calcular_perimetro()}, Color: {rectangulo2.color}")"""


#tjinder |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


"""import tkinter as tk
from tkinter import colorchooser, messagebox

class Rectangulo:
    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class AplicacionRectangulos:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Rectángulos")
        self.root.geometry("800x600")
        
        self.rectangulos = []
        
        # Marcos principales
        self.frame_entrada = tk.Frame(root, padx=10, pady=10)
        self.frame_entrada.pack(fill="x")
        
        self.frame_canvas = tk.Frame(root, padx=10, pady=10)
        self.frame_canvas.pack(fill="both", expand=True)
        
        self.frame_info = tk.Frame(root, padx=10, pady=10)
        self.frame_info.pack(fill="x")
        
        # Elementos de entrada
        tk.Label(self.frame_entrada, text="Base:").grid(row=0, column=0, padx=5, pady=5)
        self.entrada_base = tk.Entry(self.frame_entrada)
        self.entrada_base.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.frame_entrada, text="Altura:").grid(row=0, column=2, padx=5, pady=5)
        self.entrada_altura = tk.Entry(self.frame_entrada)
        self.entrada_altura.grid(row=0, column=3, padx=5, pady=5)
        
        self.btn_color = tk.Button(self.frame_entrada, text="Seleccionar Color", command=self.seleccionar_color)
        self.btn_color.grid(row=0, column=4, padx=5, pady=5)
        self.color_actual = "#FF0000"
        
        self.btn_agregar = tk.Button(self.frame_entrada, text="Agregar Rectángulo", command=self.agregar_rectangulo)
        self.btn_agregar.grid(row=0, column=5, padx=5, pady=5)
        
        self.btn_eliminar = tk.Button(self.frame_entrada, text="Eliminar Último", command=self.eliminar_ultimo)
        self.btn_eliminar.grid(row=0, column=6, padx=5, pady=5)

        self.btn_limpiar = tk.Button(self.frame_entrada, text="Limpiar Todo", command=self.limpiar_todo)
        self.btn_limpiar.grid(row=0, column=7, padx=5, pady=5)
        
        # Canvas con scroll horizontal
        self.canvas = tk.Canvas(self.frame_canvas, bg="white", width=780, height=400, scrollregion=(0, 0, 1000, 400))
        self.canvas.pack(fill="both", expand=True, side="left")
        self.scroll_x = tk.Scrollbar(self.frame_canvas, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.pack(fill="x", side="bottom")
        self.canvas.config(xscrollcommand=self.scroll_x.set)
        
        # Área de información
        self.info_text = tk.Text(self.frame_info, height=6, width=80)
        self.info_text.pack(fill="both", expand=True)
        
    def seleccionar_color(self):
        color = colorchooser.askcolor(title="Selecciona un color")
        if color[1]:
            self.color_actual = color[1]
            self.btn_color.config(bg=self.color_actual)
    
    def agregar_rectangulo(self):
        try:
            base = float(self.entrada_base.get())
            altura = float(self.entrada_altura.get())
            if base <= 0 or altura <= 0:
                messagebox.showerror("Error", "La base y la altura deben ser números positivos")
                return
            
            rectangulo = Rectangulo(base, altura, self.color_actual)
            self.rectangulos.append(rectangulo)
            self.dibujar_rectangulos()
            self.actualizar_info()
            self.entrada_base.delete(0, tk.END)
            self.entrada_altura.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos para base y altura")
    
    def eliminar_ultimo(self):
        if self.rectangulos:
            self.rectangulos.pop()
            self.dibujar_rectangulos()
            self.actualizar_info()
    
    def dibujar_rectangulos(self):
        self.canvas.delete("all")
        if not self.rectangulos:
            return
        
        max_base = max(rect.base for rect in self.rectangulos)
        max_altura = max(rect.altura for rect in self.rectangulos)
        escala = min(700 / (max_base * len(self.rectangulos)), 350 / max_altura, 50)

        x_pos = 40
        total_width = 0
        
        for i, rect in enumerate(self.rectangulos):
            x1 = x_pos
            y1 = 40
            x2 = x1 + rect.base * escala
            y2 = y1 + rect.altura * escala
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=rect.color, outline="black")
            self.canvas.create_text((x1 + x2) / 2, y2 + 15, text=f"Rectángulo {i+1}")
            x_pos = x2 + 40
            total_width = x_pos

        self.canvas.config(scrollregion=(0, 0, total_width + 50, 400))

    def actualizar_info(self):
        self.info_text.delete(1.0, tk.END)
        total_area = 0
        total_perimetro = 0
        
        for i, rect in enumerate(self.rectangulos):
            area = rect.calcular_area()
            perimetro = rect.calcular_perimetro()
            total_area += area
            total_perimetro += perimetro
            info = f"Rectángulo {i+1}: Base = {rect.base}, Altura = {rect.altura}, Color = {rect.color}\n"
            info += f"Área = {area}, Perímetro = {perimetro}\n\n"
            self.info_text.insert(tk.END, info)

        resumen = f"TOTAL: Área = {total_area}, Perímetro = {total_perimetro}\n"
        self.info_text.insert(tk.END, resumen)

    def limpiar_todo(self):
        self.rectangulos = []
        self.canvas.delete("all")
        self.info_text.delete(1.0, tk.END)
        self.entrada_base.delete(0, tk.END)
        self.entrada_altura.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionRectangulos(root)
    root.mainloop()"""

#_______________________________________________________________________________________

class Rectangulo:
    def __init__(self, base, altura, color): 
        self.base = base
        self.altura = altura
        self.color = color

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)
    
    def mostrar_info(self):
        print(f"\nRectángulo de base {self.base}, altura {self.altura}, color {self.color}")
        print(f"Área: {self.area()} - Perímetro: {self.perimetro()}")

class Cuadrado(Rectangulo):
    def __init__(self, lado, color):  
        super().__init__(lado, lado, color)  

    def mostrar_info(self):
        print(f"\nCuadrado de lado: {self.base}, Color: {self.color}")
        print(f"Área: {self.area()} - Perímetro: {self.perimetro()}")
        super().mostrar_info() 

r1 = Rectangulo(10, 6, "verde")
C1 = Cuadrado(7, "azul")

r1.mostrar_info()
C1.mostrar_info()