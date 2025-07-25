def matriz_triangular_superior_derecha(n):
    matriz = [[0] * n for _ in range(n)]
    num = 5

    for i in range(n):
        for j in range(i, n):
            matriz[i][j] = num
            num += 1

    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{num:3}" for num in fila))

n = 5
matriz_triangular = matriz_triangular_superior_derecha(n)
imprimir_matriz(matriz_triangular)
