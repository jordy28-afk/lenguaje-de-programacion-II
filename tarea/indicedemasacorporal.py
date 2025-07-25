matriz1 = []
matriz2 = []
matriz_suma = []

def leer_matriz(n, nombre_matriz):
    global matriz1, matriz2
    matriz = []
    print(f"Ingrese los elementos de la matriz {nombre_matriz}:")
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    if nombre_matriz == "A":
        matriz1 = matriz
    elif nombre_matriz == "B":
        matriz2 = matriz

def sumar_matrices(n):
    global matriz1, matriz2, matriz_suma
    matriz_suma = []
    for i in range(n):
        fila_suma = []
        for j in range(n):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma)
        matriz_suma.append(fila_suma)

def mostrar_matriz(matriz, nombre_matriz):
    print(f"\nMatriz {nombre_matriz}:")
    for fila in matriz:
        print(" ".join(map(str, fila)))

def main():
    global matriz1, matriz2, matriz_suma
    n = int(input("Ingrese el tamaño de las matrices (n ): "))
    leer_matriz(n, "A")
    leer_matriz(n, "B")

    sumar_matrices(n)

    mostrar_matriz(matriz1, "A")
    mostrar_matriz(matriz2, "B")
    mostrar_matriz(matriz_suma, "Suma")

if __name__ == "__main__":
    main()
