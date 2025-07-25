import math

def calcular_area_circulo(radio):
  
  area = math.pi * radio**2
  return area

def leer_datos_circulo():
  
  global radio
  radio = float(input("Ingrese el radio del círculo: "))

def main():
  
  leer_datos_circulo()
  area_circulo = calcular_area_circulo(radio)
  print(f"El área del círculo es: {area_circulo:.2f}")  # Formateamos a dos decimales

if __name__ == "__main__":
  main()