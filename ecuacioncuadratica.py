"""import cmath
def ecuacion_cuadratica(a, b, c):
    if a == 0:
        if b == 0:
            return  if c != 0 else 
        return f"La solución es única: x = {-c / b}"
    discriminante = cmath.sqrt(b**2 - 4*a*c)
    x1 = (-b + discriminante) / (2 * a)
    x2 = (-b - discriminante) / (2 * a)
    return x1, x2
a, b, c = 2, 9, 10
soluciones = ecuacion_cuadratica(a, b, c)
print(f"Las soluciones son: x1 = {soluciones[0]}, x2 = {soluciones[1]}")"""
"""import math 
# funcion que resuelve la ecuacion
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x = ecu(a, b, c)
print("x =", x)"""

"""import math 
# funcino que resuelve la ecuacion
def ecu(a, b, c):
    d = b**2 - 4 * a * c  
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
    return x1, x2, d 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
x1, x2, discriminante = ecu(a, b, c)
print("x1 =", x1)
print("x2 =", x2)
print("Discriminante =", discriminante)"""



"""import math 
# funcino que resuelve la ecuacion
def ecu(a, b, c):
    d = b**2 - 4 * a * c  
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d 
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if discriminante == 0:
    x, discriminante = ecu(a, b, c)
    print("x =", x)
    print("Discriminante =", discriminante)
else:
    x1, x2, discriminante = ecu(a, b, c)
    print("x1 =", x1)
    print("x2 =", x2)
    print("Discriminante =", discriminante) """


"""import math


# Función que resuelve la ecuación cuadrática
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Calcular el discriminante
discriminante = b**2 - 4 * a * c

# Imprimir los resultados
if discriminante == 0:
    x, discriminante = ecu(a, b, c)
    print("x =", x)
    print("Discriminante =", discriminante)
else:
    x1, x2, discriminante = ecu(a, b, c)
    print("x1 =", x1)
    print("x2 =", x2)
    print("Discriminante =", discriminante)"""


"""import math
import tkinter as tk
from tkinter import messagebox

# Función que resuelve la ecuación cuadrática
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d

# Función para calcular y mostrar resultados
def calcular():
    try:
        # Obtener valores de los campos de entrada
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Calcular el discriminante
        discriminante = b**2 - 4 * a * c

        # Calcular y mostrar resultados
        if discriminante == 0:
            x, discriminante = ecu(a, b, c)
            resultado.config(text=f"x = {x}\nDiscriminante = {discriminante}")
        else:
            x1, x2, discriminante = ecu(a, b, c)
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación Cuadrática")
ventana.geometry("400x300")

# Etiquetas y entradas
etiqueta_a = tk.Label(ventana, text="Valor de a:")
etiqueta_a.pack(pady=5)
entrada_a = tk.Entry(ventana)
entrada_a.pack(pady=5)

etiqueta_b = tk.Label(ventana, text="Valor de b:")
etiqueta_b.pack(pady=5)
entrada_b = tk.Entry(ventana)
entrada_b.pack(pady=5)

etiqueta_c = tk.Label(ventana, text="Valor de c:")
etiqueta_c.pack(pady=5)
entrada_c = tk.Entry(ventana)
entrada_c.pack(pady=5)

# Botón de cálculo
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(pady=10)

# Área de resultados
resultado = tk.Label(ventana, text="", font=("Arial", 12))
resultado.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()"""






