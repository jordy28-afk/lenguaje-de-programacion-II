import tkinter as tk
from math import pi

def calcular_area():
    try:
        if var.get() == "triangulo":
            base = float(entry_base.get())
            altura = float(entry_altura.get())
            area = (base * altura) / 2
            label_resultado.config(text=f"El área del triángulo es: {area:.2f}")
        else:
            radio = float(entry_radio.get())
            area = pi * (radio ** 2)
            label_resultado.config(text=f"El área del círculo es: {area:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa números válidos.")

def mostrar_triangulo():
    entry_base.pack(pady=10)
    entry_altura.pack(pady=10)
    entry_radio.pack_forget()
    label_radio.pack_forget()
    boton_calcular.config(text="Calcular Área del Triángulo")

def mostrar_circulo():
    entry_base.pack_forget()
    entry_altura.pack_forget()
    entry_radio.pack(pady=10)
    label_radio.pack(pady=10)
    boton_calcular.config(text="Calcular Área del Círculo")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Áreas")
ventana.geometry("600x600")
ventana.config(bg="#e0f7fa")  # Color de fondo

# Variable para seleccionar figura
var = tk.StringVar(value="triangulo")

# Título en la ventana
titulo = tk.Label(ventana, text="CALCULA ÁREAS", font=("Arial", 20), bg="#e0f7fa")
titulo.pack(pady=20)

# Radio buttons para seleccionar figura
rb_triangulo = tk.Radiobutton(ventana, text="Triángulo", variable=var, value="triangulo", command=mostrar_triangulo, bg="#e0f7fa")
rb_triangulo.pack(pady=5)

rb_circulo = tk.Radiobutton(ventana, text="Círculo", variable=var, value="circulo", command=mostrar_circulo, bg="#e0f7fa")
rb_circulo.pack(pady=5)

# Entradas para triángulo
label_base = tk.Label(ventana, text="Base del triángulo:", bg="#e0f7fa")
label_base.pack(pady=10)
entry_base = tk.Entry(ventana)

label_altura = tk.Label(ventana, text="Altura del triángulo:", bg="#e0f7fa")
label_altura.pack(pady=10)
entry_altura = tk.Entry(ventana)

# Entradas para círculo
label_radio = tk.Label(ventana, text="Radio del círculo:", bg="#e0f7fa")
entry_radio = tk.Entry(ventana)

# Botón para calcular el área
boton_calcular = tk.Button(ventana, text="Calcular Área del Triángulo", command=calcular_area, bg="#4caf50", fg="white")
boton_calcular.pack(pady=20)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="", bg="#e0f7fa")
label_resultado.pack(pady=20)

# Mostrar campos iniciales para triángulo
mostrar_triangulo()

# Ejecutar la ventana
ventana.mainloop()