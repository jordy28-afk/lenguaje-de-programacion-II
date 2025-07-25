from abc import ABC, abstractclassmethod

class figura (ABC):
    @abstractclassmethod
    def calcular_area (self):
        pass

class cuadrado (figura):
    def __init__(self,lado):
        if lado <=0:
            raise ValueError ("El lado debe ser mayor que cero")
        self.lado =lado
    def calcular_area (self):
        return self.lado**2
    

class triangulo  (figura):
    def __init__(self,base ,altura):
        if base<=0 or altura<=0:
             raise ValueError ("base y altura deve ser mayor que cero ")
        self.base = base 
        self.altura = altura
    def calcular_area (self):
        return (self.base * self.altura)/2
    
def calcular_area_figura():
    try:
        figura = input("ingrese cuadrado o triangulo ").lower
        if figura=="cuadrado":
            lado = float(input("lado del cuadrado : "))
            c = cuadrado(lado) 
            print(" area del cuadrado : ", c.calcular_area())
        elif figura =="triangulo":
            base = float(input("base del triangulo"))
            altura = float(input("la altura  del triangulo"))
            t = triangulo(base ,altura )
            print("area del traingulo : ",t.calcular_area())
        else:
            print("figura reconocida")
    except ValueError as ve:
        print("Error",ve)
    except Exception as e:
        print("ocurrio un error inesperado ", e)
    calcular_area_figura
