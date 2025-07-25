"""def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

with open('nombres.txt', 'r') as archivo:
    lineas = [linea.strip() for linea in archivo]  

print(":")
for linea in lineas:
    print(linea)

objetivo = input("\nIngresa el texto a buscar: ")

indice = busqueda_lineal(lineas, objetivo)

if indice != -1:
    print(f'la cadena "{objetivo}" se encuentra en la linea {indice + 1}.')
else:
    print(f'la cadena "{objetivo}" el archivo no existe .')"""
def busqueda_lineal(lista, objetivo):
    for i, elemento in enumerate(lista):
        if objetivo.lower() in elemento.lower():
            return i
    return -1

with open('nombres2.txt', 'r') as archivo:
    lineas = [linea.strip() for linea in archivo]  

print("Contenido del archivo:")
for linea in lineas:
    print(linea)

textos_busqueda = []
while True:
    texto = input("\nbuscar : ")
    if texto == "":
        break
    textos_busqueda.append(texto)
print("\nbusqueda:")
for objetivo in textos_busqueda:
    indice = busqueda_lineal(lineas, objetivo)
    if indice != -1:
        print(f'la cadena "{objetivo}" se encuentra en la linea {indice + 1}: {lineas[indice]}')
    else:
        print(f'la cadena "{objetivo}" no existe .')
