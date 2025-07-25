import tkinter as tk
from tkinter import messagebox

# Funciones de ordenamiento
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def ordenamiento_seleccion(arreglo):
    n = len(arreglo)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if arreglo[j] < arreglo[minimo]:
                minimo = j
        arreglo[i], arreglo[minimo] = arreglo[minimo], arreglo[i]
    return arreglo

def merge_sort(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]
        merge_sort(izquierda)
        merge_sort(derecha)

        i = 0  # Índice para izquierda
        j = 0  # Índice para derecha
        k = 0  # Índice para el arreglo principal

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

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

# Función que se llama al seleccionar un algoritmo
def ejecutar_algoritmo():
    algoritmo = algoritmo_var.get()
    lista = list(map(int, entrada.get().split(',')))  # Obtener lista de entrada
    resultado = []

    if algoritmo == "Burbuja":
        resultado = ordenamiento_burbuja(lista.copy())
    elif algoritmo == "Selección":
        resultado = ordenamiento_seleccion(lista.copy())
    elif algoritmo == "Merge":
        resultado = lista.copy()
        merge_sort(resultado)
    elif algoritmo == "Quick":
        resultado = lista.copy()
        quicksort(resultado, 0, len(resultado) - 1)

    messagebox.showinfo("Resultado", f"Lista ordenada ({algoritmo}): {resultado}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar Algoritmo de Ordenamiento")

# Variable para seleccionar el algoritmo
algoritmo_var = tk.StringVar(value="Burbuja")

# Interfaz
tk.Label(ventana, text="Introduce los números separados por comas:").pack()
entrada = tk.Entry(ventana)
entrada.pack()

tk.Label(ventana, text="Selecciona el algoritmo de ordenamiento:").pack()
tk.Radiobutton(ventana, text="Burbuja", variable=algoritmo_var, value="Burbuja").pack()
tk.Radiobutton(ventana, text="Selección", variable=algoritmo_var, value="Selección").pack()
tk.Radiobutton(ventana, text="Merge", variable=algoritmo_var, value="Merge").pack()
tk.Radiobutton(ventana, text="Quick", variable=algoritmo_var, value="Quick").pack()

tk.Button(ventana, text="Ejecutar", command=ejecutar_algoritmo).pack()

# Ejecutar la ventana
ventana.mainloop()
