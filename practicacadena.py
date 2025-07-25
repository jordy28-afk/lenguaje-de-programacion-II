def busqueda_lineal(lista, objetivo):
    # Iterar sobre la lista con índice y elemento
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i  # Devuelve el índice si encuentra el elemento
    return -1  # Devuelve -1 si no encuentra el elemento

# Lista de cadenas
cadenas = [
    "universidad nacional mayor de san marcos",
    "universidad nacional del altiplano",
    "universidad nacional de ingeniería",
    "universidad nacional de san agustín"
]

# Elemento a buscar
cadena_objetivo = "universidad nacional del altiplano"

# Realizar búsqueda
indice = busqueda_lineal(cadenas, cadena_objetivo)

# Imprimir resultado
if indice != -1:
    print(f'La cadena "{cadena_objetivo}" se encuentra en el índice {indice}.')
else:
    print(f'La cadena "{cadena_objetivo}" no se encuentra en la lista.')
