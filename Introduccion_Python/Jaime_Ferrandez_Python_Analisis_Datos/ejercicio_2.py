"""
===============================================================================
PROGRAMA: ARRAY 4D Y SUMA POR LOS DOS ÚLTIMOS EJES (NumPy)
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa crea un array de 4 dimensiones (4D) con NumPy, comprueba que
realmente tiene 4 dimensiones, muestra sus dimensiones y contenido, y calcula
la suma de sus elementos respecto a sus dos últimos ejes.

FUNCIONAMIENTO:
---------------
1) CREACIÓN DEL ARRAY 4D:
   - Se define una forma (shape) con 4 tamaños (uno por dimensión).
   - Se construye el array con valores consecutivos usando np.arange() y reshape().

2) COMPROBACIÓN DE DIMENSIONES:
   - Se verifica con .ndim que el array tiene 4 dimensiones.

3) VISUALIZACIÓN:
   - Se imprime el número de dimensiones (ndim), la forma (shape) y el contenido.

4) SUMA EN LOS DOS ÚLTIMOS EJES:
   - Se suman los elementos sobre los dos últimos ejes de forma general
     (calculados a partir de ndim), y se muestra el resultado.

===============================================================================
"""

import numpy as np


# Número de dimensiones que queremos (en este caso, 4)
num_dimensiones = 4

# Rango del tamaño de cada dimensión (entre 2 y 5 elementos, ambos incluidos)
min_tamano = 2
max_tamano = 5

# Creamos una tupla "shape" con 4 números aleatorios entre 2 y 5.
# Por ejemplo, podría ser (3, 2, 5, 4).
shape = tuple(np.random.randint(min_tamano, max_tamano + 1, size=num_dimensiones))

# Número total de elementos = producto de las longitudes de cada dimensión
total_elementos = np.prod(shape)

# Creamos un array 1D con valores de 0 a total_elementos-1
# y luego lo reestructuramos (reshape) al "shape" calculado arriba.
matriz = np.arange(total_elementos).reshape(shape)

# Comprobamos que efectivamente la matriz tiene 4 dimensiones
if matriz.ndim == num_dimensiones:
    print("La matriz tiene 4 dimensiones.")
else:
    print("La matriz NO tiene 4 dimensiones.")

# Mostramos información básica de la matriz
print("ndim:", matriz.ndim)
print("shape:", matriz.shape)
print("contenido:\n", matriz)

# Creamos una tupla con los índices de los dos últimos ejes.
# Si la matriz es 4D, sus ejes son: 0, 1, 2, 3
# → los dos últimos son (2, 3).
ejes_ultimos_dos = tuple(range(matriz.ndim - 2, matriz.ndim))

# Hacemos la suma sobre esos dos ejes.
# Esto "colapsa" los dos últimos ejes y deja un array 2D
# con las dimensiones de los dos primeros ejes.
suma = matriz.sum(axis=ejes_ultimos_dos)

print("\nSuma sobre los dos últimos ejes:", ejes_ultimos_dos)
print("shape suma:", suma.shape)
print("suma:\n", suma)