"""import math
import tkinter as tk
from tkinter import messagebox

# Función que resuelve la ecuación cuadrática
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d

# Función para calcular y mostrar resultados
def calcular():
    try:
        # Obtener valores de los campos de entrada
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Calcular el discriminante
        discriminante = b**2 - 4 * a * c

        # Calcular y mostrar resultados
        if discriminante == 0:
            x, discriminante = ecu(a, b, c)
            resultado.config(text=f"x = {x}\nDiscriminante = {discriminante}")
        else:
            x1, x2, discriminante = ecu(a, b, c)
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("CALCULADORA ECUACIÓN CUADRATICA")
ventana.geometry("600x600")

# Marco principal para centrar contenido
marco_principal = tk.Frame(ventana, padx=50, pady=50)
marco_principal.pack(expand=True)

# Título
titulo = tk.Label(marco_principal, text="Calculadora de Ecuación Cuadrática", font=("Arial", 16, "bold"))
titulo.pack(pady=(0, 30))

# Etiquetas y entradas con más espacio
etiqueta_a = tk.Label(marco_principal, text="Valor de a:", font=("Arial", 12))
etiqueta_a.pack(pady=10)
entrada_a = tk.Entry(marco_principal, font=("Arial", 12), width=30)
entrada_a.pack(pady=10)

etiqueta_b = tk.Label(marco_principal, text="Valor de b:", font=("Arial", 12))
etiqueta_b.pack(pady=10)
entrada_b = tk.Entry(marco_principal, font=("Arial", 12), width=30)
entrada_b.pack(pady=10)

etiqueta_c = tk.Label(marco_principal, text="Valor de c:", font=("Arial", 12))
etiqueta_c.pack(pady=10)
entrada_c = tk.Entry(marco_principal, font=("Arial", 12), width=30)
entrada_c.pack(pady=10)

# Botón de cálculo con mejor estilo
boton_calcular = tk.Button(marco_principal, text="Calcular", command=calcular, 
                            font=("Arial", 12), width=20, 
                            bg="blue", fg="white")
boton_calcular.pack(pady=20)

# Área de resultados con más espacio y estilo
resultado = tk.Label(marco_principal, text="", font=("Arial", 14), 
                     bg="lightgray", width=40, height=4)
resultado.pack(pady=20)

# Iniciar la aplicación
ventana.mainloop()"""





"""import math
import tkinter as tk
from tkinter import messagebox, ttk

# Función que resuelve la ecuación cuadrática
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d

# Función para manejar el movimiento entre entradas
def mover_siguiente(event, siguiente):
    siguiente.focus()

# Función para calcular al presionar Enter en el último campo
def calcular_enter(event):
    calcular()

# Función para calcular y mostrar resultados
def calcular():
    try:
        # Obtener valores de los campos de entrada
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Calcular el discriminante
        discriminante = b**2 - 4 * a * c

        # Calcular y mostrar resultados
        if discriminante == 0:
            x, discriminante = ecu(a, b, c)
            resultado.config(text=f"x = {x}\nDiscriminante = {discriminante}")
        else:
            x1, x2, discriminante = ecu(a, b, c)
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación Cuadrática")
ventana.geometry("600x800")

# Crear pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

# Pestaña de Calculadora
pestaña_calculadora = ttk.Frame(notebook)
notebook.add(pestaña_calculadora, text="Calculadora")

# Pestaña de Ayuda
pestaña_ayuda = ttk.Frame(notebook)
notebook.add(pestaña_ayuda, text="Ayuda")

# Contenido de la pestaña de Calculadora
marco_calculadora = tk.Frame(pestaña_calculadora, padx=50, pady=50)
marco_calculadora.pack(expand=True)

# Título
titulo = tk.Label(marco_calculadora, text="Calculadora de Ecuación Cuadrática", font=("Arial", 16, "bold"))
titulo.pack(pady=(0, 30))

# Etiquetas y entradas
etiqueta_a = tk.Label(marco_calculadora, text="Valor de a:", font=("Arial", 12))
etiqueta_a.pack(pady=10)
entrada_a = tk.Entry(marco_calculadora, font=("Arial", 12), width=30)
entrada_a.pack(pady=10)
entrada_a.bind('<Return>', lambda event: mover_siguiente(event, entrada_b))

etiqueta_b = tk.Label(marco_calculadora, text="Valor de b:", font=("Arial", 12))
etiqueta_b.pack(pady=10)
entrada_b = tk.Entry(marco_calculadora, font=("Arial", 12), width=30)
entrada_b.pack(pady=10)
entrada_b.bind('<Return>', lambda event: mover_siguiente(event, entrada_c))

etiqueta_c = tk.Label(marco_calculadora, text="Valor de c:", font=("Arial", 12))
etiqueta_c.pack(pady=10)
entrada_c = tk.Entry(marco_calculadora, font=("Arial", 12), width=30)
entrada_c.pack(pady=10)
entrada_c.bind('<Return>', calcular_enter)

# Botón de cálculo
boton_calcular = tk.Button(marco_calculadora, text="Calcular", command=calcular, 
                            font=("Arial", 12), width=20, 
                            bg="blue", fg="white")
boton_calcular.pack(pady=20)

# Área de resultados
resultado = tk.Label(marco_calculadora, text="", font=("Arial", 14), 
                     bg="lightgray", width=40, height=4)
resultado.pack(pady=20)

# Contenido de la pestaña de Ayuda
marco_ayuda = tk.Frame(pestaña_ayuda, padx=50, pady=50)
marco_ayuda.pack(expand=True)

# Texto de ayuda
texto_ayuda = tk.Text(marco_ayuda, font=("Arial", 12), wrap=tk.WORD, width=50, height=20)
texto_ayuda.pack()

# Contenido de la explicación
explicacion = ""
ECUACIÓN CUADRÁTICA

Fórmula General:
x = [-b ± √(b² - 4ac)] / (2a)

Pasos para resolver:
1. Identifica los valores de a, b y c en la ecuación ax² + bx + c = 0
2. Sustituye los valores en la fórmula general
3. Calcula el discriminante (b² - 4ac)

Tipos de soluciones:
- Discriminante > 0: Dos soluciones reales diferentes
- Discriminante = 0: Una solución real (raíz doble)
- Discriminante < 0: Dos soluciones complejas

Ejemplo:
Para la ecuación x² - 5x + 6 = 0
a = 1, b = -5, c = 6
x = [5 ± √((-5)² - 4(1)(6))] / (2(1))
x1 = 3, x2 = 2

texto_ayuda.insert(tk.END, explicacion)
texto_ayuda.config(state=tk.DISABLED)  # Hacer el texto de solo lectura

# Iniciar la aplicación
ventana.mainloop()"""




""""import math
import tkinter as tk
from tkinter import messagebox, ttk

# Función que resuelve la ecuación cuadrática
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d

# Función para manejar el movimiento entre entradas
def mover_siguiente(event, siguiente):
    siguiente.focus()

# Función para calcular al presionar Enter en el último campo
def calcular_enter(event):
    calcular()

# Función para calcular y mostrar resultados
def calcular():
    try:
        # Obtener valores de los campos de entrada
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Calcular el discriminante
        discriminante = b**2 - 4 * a * c

        # Generar pasos de resolución
        pasos = f""
PASOS DE RESOLUCIÓN:

1. Ecuación: {a}x² + {b}x + {c} = 0

2. Fórmula General: 
   x = [-b ± √(b² - 4ac)] / (2a)

3. Sustitución de valores:
   a = {a}
   b = {b}
   c = {c}

4. Cálculo del Discriminante:
   Discriminante = b² - 4ac
   Discriminante = {b}² - 4({a})({c})
   Discriminante = {discriminante}
""

        # Calcular y mostrar resultados
        if discriminante > 0:
            x1, x2, _ = ecu(a, b, c)
            pasos += f""
5. Soluciones:
   x1 = {x1}
   x2 = {x2}
   
Tipo de Solución: Dos raíces reales diferentes""
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")
        
        elif discriminante == 0:
            x, _ = ecu(a, b, c)
            pasos += f""
5. Solución:
   x = {x}
   
Tipo de Solución: Una raíz real (raíz doble)""
            resultado.config(text=f"x = {x}\nDiscriminante = {discriminante}")
        
        else:
            x1, x2, _ = ecu(a, b, c)
            pasos += f""
5. Soluciones:
   x1 = {x1}
   x2 = {x2}
   
Tipo de Solución: Raíces complejas""
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")

        # Mostrar pasos en el área de pasos
        area_pasos.config(state=tk.NORMAL)
        area_pasos.delete('1.0', tk.END)
        area_pasos.insert(tk.END, pasos)
        area_pasos.config(state=tk.DISABLED)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación Cuadrática")
ventana.geometry("800x800")

# Crear pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

# Pestaña de Calculadora
pestaña_calculadora = ttk.Frame(notebook)
notebook.add(pestaña_calculadora, text="Calculadora")

# Pestaña de Ayuda
pestaña_ayuda = ttk.Frame(notebook)
notebook.add(pestaña_ayuda, text="Ayuda")

# Marco principal para la calculadora
marco_calculadora = tk.Frame(pestaña_calculadora)
marco_calculadora.pack(expand=True, fill="both", padx=20, pady=20)

# Dividir el marco en dos columnas
marco_izquierdo = tk.Frame(marco_calculadora, width=400)
marco_izquierdo.pack(side=tk.LEFT, expand=True, fill="both", padx=10)

marco_derecho = tk.Frame(marco_calculadora, width=400)
marco_derecho.pack(side=tk.RIGHT, expand=True, fill="both", padx=10)

# Título
titulo = tk.Label(marco_izquierdo, text="Calculadora de Ecuación Cuadrática", font=("Arial", 16, "bold"))
titulo.pack(pady=(0, 30))

# Etiquetas y entradas
etiqueta_a = tk.Label(marco_izquierdo, text="Valor de a:", font=("Arial", 12))
etiqueta_a.pack(pady=10)
entrada_a = tk.Entry(marco_izquierdo, font=("Arial", 12), width=30)
entrada_a.pack(pady=10)
entrada_a.bind('<Return>', lambda event: mover_siguiente(event, entrada_b))

etiqueta_b = tk.Label(marco_izquierdo, text="Valor de b:", font=("Arial", 12))
etiqueta_b.pack(pady=10)
entrada_b = tk.Entry(marco_izquierdo, font=("Arial", 12), width=30)
entrada_b.pack(pady=10)
entrada_b.bind('<Return>', lambda event: mover_siguiente(event, entrada_c))

etiqueta_c = tk.Label(marco_izquierdo, text="Valor de c:", font=("Arial", 12))
etiqueta_c.pack(pady=10)
entrada_c = tk.Entry(marco_izquierdo, font=("Arial", 12), width=30)
entrada_c.pack(pady=10)
entrada_c.bind('<Return>', calcular_enter)

# Botón de cálculo
boton_calcular = tk.Button(marco_izquierdo, text="Calcular", command=calcular, 
                            font=("Arial", 12), width=20, 
                            bg="blue", fg="white")
boton_calcular.pack(pady=20)

# Área de resultados
resultado = tk.Label(marco_izquierdo, text="", font=("Arial", 14), 
                     bg="lightgray", width=40, height=4)
resultado.pack(pady=20)

# Área de pasos de resolución
etiqueta_pasos = tk.Label(marco_derecho, text="Pasos de Resolución", font=("Arial", 14, "bold"))
etiqueta_pasos.pack(pady=10)

area_pasos = tk.Text(marco_derecho, font=("Arial", 10), wrap=tk.WORD, width=50, height=30)
area_pasos.pack(pady=10)
area_pasos.config(state=tk.DISABLED)

# [Resto del código de la pestaña de Ayuda se mantiene igual que en el ejemplo anterior]

# Iniciar la aplicación
ventana.mainloop()"""


