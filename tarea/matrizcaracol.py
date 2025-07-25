def matriz_caracol(n):
    matriz = [[0]*n for _ in range(n)]

    izquierda,derecha=0, n-1
    arriba,abajo=0,n-1
    num=1

    while izquierda<=derecha and arriba<=abajo:
        for i in  range (izquierda,derecha+1):
            matriz[arriba][i]=num
            num=num+1
        arriba=arriba+1

        for i in  range (arriba,abajo+1):
            matriz[i][derecha]=num
            num=num+1
        derecha=derecha-1
        
        for i in  range (derecha,izquierda-1,-1):
            matriz[abajo][i]=num
            num=num+1
        abajo=abajo-1

        for i in  range (abajo,arriba-1,-1):
            matriz[i][izquierda]=num
            num=num+1
        izquierda=izquierda+1

    return matriz 
def imprimir_matriz(matriz):
    for fila in matriz:
        print("".join(f"{num:3}"for num in fila))

matriz_caracol_espiral = matriz_caracol(5)
imprimir_matriz(matriz_caracol_espiral)
        