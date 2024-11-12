import numpy as np

# Parámetros
DATA_AMOUNT = 200
DATA_GROUPS = 8
data = []

# Colores base para cada grupo
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
        variation = np.clip(color + np.random.randint(-30, 30, 3), 0, 255)
        data.append(variation)

# Convertir a un arreglo de numpy
data = np.array(data)


"""""""""""""""""""""""""""""""""""
VISUALIZAR EL CONJUNTO DE DATOS
"""""""""""""""""""""""""""""""""""
import matplotlib.pyplot as plt

# Visualizar los colores
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xticks([])
ax.set_yticks([])

# Dibujar cada color como un cuadrado en la cuadrícula
for i, color in enumerate(data):
    ax.add_patch(plt.Rectangle((i % 20, i // 20), 1, 1, color=color))

# Ajustar los límites de la gráfica
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)

plt.show()
