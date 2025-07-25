from typing import TypeVar, Generic

T = TypeVar("T", int, float)

class OperacionMatematica(Generic[T]):
    def calcular(self, a: T, b: T) -> T:
        raise NotImplementedError("Método calcular() no implementado")

class Suma(OperacionMatematica[T]):
    def calcular(self, a: T, b: T) -> T:
        return a + b

class Resta(OperacionMatematica[T]):
    def calcular(self, a: T, b: T) -> T:
        return a - b

class Multiplicacion(OperacionMatematica[T]):
    def calcular(self, a: T, b: T) -> T:
        return a * b

class divicion (OperacionMatematica[T]):
    def calcular(self, a: T,b:T)-> T:
        return a/b

def main():
    numeros = [
        (5, 3),    
        (10, 2),    
        (8, 4),     
        (10,5 )      
    ]
    
    operaciones = {
        "Suma": Suma(),
        "Resta": Resta(),
        "Multiplicación": Multiplicacion(),
        "División": divicion()
    }
    
    print()
    
    for i, (a, b) in enumerate(numeros, 1):
        print(f"\nConjunto {i}: {a} y {b}")
        
        for nombre, operacion in operaciones.items():
            try:
                resultado = operacion.calcular(a, b)
                print(f"{nombre}: {resultado}")
            except ValueError as e:
                print(f"{nombre}: Error - {str(e)}")

if __name__ == "__main__":
    main()