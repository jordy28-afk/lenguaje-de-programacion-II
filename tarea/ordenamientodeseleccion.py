"""def ordenamiento_seleccion(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[minimo]:
                minimo = j
        arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]
    return arreglo

lista = [64, 25, 12, 22, 11]
resultado = ordenamiento_seleccion(lista)
print(resultado)"""
import tkinter as tk
from tkinter import messagebox

# Función para el ordenamiento por selección
def ordenamiento_seleccion(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[minimo]:
                minimo = j
        arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]
    return arreglo

# Función para procesar la lista ingresada y mostrar el resultado
def ordenar():
    try:
        # Obtiene la lista de números desde el campo de entrada
        lista = list(map(int, entry_lista.get().split(',')))
        # Ordena la lista
        resultado = ordenamiento_seleccion(lista)
        # Muestra el resultado en la etiqueta de salida
        label_resultado.config(text="Lista ordenada: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una lista de números separados por comas.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ordenamiento por Selección")

# Etiqueta de instrucción
label_instruccion = tk.Label(root, text="Ingresa una lista de números separados por comas:")
label_instruccion.pack(pady=10)

# Campo de entrada para la lista
entry_lista = tk.Entry(root, width=30)
entry_lista.pack(pady=5)

# Botón para ordenar
btn_ordenar = tk.Button(root, text="Ordenar", command=ordenar)
btn_ordenar.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="Lista ordenada: ")
label_resultado.pack(pady=10)

# Ejecuta la ventana principal
root.mainloop()

