# Función principal de la calculadora
def calculadora():
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Elige una opción (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

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
            print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida.")

calculadora()

    


