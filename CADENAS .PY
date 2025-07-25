#creacion de cadenas 
cadena1 ="hola mundo"
cadena2 ='hola mundo'
print(cadena1)
print(cadena2)

#acceso a caracteres 
cadena = "python"
print(cadena[0])
print(cadena[-1])

#elicing 
cadena = "python"
subcadena = cadena [0:3]
print(subcadena)

#ejemplo 
cadena ="univercidad nacional del altiplano"
subcadena = cadena [12:20]
print(subcadena)

#concatenacion +
saludo = "hola"
nombre = "mundo"
mensaje =saludo+" , "+nombre
print(mensaje)

#ejemplo
nombre1="ANTHONY JORDY"
ap1="vidal"
ap2="fuentes"
mensaje=nombre1+" , "+ap1+" , "+ap2
print(mensaje)

#repeticion 
cadena = "python  "
repetida= cadena * 5
print(repetida)

#longitud de una cadena 
cadena = 'python'
print(len(cadena))
#metodos comunes para manejar cadenas
#1.-uper()
cadena="python"
print(cadena.upper())

#2lower()
cadena="PYTHON"
print(cadena.lower())

#3strip()
cadena="python"
print(cadena.strip())

#4replace(old,new)
cadena="hola,mundo"
print(cadena.replace("mundo","hola"))

# split()
cadena="manzana , pera,  platano"
frutas=cadena.split(",")
print(frutas)

# join 
lista= ["manzana" , "pera" , "plátano"]
print(",".join(lista))

# 7 find busacar
cadena="hoala, mundo"
print(cadena.find("mundo"))

#formateo de cadenas ............................................
#1. usando el operador %
nombre= "jordy"
paterno="vidal"
edad=20
mensaje= "mi nommbre es %s %s y tengo %d años. "%(nombre ,paterno,edad)
print(mensaje)

#2 str.format()
mensaje="mi nombre es {} y tengo {} años.".format(nombre,edad)
print(mensaje)
 
#f-string 
mensaje=f"mi nombre es {nombre} tengo {edad} años."
print(mensaje) 

#caracteres especiales 
cadena ="hola\n\nmundo"
print(cadena)

