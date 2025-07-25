class persona :
    def __init__(self,nombre):
        self.nombre = nombre 
        print (f"hola soy {self.nombre}")
    def __del__ (self):
        print (f"{self.nombre} feu eliminado")

persona1 = persona("luis")

del persona1 
print ("fin del programa ")
