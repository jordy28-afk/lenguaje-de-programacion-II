"""texto="hola mundo"
minusculas = texto.lower()
mayusculas = texto.upper()
print(minusculas)
print(mayusculas)
#combercion de un solo caracter a su valor Unicode o cici
caracter = 'A'
valor_unicode = ord(caracter)
print(valor_unicode)
#comberción de valores numericos a caracteres (unicode a caracter)
 
codigo =65
caracter =chr (codigo)
print(caracter)"""
#generar el codigo ascci
"""print("codigo ASCII | caracter")"""
"""for i in range(256):
    caracter=chr(i)
    print(f"{i}   |    {caracter}")"""

#4 combercion de cadenas en base 64(encriptacion)
import base64
texto ="hola mundo"
texto_base64=base64.b64encode(texto.encode('utf-8'))
print(texto_base64)
textodecodificado = base64.b64decode(texto_base64).decode ('utf-8')
print(textodecodificado)  
#co,bercion de caracteres en una cadena a otras 
# representacion de caracteres  (como rot13)
import codecs
texto ="hola mundo"
texto_rot13 = codecs.encode(texto, 'rot_13')
print(texto_rot13)
texto_decodificado = codecs.encode(texto_rot13,"rot_13")
print(texto_decodificado)
import base64
#para desincriptar
codigo_base64 = b'RElDRSBRVUUgTk8sIEVTVEFNT1MgIEVOQ1JJUFRBTkRP'
texto_decodificado = base64.b64decode(codigo_base64).decode('utf-8')
print("Texto decodificado:", texto_decodificado)


 