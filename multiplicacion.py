def multiplicacion(a,b):
    if a==0 or b==0:
        return 0
    else:
        return multiplicacion(a,b-1)+a 

numeroa=int(input("valor de a=" ))
numerob=int(input("valor de b=" ))
print(f"la multiplicacion es:", multiplicacion(numeroa,numerob))