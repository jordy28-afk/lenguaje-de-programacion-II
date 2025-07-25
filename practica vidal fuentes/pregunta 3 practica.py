"""import base64
texto = "vive la vida antes que la vida te viva "
texto_base64 = base64.b64encode(texto.encode('utf-8')).decode('utf-8')
texto_desencriptado = base64.b64decode(texto_base64).decode('utf-8')
with open('nombres.txt', 'w') as archivo:
    archivo.write(f" encriptacion es:\n{texto_base64}\n")
    archivo.write(f"texto desencriptado es:\n{texto_desencriptado}")"""

import base64

def encriptar_y_guardar(texto):
  texto_base64 = base64.b64encode(texto.encode('utf-8')).decode('utf-8')
  texto_desencriptado = base64.b64decode(texto_base64).decode('utf-8')
  with open('nombres.txt', 'w') as archivo:
    archivo.write(f"encriptacion es:\n{texto_base64}\n")
    archivo.write(f"texto desencriptado es:\n{texto_desencriptado}")
texto = input("ingresa el de  encriptacion: ")
encriptar_y_guardar(texto)

print(" ")

    
