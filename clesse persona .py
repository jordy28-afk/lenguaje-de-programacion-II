class persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    # getter para nombre
    def obtener_nombre(self):
        return self.__nombre

    # getter para edad
    def obtener_edad(self):
        return self.__edad

    # setter para edad
    def establecer_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("edad no valida")
    
    def es_mayor_de_edad(self):
        return self.__edad>=18
    
    def mostrar_datos(self):
        print(f"nombre: {self.__nombre},edad: {self.__edad}")
    
    def complir_anios (self):
        self.__edad+=1
        print(f"feliz cumpleanios")

persona1 = persona("pedro", 25)
persona1.mostrar_datos()

if persona1.es_mayor_de_edad():
    print("es mayor de edad")
else:
    print("es menor de edad")