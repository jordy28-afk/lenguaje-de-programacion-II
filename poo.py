"""class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def hablar(self, mensaje):
        print(f"{self.nombre} dice: {mensaje}")

    def caminar(self, distancia):
        print(f"{self.nombre} ha caminado {distancia} metros")

    def dormir(self, horas):
        print(f"{self.nombre} ha dormido {horas} horas")


# Creación de objetos
persona1 = Persona("Juan", 25, 1.75)
persona2 = Persona("María", 30, 1.55)

print("\n---- Acciones de Juan ---")
persona1.hablar("Hola, ¿cómo estás?")
persona1.caminar(500)
persona1.dormir(8)

print("\n---- Acciones de María ---")
persona2.hablar("Hola, buenos días")
persona2.caminar(300)
persona2.dormir(7)"""




""""class Doctor:
    def __init__(self, nombre, edad, especialidad):
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad

    def presentarse(self):
        print(f"Hola, soy el Dr. {self.nombre}, tengo {self.edad} años y me especializo en {self.especialidad}.")

    def atender_paciente(self, paciente):
        print(f"Dr. {self.nombre} está atendiendo al paciente {paciente}.")

    def recetar_medicina(self, medicina):
        print(f"Dr. {self.nombre} ha recetado: {medicina}.")

    def descansar(self, horas):
        print(f"Dr. {self.nombre} ha descansado {horas} horas.")


doctor1 = Doctor("fonng", 45, "Pediatria")
doctor2 = Doctor("mili", 38, "Cardiologia")
doctor3 = Doctor("dulido", 45, "otorrinolaringologia")

print("\n--- Información del Doctor 1 ---")
doctor1.presentarse()
doctor1.atender_paciente("mili")
doctor1.recetar_medicina("Paracetamol")
doctor1.descansar(6)

print("\n--- Información del Doctor 2 ---")
doctor2.presentarse()
doctor2.atender_paciente("fonng")
doctor2.recetar_medicina("Aspirina")
doctor2.descansar(7)

print("\n--- Información del Doctor 3---")
doctor2.presentarse()
doctor2.atender_paciente("dulido")
doctor2.recetar_medicina("sal de andrews")
doctor2.descansar(8)"""

"""import tkinter as tk
from tkinter import messagebox

class Doctor:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia

    def mostrar_informacion(self):
        return f"Nombre del doctor: {self.nombre}\nEspecialidad: {self.especialidad}\nExperiencia: {self.experiencia} años"

    def atender_paciente(self, paciente):
        return f"El Dr. {self.nombre} está atendiendo al paciente {paciente}"

    def calcular_salario(self):
        salario_base = 2000
        bono_experiencia = self.experiencia * 150
        salario_total = salario_base + bono_experiencia
        return salario_total

def registrar_doctor():
    nombre = entry_nombre.get()
    especialidad = entry_especialidad.get()
    try:
        experiencia = int(entry_experiencia.get())
    except ValueError:
        messagebox.showerror("Error", "La experiencia debe ser un número entero.")
        return

    global doctor
    doctor = Doctor(nombre, especialidad, experiencia)
    messagebox.showinfo("Registro exitoso", "Doctor registrado correctamente.")

def mostrar_info():
    if doctor:
        messagebox.showinfo("Información del Doctor", doctor.mostrar_informacion())

def atender():
    paciente = entry_paciente.get()
    if doctor and paciente:
        messagebox.showinfo("Atención al Paciente", doctor.atender_paciente(paciente))
    else:
        messagebox.showerror("Error", "Debe registrar al doctor y escribir el nombre del paciente.")

def calcular_salario():
    if doctor:
        salario = doctor.calcular_salario()
        messagebox.showinfo("Salario", f"Salario total del doctor: {salario} soles")

# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Doctor")

# Entradas
tk.Label(ventana, text="Nombre del Doctor:").grid(row=0, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Especialidad:").grid(row=1, column=0)
entry_especialidad = tk.Entry(ventana)
entry_especialidad.grid(row=1, column=1)

tk.Label(ventana, text="Años de experiencia:").grid(row=2, column=0)
entry_experiencia = tk.Entry(ventana)
entry_experiencia.grid(row=2, column=1)

tk.Button(ventana, text="Registrar Doctor", command=registrar_doctor).grid(row=3, columnspan=2, pady=5)

# Paciente
tk.Label(ventana, text="Nombre del Paciente:").grid(row=4, column=0)
entry_paciente = tk.Entry(ventana)
entry_paciente.grid(row=4, column=1)

# Botones de acciones
tk.Button(ventana, text="Mostrar Información", command=mostrar_info).grid(row=5, columnspan=2, pady=5)
tk.Button(ventana, text="Atender Paciente", command=atender).grid(row=6, columnspan=2, pady=5)
tk.Button(ventana, text="Calcular Salario", command=calcular_salario).grid(row=7, columnspan=2, pady=5)

# Inicializar variable global
doctor = None

ventana.mainloop()"""

class estudiante :
    def __init__(self,nombre,edad,carrera):
        self.nombre =nombre
        self.edad = edad
        self.carrera = carrera
        self.notas=[]

    def agregar_notas(self,notas):
        self.notas.append(notas)

    def promedio_nota(self):
        if len(self.notas)== 0:
            return 0
        return sum (self.notas)/len(self.notas)
    
    def es_aprobado(self):
        promedio =self.promedio_nota()
        if promedio >=11:
            return True
        return False
    def mostrar_informacion(self):
        info = f"nombre:{self.nombre}\nedad:{self.edad}\ncarrera:{self.carrera}\nnotas:{self.notas}\n "
        info+= f"promedio:{self.promedio_nota():2f}\n aprobado: {'si'if self.es_aprobado()else'no'}"
        return info

estudiante1 = estudiante ("juan perez",20,"ingenieria estadistica e informatica")
estudiante1.agregar_notas(18)
estudiante1.agregar_notas(17)
estudiante1.agregar_notas(19)
estudiante1.agregar_notas(14)

print(estudiante1.mostrar_informacion())

