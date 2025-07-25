# calculadora:)
def calculadora():
    print("selecciona una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    
    opcion = input("elige una opcion:) (1/2/3/4): ")

    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))

    if opcion == '1':
        print(f"Resultado: {num1 + num2}")
    elif opcion == '2':
        print(f"Resultado: {num1 - num2}")
    elif opcion == '3':
        print(f"Resultado: {num1 * num2}")
    elif opcion == '4':
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("error: no se puede dividir entre cero.")
    else:
        print("no valido.")

calculadora()

    


