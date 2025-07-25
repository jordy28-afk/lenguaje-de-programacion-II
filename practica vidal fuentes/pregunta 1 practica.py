arreglo=input("ingresa los numeros :")
arreglo =[int(x) for x in arreglo.split()]

i=0
j=0
def ordenamiento_burbuja(arreglo):
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    return arreglo

resultado=ordenamiento_burbuja(arreglo)
print(resultado)
with open('orden.txt', 'w') as archivo:
    archivo.write(f"La encriptación es:\n{resultado}")
