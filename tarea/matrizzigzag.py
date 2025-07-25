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

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(f"{num:3}" for num in fila))

matriz_zigzag_espiral = matriz_zigzag(5)
imprimir_matriz(matriz_zigzag_espiral)
