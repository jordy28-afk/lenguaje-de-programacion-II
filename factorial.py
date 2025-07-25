"""def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

numero=int(input("valor de n" ))
print(f"el factorial es :{factorial(numero)}")"""
import tkinter as tk
from tkinter import messagebox

# Función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n

# Función para mostrar el resultado en un mensaje emergente
def calcular_factorial():
    try:
        numero = int(entry.get())
        resultado = factorial(numero)
        messagebox.showinfo("Resultado", f"El factorial de {numero} es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido")

# Configuración de la ventana principal de tkinter
ventana = tk.Tk()
ventana.title("Cálculo de Factorial")

# Etiqueta y entrada para el número
label = tk.Label(ventana, text="Ingrese el valor de n:")
label.pack()

entry = tk.Entry(ventana)
entry.pack()

# Botón para calcular el factorial
boton = tk.Button(ventana, text="Calcular", command=calcular_factorial)
boton.pack()

ventana.mainloop()

    