def digitos(num):
    if num < 10:
        return 1
    else:
        return digitos(num // 10) + 1
    
num = int(input("Ingrese el valor : "))

print(f"La cantidad de digitos es: {digitos(num)}")