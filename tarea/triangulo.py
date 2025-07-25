def calcular_area(b,h):
   area=(b*h)/2
   return area

def leer_datos():
    global base, altura
    base = int(input("ingrese los datos de la base del triangulo: "))
    altura = int(input("ingrese los datos de la alturadel triangulo: "))

def main():
    leer_datos()
    area_triangulo=calcular_area(base, altura)
    print(f"el area del triangulo es : {area_triangulo}")

if __name__=="__main__":
    main()