"""import re

# Función para buscar un patrón en un texto
def buscar_patron(texto, patron):
    # Usamos re.search para buscar el patrón en el texto
    resultado = re.search(patron, texto)
    if resultado:
        return resultado.start()  # Retorna el índice de inicio del patrón
    return -1

# Texto y patrón a buscar
texto = "Hola, este es un ejemplo de búsqueda usando expresiones regulares."
patron = r"expresiones"  # Puedes usar cualquier expresión regular válida

# Llamamos a la función
indice = buscar_patron(texto, patron)

# Mostramos el resultado
if indice != -1:
    print(f"El patrón '{patron}' se encuentra en el índice {indice}.")
else:
    print(f"El patrón '{patron}' no se encontró en el texto.")"""
#irregular 
# Función para buscar un patrón en un texto
def buscar_patron_sin_regex(texto, patron):
    n = len(texto)
    m = len(patron)

    # Recorrer cada posible posición de inicio en el texto
    for i in range(n - m + 1):
        # Comparar el patrón con la subcadena actual
        if texto[i:i + m] == patron:
            return i  # Retorna el índice donde comienza el patrón
    return -1  # Retorna -1 si no encuentra el patrón

# Texto y patrón a buscar
texto = "univerciad nacional del altiplano."
patron = "nacional"

# Llamar a la función
indice = buscar_patron_sin_regex(texto, patron)

# Mostrar el resultado
if indice != -1:
    print(f"El patrón '{patron}' se encuentra en el índice {indice}.")
else:
    print(f"El patrón '{patron}' no se encuentra en el texto.")
