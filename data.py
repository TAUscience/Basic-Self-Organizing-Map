import numpy as np

# Parámetros
DATA_AMOUNT = 200
DATA_GROUPS = 8
variation_factor = 1  # Valor de variación del 0 (sin variación) al 1 (máxima variación)
data = []

# Colores base para cada grupo (puedes ajustar estos valores)
base_colors = [
    [255, 0, 0],    # Rojo
    [0, 255, 0],    # Verde
    [0, 0, 255],    # Azul
    [255, 255, 0],  # Amarillo
    [255, 0, 255],  # Magenta
    [0, 255, 255],  # Cyan
    [128, 128, 128],# Gris
    [255, 165, 0]   # Naranja
]

# Cantidad de colores por grupo
colors_per_group = DATA_AMOUNT // DATA_GROUPS

# Generar los colores
for color in base_colors[:DATA_GROUPS]:
    for _ in range(colors_per_group):
        # Crear una pequeña variación aleatoria en torno al color base
        max_variation = int(75 * variation_factor)  # Ajusta la variación máxima
        variation = np.clip(color + np.random.randint(-max_variation, max_variation, 3), 0, 255)
        data.append(variation)

# Convertir a un arreglo de numpy
data = np.array(data)


"""""""""""""""""""""""""""""""""""
VISUALIZAR EL CONJUNTO DE DATOS
"""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt

# Convertir a un arreglo de numpy y escalar a rango [0, 1] para matplotlib
data_plot = np.array(data) / 255.0

# Visualizar los colores
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xticks([])
ax.set_yticks([])

# Dibujar cada color como un cuadrado en la cuadrícula
for i, color in enumerate(data_plot):
    ax.add_patch(plt.Rectangle((i % 20, i // 20), 1, 1, color=color))

# Ajustar los límites de la gráfica
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)

plt.show()