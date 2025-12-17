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

# Definir un array de cuatro dimensiones y comprobarlo con NumPy
num_dimensiones = 4

# Definimos el tamaño de cada dimensión sin fijar constantes tipo 2*3*4*5
min_tamano = 2
max_tamano = 5
shape = tuple(np.random.randint(min_tamano, max_tamano + 1, size=num_dimensiones))

total_elementos = np.prod(shape)
matriz = np.arange(total_elementos).reshape(shape)

if matriz.ndim == num_dimensiones:
    print("La matriz tiene 4 dimensiones.")
else:
    print("La matriz NO tiene 4 dimensiones.")

# Mostrar por pantalla las dimensiones del array y su contenido
print("ndim:", matriz.ndim)
print("shape:", matriz.shape)
print("contenido:\n", matriz)

# Sumar los elementos en función de sus dos últimos ejes y mostrar resultado
ejes_ultimos_dos = tuple(range(matriz.ndim - 2, matriz.ndim))
suma = matriz.sum(axis=ejes_ultimos_dos)

print("\nSuma sobre los dos últimos ejes:", ejes_ultimos_dos)
print("shape suma:", suma.shape)
print("suma:\n", suma)
