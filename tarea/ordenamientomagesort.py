"""def merge_sort(arr):
    if len(arr) > 1:
        # Encuentra el punto medio para dividir el arreglo
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        # Llama recursivamente a merge_sort en ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Índices para recorrer las dos sublistas y el arreglo principal
        i = 0  # Índice para izquierda
        j = 0  # Índice para derecha
        k = 0  # Índice para el arreglo principal

        # Fusiona las dos mitades en el arreglo principal
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Copia los elementos restantes de izquierda, si los hay
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        # Copia los elementos restantes de derecha, si los hay
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
arr = [12, 11, 13, 5, 6]
merge_sort(arr)
print("Lista ordenada:", arr)"""
import tkinter as tk
from tkinter import messagebox

# Función para el ordenamiento Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        # Encuentra el punto medio para dividir el arreglo
        medio = len(arr) // 2
        izquierda = arr[:medio]
        derecha = arr[medio:]

        # Llama recursivamente a merge_sort en ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Índices para recorrer las dos sublistas y el arreglo principal
        i = 0  # Índice para izquierda
        j = 0  # Índice para derecha
        k = 0  # Índice para el arreglo principal

        # Fusiona las dos mitades en el arreglo principal
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        # Copia los elementos restantes de izquierda, si los hay
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        # Copia los elementos restantes de derecha, si los hay
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

# Función para procesar la lista ingresada y mostrar el resultado
def ordenar():
    try:
        # Obtiene la lista de números desde el campo de entrada
        lista = list(map(int, entry_lista.get().split(',')))
        # Ordena la lista usando Merge Sort
        merge_sort(lista)
        # Muestra el resultado en la etiqueta de salida
        label_resultado.config(text="Lista ordenada: " + str(lista))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una lista de números separados por comas.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ordenamiento Merge Sort")

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
