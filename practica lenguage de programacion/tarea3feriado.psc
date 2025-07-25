//los valores xyz fallavan , por eso los cambie por (abc)
Algoritmo valores_a_b_c
    Definir  a,  b,  c, limite Como Entero
    Definir resultado Como Real
    Escribir "Ingrese el límite superior para X, Y y Z: "
    Leer limite
    Para a = 1 Hasta limite Con Paso 1
        Para b= 1 Hasta limite Con Paso 1
            Para c = 1 Hasta limite Con Paso 1
				
                resultado = 18 * (a^3) + 11 * (b^5) + 8 * (c^6)
                Si resultado < 6300 Entonces
                    Escribir "(", a, ", ", b, ", ", c, ")"
                FinSi
                
            FinPara
        FinPara
    FinPara
FinAlgoritmo
