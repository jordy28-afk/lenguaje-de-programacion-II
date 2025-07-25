def hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de las Torres de Hanoi de forma recursiva.

    Args:
        n: Número de discos.
        origen: Torre de origen.
        destino: Torre de destino.
        auxiliar: Torre auxiliar.
    """

    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        hanoi(n-1, origen, auxiliar, destino)
        print(f"Mover disco {n} de {origen} a {destino}")
        hanoi(n-1, auxiliar, destino, origen)

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de discos: "))
    hanoi(n, 'A', 'C', 'B')