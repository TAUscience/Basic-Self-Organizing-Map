import numpy as np
import matplotlib.pyplot as plt
import funciones_aux as faux
from data import datos

tam = (10, 10)
cuadricula = np.random.randint(0, 256, (tam[0], tam[1], 3), dtype=int)

print("Cuadrícula SOM de 10x10 inicializada aleatoriamente (valores R, G, B):")
print(cuadricula)

total_iteraciones = 1000
alpha_inicial = 0.5
radio_inicial = max(cuadricula.shape) / 2 

for iteracion in range(total_iteraciones):
    color_entrada = datos[np.random.randint(len(datos))]
    ganador = faux.neurona_ganadora(color_entrada, cuadricula)
    alpha = faux.tasa_aprendizaje(iteracion, total_iteraciones, alpha_inicial)
    radio_vecindad = radio_inicial
    faux.actualizar_pesos(cuadricula, color_entrada, ganador, alpha, radio_vecindad)