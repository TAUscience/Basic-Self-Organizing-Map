import numpy as np

def distancia_euclidiana(colores_entrada, color_neurona):
    # Calcular la distancia euclidiana
    distancia = np.sqrt(np.sum((colores_entrada - color_neurona) ** 2))
    return distancia

def neurona_ganadora(color_entrada, cuadrícula):
    filas, columnas, _ = cuadrícula.shape
    distancias = np.empty((filas, columnas))

    for i in range(filas):
        for j in range(columnas):
            distancias[i, j] = distancia_euclidiana(color_entrada, cuadrícula[i, j])

    # Encuentra las coordenadas de la neurona con la menor distancia
    ganador = np.unravel_index(np.argmin(distancias), distancias.shape)
    return ganador

def tasa_aprendizaje(iteracion, total_iteraciones, alpha_inicial=0.5):
  #Calculo de tasa de aprendizaje decreciente
    return alpha_inicial * (1 - iteracion / total_iteraciones)

def actualizar_pesos(cuadricula, color_entrada, ganador, alpha, radio_vecindad):

    return 
