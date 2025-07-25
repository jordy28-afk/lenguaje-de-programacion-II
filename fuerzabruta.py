def busqueda_fuerza_bruta(texto, patron):
    n = len(texto)  
    m = len(patron)  

    for i in range(n - m + 1):  
        j = 0
        while j < m and texto[i + j] == patron[j]: 
            j += 1
        if j == m:  
            return i  
    return -1  

texto = "hola, este es un ejemplo de busqueda de fuerza bruta"
patron = "fuerza"

resultado = busqueda_fuerza_bruta(texto, patron)

if resultado != -1:
    print(f'El patrón "{patron}" se encuentra en la posición {resultado}.')
else:
    print(f'El patrón "{patron}" no se encuentra en el texto.')
