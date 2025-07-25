class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []
    
    def agregar_nota(self, nota):
        self.notas.append(nota)
     
    def promedio(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0
    
    def es_aprobado(self):
        return self.promedio() >= 10.5
    
    def mostrar_informacion(self):
        info = f"Nombre: {self.nombre}\nEdad: {self.edad}\nCarrera: {self.carrera}\nNotas: {self.notas}\n"
        info += f"Promedio: {self.promedio():.2f}\nAprobado: {'Sí' if self.es_aprobado() else 'No'}"
        print(info)

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
estudiante = Estudiante(nombre, edad, carrera)

cantidad_notas = int(input("Ingrese la cantidad de notas: "))
for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    estudiante.agregar_nota(nota)

print("==== Información del Estudiante ====")
estudiante.mostrar_informacion()
