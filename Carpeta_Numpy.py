import numpy as np
altura = np.array([ 1.67, 1.73, 1.76, 1.85, 1.77, 1.73 ])
masa = np.array([ 65.0, 79.2, 76.7, 82.0, 72.5, 66.1 ])
print([masa / (altura ** 2)])

# Un vector (dimensión 1) con tres elementos

v_1d = np.array([1, 2, 3])
# Número de dimensiones del array
print(v_1d.ndim)
# Número de elementos en cada dimensión del array
print(v_1d.shape)
# Número total de elementos del array
print(v_1d.size)
# Tipo de los elementos
print(v_1d.dtype)

# Ahora vamos a crear una matriz
# utilizando listas anidadas
m_2d = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(m_2d)
# Es un array de 2 dimensiones (una matriz)
print(m_2d.ndim) 

# El primer eje o dimensión tiene tamaño 2 (filas)
# El segundo eje o dimensión tiene tamaño 3 (columnas)
print(m_2d.shape)

# Número total de elementos del array
print(m_2d.size)