import math
import tkinter as tk
from tkinter import messagebox, ttk

# Función que resuelve la ecuación cuadrática
def ecu(a, b, c):
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2, d
    elif d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        return x, d
    else:
        x1 = (-b + math.sqrt(abs(d)) * 1j) / (2 * a)
        x2 = (-b - math.sqrt(abs(d)) * 1j) / (2 * a)
        return x1, x2, d

# Función para manejar el movimiento entre entradas
def mover_siguiente(event, siguiente):
    siguiente.focus()

# Función para calcular al presionar Enter en el último campo
def calcular_enter(event):
    calcular()

# Función para calcular y mostrar resultados
def calcular():
    try:
        # Obtener valores de los campos de entrada
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())

        # Calcular el discriminante
        discriminante = b**2 - 4 * a * c

        # Generar pasos de resolución
        pasos = f"""
PASOS DE RESOLUCIÓN:

1. Ecuación: {a}x² + {b}x + {c} = 0

2. Fórmula General: 
   x = [-b ± √(b² - 4ac)] / (2a)

3. Sustitución de valores en la fórmula general:
   x = [ -({b}) ± √({b}² - 4 * ({a}) * ({c})) ] / (2 * ({a}))

4. Simplificando la expresión dentro de la raíz cuadrada:
   x = [ -({b}) ± √({discriminante}) ] / (2 * ({a}))

"""

        # Calcular y mostrar resultados
        if discriminante > 0:
            x1, x2, _ = ecu(a, b, c)
            pasos += f"""
5. Calculando las dos soluciones:
   x1 = [ -({b}) + √({discriminante}) ] / (2 * ({a})) = {x1}
   x2 = [ -({b}) - √({discriminante}) ] / (2 * ({a})) = {x2}

Tipo de Solución: Dos raíces reales diferentes"""
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")
        
        elif discriminante == 0:
            x, _ = ecu(a, b, c)
            pasos += f"""
5. Calculando la única solución:
   x = [ -({b}) + √({discriminante}) ] / (2 * ({a})) = {x}

Tipo de Solución: Una raíz real (raíz doble)"""
            resultado.config(text=f"x = {x}\nDiscriminante = {discriminante}")
        
        else:
            x1, x2, _ = ecu(a, b, c)
            pasos += f"""
5. Calculando las dos soluciones complejas:
   x1 = [ -({b}) + √({discriminante}) ] / (2 * ({a})) = {x1}
   x2 = [ -({b}) - √({discriminante}) ] / (2 * ({a})) = {x2}

Tipo de Solución: Raíces complejas"""
            resultado.config(text=f"x1 = {x1}\nx2 = {x2}\nDiscriminante = {discriminante}")

        # Mostrar pasos en el área de pasos
        area_pasos.config(state=tk.NORMAL)
        area_pasos.delete('1.0', tk.END)
        area_pasos.insert(tk.END, pasos)
        area_pasos.config(state=tk.DISABLED)

        # Agregar la ecuación al historial
        historial.append(f"{a}x² + {b}x + {c} = 0")
        actualizar_historial()
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos")

