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

def vecindad(cuadricula, ganador, radio_vecindad):
    filas, columnas, _ = cuadricula.shape
    vecindad = np.zeros((filas, columnas))
    for i in range(filas):
        for j in range(columnas):
            distancia = np.sqrt((i - ganador[0])**2 + (j - ganador[1])**2)
        if distancia <= radio_vecindad:
            vecindad[i, j] = np.exp(-(distancia**2) / (2 * radio_vecindad**2))

    return vecindad

def actualizar_pesos(cuadricula, color_entrada, ganador, alpha, radio_vecindad):
    filas, columnas, _ = cuadricula.shape
    
    # Calculamos la vecindad de la neurona ganadora
    vecindad_actual = vecindad(cuadricula, ganador, radio_vecindad)
    
    # Actualizamos los pesos de todas las neuronas
    for i in range(filas):
        for j in range(columnas):
            # Si la neurona está dentro de la vecindad, actualizamos su peso
            if vecindad_actual[i, j] > 0:
                # Actualización de pesos usando la fórmula del SOM
                cuadricula[i, j] = cuadricula[i, j] + alpha * vecindad_actual[i, j] * (color_entrada - cuadricula[i, j])
    
    return cuadricula

    return 
