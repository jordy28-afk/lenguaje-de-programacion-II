import tkinter as tk
from tkinter import ttk

# Funciones de generación de matrices
def matriz_caracol(n):
    matriz = [[0]*n for _ in range(n)]
    izquierda, derecha = 0, n - 1
    arriba, abajo = 0, n - 1
    num = 1

    while izquierda <= derecha and arriba <= abajo:
        for i in range(izquierda, derecha + 1):
            matriz[arriba][i] = num
            num += 1
        arriba += 1

        for i in range(arriba, abajo + 1):
            matriz[i][derecha] = num
            num += 1
        derecha -= 1

        for i in range(derecha, izquierda - 1, -1):
            matriz[abajo][i] = num
            num += 1
        abajo -= 1

        for i in range(abajo, arriba - 1, -1):
            matriz[i][izquierda] = num
            num += 1
        izquierda += 1

    return matriz

def matriz_zigzag(n):
    matriz = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                matriz[i][j] = num
                num += 1
        else:
            for j in range(n - 1, -1, -1):
                matriz[i][j] = num
                num += 1

    return matriz

def matriz_triangular_superior_derecha(n):
    matriz = [[0] * n for _ in range(n)]
    num = 1

    for i in range(n):
        for j in range(i, n):
            matriz[i][j] = num
            num += 1

    return matriz

# Función para mostrar la matriz
def imprimir_matriz(matriz):
    output.delete("1.0", tk.END)
    for fila in matriz:
        output.insert(tk.END, " ".join(f"{num:3}" for num in fila) + "\n")

# Función para generar matriz según la selección
def generar_matriz():
    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("El tamaño debe ser un entero positivo.")
    except ValueError:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Por favor, ingresa un número entero positivo.")
        return

    tipo_matriz = matriz_tipo.get()
    if tipo_matriz == "Caracol":
        matriz = matriz_caracol(n)
    elif tipo_matriz == "Zigzag":
        matriz = matriz_zigzag(n)
    elif tipo_matriz == "Triangular Superior Derecha":
        matriz = matriz_triangular_superior_derecha(n)
    
    imprimir_matriz(matriz)

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Generador de Matrices")

# Entrada de tamaño de la matriz
tk.Label(root, text="Tamaño de la matriz (n):").grid(row=0, column=0, padx=5, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1, padx=5, pady=5)

# Selección de tipo de matriz
tk.Label(root, text="Tipo de Matriz:").grid(row=1, column=0, padx=5, pady=5)
matriz_tipo = ttk.Combobox(root, values=["Caracol", "Zigzag", "Triangular Superior Derecha"])
matriz_tipo.grid(row=1, column=1, padx=5, pady=5)
matriz_tipo.set("Caracol")

# Botón para generar la matriz
btn_generar = tk.Button(root, text="Generar Matriz", command=generar_matriz)
btn_generar.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

# Área de salida para mostrar la matriz
output = tk.Text(root, width=20, height=10, font=("Courier", 12))
output.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