# Función para actualizar el historial
def actualizar_historial():
    historial_listbox.delete(0, tk.END)
    for ecuacion in historial:
        historial_listbox.insert(tk.END, ecuacion)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ecuación Cuadrática")
ventana.geometry("800x800")

# Crear pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

# Pestaña de Calculadora
pestaña_calculadora = ttk.Frame(notebook)
notebook.add(pestaña_calculadora, text="Calculadora")

# Pestaña de Historial
pestaña_historial = ttk.Frame(notebook)
notebook.add(pestaña_historial, text="Historial")

# Marco principal para la calculadora
marco_calculadora = tk.Frame(pestaña_calculadora)
marco_calculadora.pack(expand=True, fill="both", padx=20, pady=20)

# Dividir el marco en dos columnas
marco_izquierdo = tk.Frame(marco_calculadora, width=400)
marco_izquierdo.pack(side=tk.LEFT, expand=True, fill="both", padx=10)

marco_derecho = tk.Frame(marco_calculadora, width=400)
marco_derecho.pack(side=tk.RIGHT, expand=True, fill="both", padx=10)

# Título
titulo = tk.Label(marco_izquierdo, text="Calculadora de Ecuación Cuadrática", font=("Arial", 16, "bold"))
titulo.pack(pady=(0, 30))

# Etiquetas y entradas
etiqueta_a = tk.Label(marco_izquierdo, text="Valor de a:", font=("Arial", 12))
etiqueta_a.pack(pady=10)
entrada_a = tk.Entry(marco_izquierdo, font=("Arial", 12), width=30)
entrada_a.pack(pady=10)
entrada_a.bind('<Return>', lambda event: mover_siguiente(event, entrada_b))

etiqueta_b = tk.Label(marco_izquierdo, text="Valor de b:", font=("Arial", 12))
etiqueta_b.pack(pady=10)
entrada_b = tk.Entry(marco_izquierdo, font=("Arial", 12), width=30)
entrada_b.pack(pady=10)
entrada_b.bind('<Return>', lambda event: mover_siguiente(event, entrada_c))

etiqueta_c = tk.Label(marco_izquierdo, text="Valor de c:", font=("Arial", 12))
etiqueta_c.pack(pady=10)
entrada_c = tk.Entry(marco_izquierdo, font=("Arial", 12), width=30)
entrada_c.pack(pady=10)
entrada_c.bind('<Return>', calcular_enter)

# Botón de cálculo
boton_calcular = tk.Button(marco_izquierdo, text="Calcular", command=calcular, 
                            font=("Arial", 12), width=20, 
                            bg="blue", fg="white")
boton_calcular.pack(pady=20)

# Área de resultados
resultado = tk.Label(marco_izquierdo, text="", font=("Arial", 14), 
                     bg="lightgray", width=40, height=4)
resultado.pack(pady=20)

# Área de pasos de resolución
etiqueta_pasos = tk.Label(marco_derecho, text="Pasos de Resolución", font=("Arial", 14, "bold"))
etiqueta_pasos.pack(pady=10)

area_pasos = tk.Text(marco_derecho, font=("Arial", 10), wrap=tk.WORD, width=50, height=30)
area_pasos.pack(pady=10)
area_pasos.config(state=tk.DISABLED)

# Historial de ecuaciones
historial = []

# Marco para el historial en la pestaña Historial
marco_historial = tk.Frame(pestaña_historial)
marco_historial.pack(expand=True, fill="both", padx=20, pady=20)

# Listbox para mostrar el historial
historial_listbox = tk.Listbox(marco_historial, font=("Arial", 12), width=50, height=20)
historial_listbox.pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
