"""class Calculadora:
    def __init__(self, num1, num2):
        self._numero1 = num1
        self._numero2 = num2

    def suma(self):
        return self._numero1 + self._numero2

    def resta(self):
        return self._numero1 - self._numero2

    def multiplicacion(self):
        return self._numero1 * self._numero2

    def division(self):
        if self._numero2 == 0:
            return "¡Error! No se puede dividir por cero."
        return self._numero1 / self._numero2

    def mostrar_operaciones(self):
        print(f"Número 1: {self._numero1}")
        print(f"Número 2: {self._numero2}")
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")

try:
    num1 = int(input("Ingresa el primer número entero: "))
    num2 = int(input("Ingresa el segundo número entero: "))

    calc = Calculadora(num1, num2)
    calc.mostrar_operaciones()

    print("\nCambiando valores...")
    nuevo1 = int(input("Ingresa el nuevo valor para el primer número: "))
    nuevo2 = int(input("Ingresa el nuevo valor para el segundo número: "))

    calc = Calculadora(nuevo1, nuevo2)
    calc.mostrar_operaciones()

except ValueError:
    print("Por favor, ingresa solo números enteros válidos. No te me webees 😅")"""



"""import tkinter as tk
from tkinter import messagebox

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Colorida")
        self.root.geometry("400x500")
        self.root.configure(bg="#1a1a2e")  # Fondo azul oscuro
        
        # Variables para almacenar los números
        self.numero1 = tk.DoubleVar()
        self.numero2 = tk.DoubleVar()
        
        # Título
        titulo = tk.Label(root, text="Calculadora Colorida", font=("Arial", 18, "bold"), 
                         bg="#1a1a2e", fg="#e94560")  # Texto rojo brillante
        titulo.pack(pady=20)
        
        # Frame para entrada de datos
        frame_entrada = tk.Frame(root, bg="#16213e")  # Azul medio
        frame_entrada.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Etiquetas y campos de entrada
        tk.Label(frame_entrada, text="Primer número:", font=("Arial", 12), 
                bg="#16213e", fg="#f1f1f1").pack(pady=5)  # Texto blanco
        
        entrada1 = tk.Entry(frame_entrada, textvariable=self.numero1, font=("Arial", 12),
                           bg="#0f3460", fg="white", insertbackground="white")  # Campo azul
        entrada1.pack(pady=5, padx=20, fill="x")
        
        tk.Label(frame_entrada, text="Segundo número:", font=("Arial", 12), 
                bg="#16213e", fg="#f1f1f1").pack(pady=5)
        
        entrada2 = tk.Entry(frame_entrada, textvariable=self.numero2, font=("Arial", 12),
                          bg="#0f3460", fg="white", insertbackground="white")
        entrada2.pack(pady=5, padx=20, fill="x")
        
        # Frame para botones
        frame_botones = tk.Frame(root, bg="#1a1a2e")
        frame_botones.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Botones de operaciones
        btn_suma = tk.Button(frame_botones, text="Suma", command=lambda: self.calcular("suma"),
                           bg="#e94560", fg="white", font=("Arial", 12, "bold"), 
                           activebackground="#ff2e63", relief=tk.RAISED, width=10)
        btn_suma.grid(row=0, column=0, padx=10, pady=10)
        
        btn_resta = tk.Button(frame_botones, text="Resta", command=lambda: self.calcular("resta"),
                            bg="#e94560", fg="white", font=("Arial", 12, "bold"), 
                            activebackground="#ff2e63", relief=tk.RAISED, width=10)
        btn_resta.grid(row=0, column=1, padx=10, pady=10)
        
        btn_mult = tk.Button(frame_botones, text="Multiplicar", command=lambda: self.calcular("multiplicacion"),
                           bg="#e94560", fg="white", font=("Arial", 12, "bold"), 
                           activebackground="#ff2e63", relief=tk.RAISED, width=10)
        btn_mult.grid(row=1, column=0, padx=10, pady=10)
        
        btn_div = tk.Button(frame_botones, text="Dividir", command=lambda: self.calcular("division"),
                          bg="#e94560", fg="white", font=("Arial", 12, "bold"), 
                          activebackground="#ff2e63", relief=tk.RAISED, width=10)
        btn_div.grid(row=1, column=1, padx=10, pady=10)
        
        btn_todas = tk.Button(frame_botones, text="Todas las operaciones", command=self.mostrar_operaciones,
                            bg="#0f3460", fg="white", font=("Arial", 12, "bold"), 
                            activebackground="#256d85", relief=tk.RAISED)
        btn_todas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Frame para resultados
        self.frame_resultados = tk.Frame(root, bg="#0f3460")  # Azul más oscuro
        self.frame_resultados.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.label_resultado = tk.Label(self.frame_resultados, text="Resultado aparecerá aquí", 
                                      font=("Arial", 14), bg="#0f3460", fg="#f1f1f1", 
                                      wraplength=350, justify="left")
        self.label_resultado.pack(pady=10, padx=10)
        
    def calcular(self, operacion):
        try:
            num1 = self.numero1.get()
            num2 = self.numero2.get()
            
            calculadora = Calculadora(num1, num2)
            
            if operacion == "suma":
                resultado = calculadora.suma()
                self.label_resultado.config(text=f"Suma: {num1} + {num2} = {resultado}")
            elif operacion == "resta":
                resultado = calculadora.resta()
                self.label_resultado.config(text=f"Resta: {num1} - {num2} = {resultado}")
            elif operacion == "multiplicacion":
                resultado = calculadora.multiplicacion()
                self.label_resultado.config(text=f"Multiplicación: {num1} × {num2} = {resultado}")
            elif operacion == "division":
                resultado = calculadora.division()
                self.label_resultado.config(text=f"División: {num1} ÷ {num2} = {resultado}")
                
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos")
    
    def mostrar_operaciones(self):
        try:
            num1 = self.numero1.get()
            num2 = self.numero2.get()
            
            calculadora = Calculadora(num1, num2)
            
            resultado = f"Número 1: {num1}\n"
            resultado += f"Número 2: {num2}\n"
            resultado += f"Suma: {calculadora.suma()}\n"
            resultado += f"Resta: {calculadora.resta()}\n"
            resultado += f"Multiplicación: {calculadora.multiplicacion()}\n"
            resultado += f"División: {calculadora.division()}"
            
            self.label_resultado.config(text=resultado)
            
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos")


class Calculadora:
    def __init__(self, num1, num2):
        self._numero1 = num1
        self._numero2 = num2
    
    def suma(self):
        return self._numero1 + self._numero2
    
    def resta(self):
        return self._numero1 - self._numero2
    
    def multiplicacion(self):
        return self._numero1 * self._numero2
    
    def division(self):
        if self._numero2 == 0:
            return "¡Error! No se puede dividir por cero."
        return self._numero1 / self._numero2
    
    def mostrar_operaciones(self):
        print(f"Número 1: {self._numero1}")
        print(f"Número 2: {self._numero2}")
        print(f"Suma: {self.suma()}")
        print(f"Resta: {self.resta()}")
        print(f"Multiplicación: {self.multiplicacion()}")
        print(f"División: {self.division()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGUI(root)
    root.mainloop()"""


import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculadoraAvanzada:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Avanzada")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")
        
        # Tema de colores
        self.color_pantalla = "#2d2d42"
        self.color_boton_num = "#3b3b5b"
        self.color_boton_op = "#f5924a"  # naranja
        self.color_boton_func = "#e94560"  # rojo
        self.color_texto = "#ffffff"
        self.color_resultado = "#6ae4a9"  # verde claro
        
        # Variables
        self.expresion = ""
        self.resultado = 0
        self.memoria = 0
        self.historial = []
        
        # Crear widgets
        self.crear_widgets()
    
    def crear_widgets(self):
        # Frame para la pantalla
        frame_pantalla = tk.Frame(self.root, bg="#1e1e2e")
        frame_pantalla.pack(fill="both", padx=10, pady=10)
        
        # Historial pequeño (últimas 3 operaciones)
        self.historial_var = tk.StringVar()
        self.historial_label = tk.Label(
            frame_pantalla, 
            textvariable=self.historial_var,
            font=("Arial", 10),
            bg=self.color_pantalla,
            fg="#a0a0a0",  # gris claro
            height=3,
            anchor="se",
            justify="right"
        )
        self.historial_label.pack(fill="both", padx=5, pady=(5, 0))
        
        # Pantalla principal
        self.pantalla = tk.Entry(
            frame_pantalla,
            font=("Arial", 24, "bold"),
            bg=self.color_pantalla,
            fg=self.color_texto,
            insertbackground=self.color_texto,
            justify="right",
            bd=0,
            relief=tk.FLAT
        )
        self.pantalla.pack(fill="both", padx=5, pady=5, ipady=10)
        self.pantalla.insert(0, "0")
        self.pantalla.config(state="readonly")
        
        # Pestañas para funciones adicionales
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10)
        
        # Estilos para las pestañas
        estilo = ttk.Style()
        estilo.configure("TNotebook", background="#1e1e2e", borderwidth=0)
        estilo.configure("TNotebook.Tab", background="#3b3b5b", foreground="white", padding=[10, 2])
        estilo.map("TNotebook.Tab", background=[("selected", "#f5924a")])
        
        # Pestaña calculadora estándar
        self.tab_estandar = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(self.tab_estandar, text="Estándar")
        
        # Pestaña calculadora científica
        self.tab_cientifica = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(self.tab_cientifica, text="Científica")
        
        # Pestaña historial
        self.tab_historial = tk.Frame(self.notebook, bg="#1e1e2e")
        self.notebook.add(self.tab_historial, text="Historial")
        
        # Configurar botones estándar
        self.configurar_botones_estandar()
        
        # Configurar botones científicos
        self.configurar_botones_cientificos()
        
        # Configurar historial
        self.configurar_historial()
    
    def configurar_botones_estandar(self):
        # Frame para botones
        frame_botones = tk.Frame(self.tab_estandar, bg="#1e1e2e")
        frame_botones.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Configuración de botones
        botones = [
            ("MC", 0, 0, self.color_boton_func, lambda: self.memoria_clear()),
            ("MR", 0, 1, self.color_boton_func, lambda: self.memoria_recall()),
            ("M+", 0, 2, self.color_boton_func, lambda: self.memoria_add()),
            ("M-", 0, 3, self.color_boton_func, lambda: self.memoria_subtract()),
            
            ("C", 1, 0, self.color_boton_func, lambda: self.limpiar()),
            ("⌫", 1, 1, self.color_boton_func, lambda: self.borrar()),
            ("%", 1, 2, self.color_boton_op, lambda: self.agregar_a_expresion("%")),
            ("÷", 1, 3, self.color_boton_op, lambda: self.agregar_a_expresion("/")),
            
            ("7", 2, 0, self.color_boton_num, lambda: self.agregar_a_expresion("7")),
            ("8", 2, 1, self.color_boton_num, lambda: self.agregar_a_expresion("8")),
            ("9", 2, 2, self.color_boton_num, lambda: self.agregar_a_expresion("9")),
            ("×", 2, 3, self.color_boton_op, lambda: self.agregar_a_expresion("*")),
            
            ("4", 3, 0, self.color_boton_num, lambda: self.agregar_a_expresion("4")),
            ("5", 3, 1, self.color_boton_num, lambda: self.agregar_a_expresion("5")),
            ("6", 3, 2, self.color_boton_num, lambda: self.agregar_a_expresion("6")),
            ("-", 3, 3, self.color_boton_op, lambda: self.agregar_a_expresion("-")),
            
            ("1", 4, 0, self.color_boton_num, lambda: self.agregar_a_expresion("1")),
            ("2", 4, 1, self.color_boton_num, lambda: self.agregar_a_expresion("2")),
            ("3", 4, 2, self.color_boton_num, lambda: self.agregar_a_expresion("3")),
            ("+", 4, 3, self.color_boton_op, lambda: self.agregar_a_expresion("+")),
            
            ("±", 5, 0, self.color_boton_num, lambda: self.cambiar_signo()),
            ("0", 5, 1, self.color_boton_num, lambda: self.agregar_a_expresion("0")),
            (".", 5, 2, self.color_boton_num, lambda: self.agregar_a_expresion(".")),
            ("=", 5, 3, self.color_boton_op, lambda: self.calcular()),
        ]
        
        # Crear grid
        frame_botones.columnconfigure(0, weight=1)
        frame_botones.columnconfigure(1, weight=1)
        frame_botones.columnconfigure(2, weight=1)
        frame_botones.columnconfigure(3, weight=1)
        
        for i in range(6):
            frame_botones.rowconfigure(i, weight=1)
        
        # Crear botones
        for (texto, fila, columna, color, comando) in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                font=("Arial", 16, "bold"),
                bg=color,
                fg=self.color_texto,
                activebackground=self.ajustar_color(color, 20),
                activeforeground=self.color_texto,
                relief=tk.FLAT,
                borderwidth=0,
                command=comando
            )
            boton.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
    
    def configurar_botones_cientificos(self):
        # Frame para botones científicos
        frame_botones = tk.Frame(self.tab_cientifica, bg="#1e1e2e")
        frame_botones.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Configuración de botones científicos
        botones = [
            ("sin", 0, 0, self.color_boton_func, lambda: self.funcion_cientifica("sin(")),
            ("cos", 0, 1, self.color_boton_func, lambda: self.funcion_cientifica("cos(")),
            ("tan", 0, 2, self.color_boton_func, lambda: self.funcion_cientifica("tan(")),
            ("DEG", 0, 3, self.color_boton_func, lambda: self.cambiar_modo()),
            
            ("√", 1, 0, self.color_boton_func, lambda: self.funcion_cientifica("sqrt(")),
            ("x²", 1, 1, self.color_boton_func, lambda: self.funcion_cientifica("**2")),
            ("x^y", 1, 2, self.color_boton_func, lambda: self.agregar_a_expresion("**")),
            ("log", 1, 3, self.color_boton_func, lambda: self.funcion_cientifica("log10(")),
            
            ("(", 2, 0, self.color_boton_op, lambda: self.agregar_a_expresion("(")),
            (")", 2, 1, self.color_boton_op, lambda: self.agregar_a_expresion(")")),
            ("π", 2, 2, self.color_boton_num, lambda: self.agregar_a_expresion("π")),
            ("e", 2, 3, self.color_boton_num, lambda: self.agregar_a_expresion("e")),
            
            ("exp", 3, 0, self.color_boton_func, lambda: self.funcion_cientifica("exp(")),
            ("ln", 3, 1, self.color_boton_func, lambda: self.funcion_cientifica("log(")),
            ("abs", 3, 2, self.color_boton_func, lambda: self.funcion_cientifica("abs(")),
            ("n!", 3, 3, self.color_boton_func, lambda: self.funcion_cientifica("factorial(")),
            
            ("mod", 4, 0, self.color_boton_op, lambda: self.agregar_a_expresion("%")),
            ("1/x", 4, 1, self.color_boton_func, lambda: self.funcion_cientifica("1/")),
            ("C", 4, 2, self.color_boton_func, lambda: self.limpiar()),
            ("=", 4, 3, self.color_boton_op, lambda: self.calcular()),
        ]
        
        # Crear grid
        frame_botones.columnconfigure(0, weight=1)
        frame_botones.columnconfigure(1, weight=1)
        frame_botones.columnconfigure(2, weight=1)
        frame_botones.columnconfigure(3, weight=1)
        
        for i in range(5):
            frame_botones.rowconfigure(i, weight=1)
        
        # Crear botones
        for (texto, fila, columna, color, comando) in botones:
            boton = tk.Button(
                frame_botones,
                text=texto,
                font=("Arial", 14, "bold"),
                bg=color,
                fg=self.color_texto,
                activebackground=self.ajustar_color(color, 20),
                activeforeground=self.color_texto,
                relief=tk.FLAT,
                borderwidth=0,
                command=comando
            )
            boton.grid(row=fila, column=columna, padx=2, pady=2, sticky="nsew")
    
    def configurar_historial(self):
        frame_historial = tk.Frame(self.tab_historial, bg="#1e1e2e")
        frame_historial.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Lista para mostrar el historial
        self.lista_historial = tk.Listbox(
            frame_historial,
            bg=self.color_pantalla,
            fg=self.color_texto,
            font=("Arial", 12),
            selectbackground=self.color_boton_op,
            selectforeground=self.color_texto,
            relief=tk.FLAT,
            borderwidth=0
        )
        self.lista_historial.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Botones para el historial
        frame_botones_hist = tk.Frame(frame_historial, bg="#1e1e2e")
        frame_botones_hist.pack(fill="x", padx=5, pady=5)
        
        btn_borrar_hist = tk.Button(
            frame_botones_hist,
            text="Borrar Historial",
            font=("Arial", 12),
            bg=self.color_boton_func,
            fg=self.color_texto,
            command=self.borrar_historial
        )
        btn_borrar_hist.pack(side="left", padx=5)
        
        btn_usar_hist = tk.Button(
            frame_botones_hist,
            text="Usar Seleccionado",
            font=("Arial", 12),
            bg=self.color_boton_op,
            fg=self.color_texto,
            command=self.usar_historial
        )
        btn_usar_hist.pack(side="right", padx=5)
    
    def ajustar_color(self, color_hex, ajuste):
        """Ajusta el brillo de un color hexadecimal"""
        r = int(color_hex[1:3], 16)
        g = int(color_hex[3:5], 16)
        b = int(color_hex[5:7], 16)
        
        r = max(0, min(255, r + ajuste))
        g = max(0, min(255, g + ajuste))
        b = max(0, min(255, b + ajuste))
        
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def agregar_a_expresion(self, valor):
        if self.expresion == "0" or self.pantalla.get() == "0":
            self.expresion = ""
        
        # Reemplazar símbolos especiales
        if valor == "π":
            valor = "math.pi"
        elif valor == "e":
            valor = "math.e"
        
        self.expresion += valor
        self.actualizar_pantalla()
    
    def funcion_cientifica(self, funcion):
        if self.expresion == "0":
            self.expresion = ""
        
        # Añadir prefijo math. para funciones
        if funcion in ["sin(", "cos(", "tan(", "log(", "log10(", "sqrt(", "exp(", "factorial("]:
            funcion = "math." + funcion
        
        self.expresion += funcion
        self.actualizar_pantalla()
    
    def actualizar_pantalla(self):
        # Versión para mostrar (reemplazar multiplicación y división por símbolos)
        display_expr = self.expresion.replace("*", "×").replace("/", "÷")
        display_expr = display_expr.replace("math.pi", "π").replace("math.e", "e")
        display_expr = display_expr.replace("math.sin", "sin").replace("math.cos", "cos")
        display_expr = display_expr.replace("math.tan", "tan").replace("math.log", "ln")
        display_expr = display_expr.replace("math.log10", "log").replace("math.sqrt", "√")
        display_expr = display_expr.replace("math.exp", "exp").replace("math.factorial", "fact")
        
        # Actualizar pantalla
        self.pantalla.config(state="normal")
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, display_expr if display_expr else "0")
        self.pantalla.config(state="readonly")
    
    def calcular(self):
        if not self.expresion:
            return
        
        try:
            # Guardar la expresión original para el historial
            expresion_original = self.expresion
            display_expr = expresion_original.replace("*", "×").replace("/", "÷")
            display_expr = display_expr.replace("math.pi", "π").replace("math.e", "e")
            display_expr = display_expr.replace("math.sin", "sin").replace("math.cos", "cos")
            display_expr = display_expr.replace("math.tan", "tan").replace("math.log", "ln")
            display_expr = display_expr.replace("math.log10", "log").replace("math.sqrt", "√")
            display_expr = display_expr.replace("math.exp", "exp").replace("math.factorial", "fact")
            
            # Evaluar la expresión
            self.resultado = eval(self.expresion)
            
            # Agregar al historial
            entrada_historial = f"{display_expr} = {self.resultado}"
            self.historial.append(entrada_historial)
            self.lista_historial.insert(0, entrada_historial)
            
            # Actualizar historial pequeño
            self.actualizar_historial_pequeno()
            
            # Mostrar resultado
            self.expresion = str(self.resultado)
            self.actualizar_pantalla()
            
        except Exception as e:
            self.pantalla.config(state="normal")
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")
            self.pantalla.config(state="readonly")
            self.expresion = ""
    
    def limpiar(self):
        self.expresion = ""
        self.actualizar_pantalla()
    
    def borrar(self):
        self.expresion = self.expresion[:-1]
        self.actualizar_pantalla()
    
    def cambiar_signo(self):
        if not self.expresion:
            self.expresion = "0"
        
        # Verificar si es un número simple o una expresión
        try:
            valor = float(self.expresion)
            self.expresion = str(-valor)
        except:
            # Si no es un número simple, envolver en -1 *
            self.expresion = f"-1*({self.expresion})"
        
        self.actualizar_pantalla()
    
    def cambiar_modo(self):
        # Esta función cambiaría entre radianes y grados
        # Necesitaría una implementación más completa para ser funcional
        messagebox.showinfo("Información", "Cambio entre radianes y grados no implementado")
    
    def memoria_clear(self):
        self.memoria = 0
        messagebox.showinfo("Memoria", "Memoria borrada")
    
    def memoria_recall(self):
        self.expresion = str(self.memoria)
        self.actualizar_pantalla()
    
    def memoria_add(self):
        try:
            if self.expresion:
                valor = eval(self.expresion)
                self.memoria += valor
                messagebox.showinfo("Memoria", f"Valor {valor} añadido a la memoria")
        except:
            messagebox.showerror("Error", "No se pudo añadir a la memoria")
    
    def memoria_subtract(self):
        try:
            if self.expresion:
                valor = eval(self.expresion)
                self.memoria -= valor
                messagebox.showinfo("Memoria", f"Valor {valor} restado de la memoria")
        except:
            messagebox.showerror("Error", "No se pudo restar de la memoria")
    
    def borrar_historial(self):
        self.historial = []
        self.lista_historial.delete(0, tk.END)
        self.historial_var.set("")
    
    def usar_historial(self):
        seleccion = self.lista_historial.curselection()
        if seleccion:
            item = self.lista_historial.get(seleccion[0])
            expresion = item.split(" = ")[0]
            
            # Convertir símbolos de vuelta a formato de código
            expresion = expresion.replace("×", "*").replace("÷", "/")
            expresion = expresion.replace("π", "math.pi").replace("e", "math.e")
            expresion = expresion.replace("sin", "math.sin").replace("cos", "math.cos")
            expresion = expresion.replace("tan", "math.tan").replace("ln", "math.log")
            expresion = expresion.replace("log", "math.log10").replace("√", "math.sqrt")
            expresion = expresion.replace("exp", "math.exp").replace("fact", "math.factorial")
            
            self.expresion = expresion
            self.actualizar_pantalla()
            
            # Cambiar a la pestaña estándar
            self.notebook.select(0)
    
    def actualizar_historial_pequeno(self):
        # Mostrar las últimas 3 operaciones en el historial pequeño
        historial_texto = ""
        for i in range(min(3, len(self.historial))):
            historial_texto += self.historial[i] + "\n"
        self.historial_var.set(historial_texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraAvanzada(root)
    root.mainloop()