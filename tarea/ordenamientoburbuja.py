"""def ordenamiento_burbuja(lista):
    n = 6
    for i in range(n):
        for j in range(0, n - i - 2):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
lista=[64,34,25,12,22]
resultado=ordenamiento_burbuja(lista)
print(resultado)"""
def ordenamiento_burbuja(nueva_lista):
    n = len(nueva_lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nueva_lista[j] > nueva_lista[j + 1]:
                nueva_lista[j], nueva_lista[j + 1] = nueva_lista[j + 1], nueva_lista[j]
    return nueva_lista


# Ejemplo 2: Pidiendo la lista por input
nueva_lista = input("Ingresa los números separados por espacios: ").split()
nueva_lista = [int(num) for num in nueva_lista]
resultado = ordenamiento_burbuja(nueva_lista)
print(resultado)
                
