from tkinter import Canvas, Tk, Frame, LAST, Label
from time import strftime
from math import cos, sin, radians, pi
import random
import locale

# Configurar el idioma en español
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

ventana = Tk()
ventana.title('Reloj Analógico')
ventana.geometry('420x540')  # Aumentar altura para incluir la fecha
ventana.config(bg='white')  # Fondo blanco
ventana.minsize(width=420, height=540)
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

frame = Frame(ventana, height=400, width=400, bg='white', relief='sunken')  # Fondo blanco
frame.grid(column=0, row=0)
canvas = Canvas(frame, bg='white', width=385, height=385, relief='raised', bd=10)  # Fondo blanco
canvas.grid(padx=5, pady=5)

# Etiqueta para el reloj digital
label_digital = Label(ventana, text='', font=('Arial', 18, 'bold'), bg='white', fg='black')
label_digital.grid(column=0, row=1, pady=5)

# Etiqueta para la fecha
label_fecha = Label(ventana, text='', font=('Arial', 16), bg='white', fg='dark green')
label_fecha.grid(column=0, row=2, pady=5)

# Etiqueta para la temperatura
label_temperatura = Label(ventana, text='', font=('Arial', 14, 'italic'), bg='white', fg='gray20')
label_temperatura.grid(column=0, row=3, pady=5)

hr = 0
mi = 0
se = 0
temperatura_actual = None  # Variable para guardar la temperatura actual
ultimo_cambio_temperatura = 0  # Hora en la que se cambió la temperatura

def reloj(h, m, s):
    canvas.delete('all')  # Limpiar el canvas antes de redibujar
    canvas.create_oval(50, 50, 350, 350, fill='yellow', outline='blue', width=6, activeoutline='dark violet', activefill='gray12')
    numeros = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]
    for i in range(0, len(numeros)):
        canvas.create_text(200 - 120 * sin(((i + 1) * 2 * pi) / 12), 200 - 120 * cos(((i + 1) * 2 * pi) / 12),
                           text=numeros[i], font=('Arial', 12, 'bold'), fill='black')  # Texto negro sobre blanco
    for y in range(60):
        canvas.create_text(200 - 140 * sin(((y + 1) * 2 * pi) / 60), 200 - 140 * cos(((y + 1) * 2 * pi) / 60),
                           text='•', font=('Arial', 12, 'bold'), fill='deep sky blue')
    for x in range(12):
        canvas.create_text(200 - 140 * sin(((x + 1) * 2 * pi) / 12), 200 - 140 * cos(((x + 1) * 2 * pi) / 12),
                           text='•', font=('Arial', 25, 'bold'), fill='red')
    # Agujas del reloj horas, minutos, segundos
    canvas.create_line(200, 200, 200 + 60 * sin(radians(hr)), 200 - 60 * cos(radians(hr)), fill='red', width=9, arrow=LAST)
    canvas.create_line(200, 200, 200 + 80 * sin(radians(mi)), 200 - 80 * cos(radians(mi)), fill='blue', width=6, arrow=LAST)
    canvas.create_line(200, 200, 200 + 120 * sin(radians(se)), 200 - 120 * cos(radians(se)), fill='magenta2', width=3, arrow=LAST)
    canvas.create_oval(190, 190, 210, 210, fill='gold', outline='black', width=2)

def generar_temperatura():
    # Generar una temperatura aleatoria entre -10 y 40 grados Celsius
    return f'{random.uniform(-10, 40):.1f}°C'

def tiempo():
    global hr, mi, se, temperatura_actual, ultimo_cambio_temperatura

    h = int(strftime('%H'))
    m = int(strftime('%M'))
    s = int(strftime('%S'))
    hr = (h / 12) * 360
    mi = (m / 60) * 360
    se = (s / 60) * 360

    reloj(hr, mi, se)

    # Actualizar el reloj digital
    label_digital.config(text=strftime('%H:%M:%S'))

    # Actualizar la fecha en español
    label_fecha.config(text=strftime('%A, %d de %B de %Y').capitalize())  # Ejemplo: "Lunes, 03 de diciembre de 2024"

    # Verificar si han pasado 5 horas desde el último cambio de temperatura
    tiempo_actual_en_horas = h + m / 60
    if tiempo_actual_en_horas - ultimo_cambio_temperatura >= 5 or temperatura_actual is None:
        temperatura_actual = generar_temperatura()
        ultimo_cambio_temperatura = tiempo_actual_en_horas

    # Actualizar la temperatura
    label_temperatura.config(text=f'Temperatura: {temperatura_actual}')

    canvas.after(1000, tiempo)

tiempo()
ventana.mainloop()
