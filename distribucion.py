import numpy as np
import matplotlib.pyplot as plt
lambda_val = 1  # Valor de lambda
x_start = 0     # Valor inicial de x
x_end = 10      # Valor final de x
x_step = 0.5    # Paso entre valores de x

x = np.arange(x_start, x_end + x_step, x_step)

y_density = lambda_val * np.exp(-lambda_val * x)     
#------------------------ 
y_cumulative = 1 - np.exp(-lambda_val * x)  

plt.figure(figsize=(10, 6))
plt.plot(x, y_density, label='Densidad f(x)', color='blue', marker='o')
plt.plot(x, y_cumulative, label='Acumulada F(x)', color='green', linestyle='--', marker='x')
plt.title('Distribución Exponencial: Densidad y Función Acumulativa')
plt.xlabel('x')
plt.ylabel('Valor')
plt.grid(True)
plt.legend()
plt.show()