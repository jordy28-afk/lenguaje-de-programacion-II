"""def quicksort(arr, bajo, alto):
    if bajo < alto:
        pivote = particionar(arr, bajo, alto)
        quicksort(arr, bajo, pivote - 1)
        quicksort(arr, pivote + 1, alto)

def particionar(arr, bajo, alto):
    pivote = arr[alto]  
    i = bajo - 1  
    for j in range(bajo, alto):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1  

arr = [8, 14, 5, 2, 7]
quicksort(arr, 0, len(arr) - 1)
print("arr ordenado :", arr)"""
import tkinter as tk
from tkinter import messagebox

# Función para el ordenamiento QuickSort
def quicksort(arr, bajo, alto):
    if bajo < alto:
        pivote = particionar(arr, bajo, alto)
        quicksort(arr, bajo, pivote - 1)
        quicksort(arr, pivote + 1, alto)

def particionar(arr, bajo, alto):
    pivote = arr[alto]
    i = bajo - 1
    for j in range(bajo, alto):
        if arr[j] < pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

# Función para procesar la lista ingresada y mostrar el resultado
def ordenar():
    try:
        # Obtiene la lista de números desde el campo de entrada
        lista = list(map(int, entry_lista.get().split(',')))
        # Ordena la lista usando QuickSort
        quicksort(lista, 0, len(lista) - 1)
        # Muestra el resultado en la etiqueta de salida
        label_resultado.config(text="Lista ordenada: " + str(lista))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una lista de números separados por comas.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ordenamiento QuickSort")

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


