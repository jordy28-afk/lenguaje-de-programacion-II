def suma(n):
    if n==0:
        return 0
    else:
        return suma(n-1)+n

numero=int(input("valor de n" ))
print(f"la suma es :{suma(numero)}")