## CALCULO EN NUMPY ##

import numpy as np
altura = np.array([ 1.67, 1.73, 1.76, 1.85, 1.77, 1.73 ])
masa = np.array([ 65.0, 79.2, 76.7, 82.0, 72.5, 66.1 ])
print([masa / (altura ** 2)])

## ARRAYS ##

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

# Tipo de los elementos
print(m_2d.dtype)

# También podemos indicar el tipo de los elementos
# al crear el array, con el argumento 'dtype'
print(np.array([[1, 2, 3], [4, 5, 6]], dtype='float64'))

# La función np.arange() es similar al "range()" normal
	# pero crea arrays en lugar de listas
m1 = np.arange(15)
print(m1) 

# Al igual que range(), se puede indicar 
	# el limite inicial, final y el tamaño del paso
m2 = np.arange(1, 10, 2)
print(m2)

# Si queremos crear un array dividiendo un intervalo
	# en N elementos equiespaciados, podemos usar np.linspace()
m3 = np.linspace(0, 10, 5)  # Genera 5 núms entre 0 y 10 (ambos incluidos)
print(m3)

#Si recuerdas la función range() que hemos utilizado múltiples veces para generar secuencias, 
# notarás que la función np.arange() es prácticamente idéntica, solo que crea objetos de tipo 
# ndarray (que es el tipo de los arrays en NumPy).

# La función np.linspace() es un poco distinta, porque en lugar de darle el tamaño del paso, 
# lo que hace es generar un número dado de valores igualmente espaciados entre los dos límites 
# que le indicas (incluyendo ambos en el resultado).

# Al operar con vectores y matrices, será habitual que tengamos que utilizar construcciones especiales, 
# como matrices unidad, o arrays con todos los elementos cero o iguales... NumPy incluye varias funciones 
# muy prácticas para crear estos tipos de arrays más comunes.

# Crear un vector con 5 ceros
print(np.zeros(5))

# Crear una matriz 2x3 de ceros
print(np.zeros((2,3)))

# Crear una matrix 2x3 rellenada con el mismo valor (99) 
# para todos los elementos
print(np.full((2,3), 99))

# Fijamos la semilla aleatoria (por reproducibilidad)
np.random.seed(42)
# Crear una matrix 2x3
# rellenada con numeros aleatorios en [0, 1)
print(np.random.random((2,3)))

# Distribución uniforme en [a, b)
print(np.random.uniform(0, 10, size=(2,3)))


## INDEXADO E ITERACIÓN ##

# Podemos seleccionar elementos individuales o rebanadas de un array de forma similar a como lo hacemos con las 
# listas u otras secuencias en Python. La principal diferencia está en cómo seleccionar elementos en arrays 
# de 2 o más dimensiones.

# Para empezar, podemos seleccionar elementos indicando su posición en el array. Al igual que con las listas, 
# al primer elemento de cada dimensión se accede con el índice de posición cero. Si una dimensión tiene N elementos, 
# el último estará en la posición (N - 1).

# !!!! No confundas el número de dimensiones con el tamaño o número de elementos en cada dimensión del array !!!!

# Un array de dimensión 1 (vector)
v1 = np.arange(0, 50, 5)
print(v1)

# Podemos seleccionar un elemento individual
print(v1[2])

# Ahora con una matriz 3x4
# Fíjate que usamos la función range() normal
# para pasar las listas que necesitamos
# al inicializar el array
m2 = np.array([range(0,4), range(4,8), range(8,12)])
print(m2)

# # Seleccionamos un elemento
# indicando la fila (2) y la columna (3)
print(m2[2, 3])

# Seleccionamos los elementos
# de la fila 1 en las columnas 2 y 3
print(m2[1, [2,3]])

# Cuando tenemos un array de 2 o más dimensiones, debemos incluir entre los corchetes la selección de elementos 
# para cada dimensión, separándolas con comas (p.ej. m2[2, 3]). Si en una dimensión queremos seleccionar todos 
# los elementos, utilizamos los dos puntos (:).

# Seleccionamos la fila 0
print(m2[0, :])

# Seleccionamos la columna 1
print(m2[:, 1])

# Seleccionamos los elementos que están entre
# la fila 1 y la 3 (no incluida)
# y entre la columna 1 y la 3 (no incluida)
print(m2[1:3, 1:3])

# También podemos utilizar una máscara booleana para seleccionar elementos. Esto es útil para poder 
# filtrar aquellos valores que cumplen una determinada condición. Veamos cómo:

# Para cada elemento del array, comprobamos si es par o no
mascara_pares = (m2 % 2 == 0)
print(mascara_pares)

# Ahora usamos la mascara para seleccionar los elementos
print(m2[mascara_pares])
# Si te das cuenta, de toda la matriz, solo selecciona aquellos
# items que son pares, ya que como condición de selección hemos dicho
# que solo seleccione los que cumplen esta condición: % 2 == 0

# Si te fijas, Numpy siempre trabaja con arrays [condicion o indices]
# m2 → el array base sobre el que trabajas.
# m2 % 2 == 0 genera una máscara booleana del mismo tamaño que m2
# m2[m2 % 2 == 0] aplica esa máscara sobre m2 y devuelve solo los 
# elementos donde la condición es True (solo los pares).

## MANIPULANDO ARRAYS ##

