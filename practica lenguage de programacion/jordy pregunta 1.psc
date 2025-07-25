Algoritmo  signozodiacal
    Definir dia Como Entero
    Definir mes Como Entero
	
    Escribir "tu dia de nacimiento es:)"
    Leer dia
    Escribir "tu fecha de nacimiento es: (EJEMPLO donde enero = 1 y diciembre = 12):"
    Leer mes
	
    Si (mes = 3 Y dia >= 21) O (mes = 4 Y dia <= 19) Entonces
        Escribir "Tu signo es Aries"
		
    Sino
        Si (mes = 4 Y dia >= 20) O (mes = 5 Y dia <= 20) Entonces
            Escribir "Tu signo es Tauro"
			
        Sino
            Si (mes = 5 Y dia >= 21) O (mes = 6 Y dia <= 20) Entonces
                Escribir "Tu signo es Geminis"
				
            Sino
                Si (mes = 6 Y dia >= 21) O (mes = 7 Y dia <= 22) Entonces
                    Escribir "Tu signo es Cáncer"
					
                Sino
                    Si (mes = 7 Y dia >= 23) O (mes = 8 Y dia <= 22) Entonces
                        Escribir "Tu signo es Leo"
						
                    Sino
                        Si (mes = 8 Y dia >= 23) O (mes = 9 Y dia <= 22) Entonces
                            Escribir "Tu signo es Virgo"
							
                        Sino
                            Si (mes = 9 Y dia >= 23) O (mes = 10 Y dia <= 22) Entonces
                                Escribir "Tu signo es Libra"
								
                            Sino
                                Si (mes = 10 Y dia >= 23) O (mes = 11 Y dia <= 21) Entonces
                                    Escribir "Tu signo es Escorpio"
									
                                Sino
                                    Si (mes = 11 Y dia >= 22) O (mes = 12 Y dia <= 21) Entonces
                                        Escribir "Tu signo es Sagitario"
										
                                    Sino
                                        Si (mes = 12 Y dia >= 22) O (mes = 1 Y dia <= 19) Entonces
                                            Escribir "Tu signo es Capricornio"
											
                                        Sino
                                            Si (mes = 1 Y dia >= 20) O (mes = 2 Y dia <= 18) Entonces
                                                Escribir "Tu signo es Acuario"
												
                                            Sino
                                                Si (mes = 2 Y dia >= 19) O (mes = 3 Y dia <= 20) Entonces
                                                    Escribir "Tu signo es Piscis"
                                                FinSi
                                            FinSi
                                        FinSi
                                    FinSi
                                FinSi
                            FinSi
                        FinSi
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo


