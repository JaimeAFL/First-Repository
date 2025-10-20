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

# Es posible generar nuevos arrays modificando o combinando arrays 
# existentes. Podemos crear un array multidimensional a partir de un vector 
# mediante la función reshape(), o podemos aplanar el array 
# multidimensional para obtener un vector usando la función flatten().

# Partimos de un vector (array 1d)
v = np.arange(15)
print(v) 

# Creamos una matriz (3x5) usando reshape()
m = v.reshape(3, 5)
print(m)

# Podemos obtener un nuevo vector "aplanando" todos elementos de la matriz,
# recorriendo fila tras fila.
v2 = m.flatten()
print(v2)

# También podemos "aplanar" la matriz recorriendo columna tras columna
# usando el modificador "F".
v2c = m.flatten("F")
print(v2c)

# Tanto reshape() como flatten() devuelven un array nuevo copiando los datos, 
# no modifican el array original. Y si te preguntas el porqué de usar "F" como 
# modificador de flatten(), viene del lenguaje de programación Fortran, que 
# almacena y opera las matrices columna a columna.
# Una operación típica con matrices es la trasposición, reflejando los elementos 
# a lo largo de su diagonal.

m = np.arange(15).reshape(3, 5)
print(m)

# Trasponemos la matriz usando el método T
# Fíjate que no necesita paréntesis.
m.T

# También podemos concatenar o apilar arrays en diferentes ejes.

m1 = np.arange(0,6).reshape(2, 3)
m2 = np.arange(10,16).reshape(2, 3)

 # Apilar verticalmente dos arrays
print(np.vstack((m1, m2)))

# Apilar horizontalmente dos arrays
print(np.hstack((m1, m2)))

# Podemos añadir una fila (array 1d) al final de un array 2d fila = np.array([30, 40, 60])
print(np.vstack((m1, m2)))

# Si queremos añadir una columna (array 1d) a un array 2d,
# usamos la funcion np.column_stack()
columna = np.array([100, 200])
print(np.column_stack((m1, columna)))

# A la hora de concatenar arrays asegúrate de que las dimensiones tienen tamaños compatibles. 
# Por ejemplo, con una matriz de F filas por C columnas, una nueva fila deberá tener C elementos, 
# y una nueva columna deberá tener F elementos.

# Igual que concatenamos arrays, podemos partir un array en trozos. Para ello tenemos las funciones np.vsplit() 
# y np.hsplit(). Ambas funciones devuelven una lista con los subarrays resultado de la división.

m_grande = np.arange(12).reshape(3, 4)
print(m_grande)

# Dividimos el array horizontalmente en 2 trozos
divh = np.hsplit(m_grande, 2)

# El resultado es una lista, veamos el primer trozo
print(divh[0])

# y el segundo
print(divh[1])

# Ahora dividimos verticalmente.
# No podemos dividir en 2 porque hay 3 filas.
# Pero podemos indicar los puntos de división con una tupla.
divv = np.vsplit(m_grande, (1,))
print(divv[0])

# Como ves, ambas funciones pueden usarse de dos formas. 
# En la primera, indicamos el número de particiones que queremos obtener. 
# Es este caso, es necesario que el número de filas (con np.vsplit()) o de columnas 
# (con np.hsplit()) sea divisible por el número de porciones que queremos. 
# Los trozos resultantes deben tener el mismo tamaño, o de lo contrario se producirá un error.

# En la segunda forma, pasamos como argumento una tupla con los puntos de corte por donde queremos dividir, 
# ya sea en filas o en columnas. En el ejemplo, queremos cortar por un único punto (fila en este caso), por lo 
# que usamos una tupla con un único elemento. Si recuerdas lo que aprendimos sobre las tuplas, para definir 
# una tupla de un solo elemento debemos añadir una coma justo detrás del valor (así Python lo puede distinguir 
# de otras expresiones que también usan paréntesis).

## MANIPULANDO ARRAYS ##

# Es posible generar nuevos arrays modificando o combinando arrays existentes. Podemos crear un array multidimensional 
# a partir de un vector mediante la función reshape(), o podemos aplanar el array multidimensional para obtener 
# un vector usando la función flatten().

# Partimos de un vector (array 1d)
v = np.arange(15)
print(v)

# Creamos una matriz (3x5) usando reshape()
m = v.reshape(3, 5)
print(m)

# Podemos obtener un nuevo vector
# "aplanando" todos elementos de la matriz,
# recorriendo fila tras fila
v2 = m.flatten()
print(v2)

# También podemos "aplanar" la matriz
# recorriendo columna tras columna
# usando el modificador "F"
v2c = m.flatten("F")
print(v2c)

## ASIGNACIONES ##

m = np.arange(12).reshape(3, 4)
print(m)

# Cambiar un elemento particular
m[0, 0] = 100
print(m)

# Podemos cambiar una "rebanada" con una lista de valores
# Ej. de la fila 1, desde la columna 1 hasta el final
#     (3 elementos)
m[1, 1:] = [50, 60, 70]
print(m)

# O cambiar todos los elementos seleccionados
# con un único valor
# Ej. desde la fila 1 hasta el final 
#     y la columna 2 hasta el final
m[1:, 2:] = 0
print(m)

## OPERACIONES MATEMÁTICAS ##

# Como te hemos adelantado en el ejemplo inicial, una de las caracterísiticas claves que hace tan útil y potente 
# a la librería NumPy es su habilidad para realizar operaciones directamente sobre arrays de datos de forma sencilla 
# y eficiente. Los operadores matemáticos habituales pueden utilizarse con arrays directamente. Podemos operar 
# con dos arrays, o bien con un array y un escalar. En ambos casos, las operaciones se realizan elemento a elemento.

v1 = np.array([2,5])
v2 = np.array([3,3])
m1 = np.array([1,2,3,4]).reshape(2,2)
m2 = np.array([3,5,7,11]).reshape(2,2)

# Podemos sumar un escalar a todos los elementos de un array
print( v1 + 3 )
print( m1 + 5 )

# O sumar dos arrays elemento a elemento
print( m1 + m2 )

# Resta de arrays
print( m2 - m1 )

# Multiplicación con escalar (no confundir con producto escalar de vectores/matrices)
m10 = 10 * m1
print(m10)

# Multiplicación de arrays
print(v1 * v2)  
print(m1 * m2)

# División
print( m10 / m1 )

# al aplicar estas operaciones elemento a elemento con dos arrays, 
# ambos deben tener dimensiones de tamaño compatible. Es decir, vectores o matrices que tengan el mismo 
# número de elementos en cada eje o dimensión. No obstante, es posible combinar en estas operaciones 
# dos arrays que tengan distinto número de dimensiones (por ejemplo, una matriz y un vector), siempre 
# que la dimensión del menor tenga un tamaño compatible con el array de más dimensiones. 
# Con un ejemplo seguro que queda más claro.

# array 1d: vector de dos elementos
v1 = np.array([2,5])
# array 1d: vector de tres elementos
v3 = np.array([3,3,3])
m1 = np.array([1,2,3,4]).reshape(2,2)     # array 2d: matriz 2x2
print(m1)

# Multiplicar matriz (2d) por vector (1d)  elemento a elemento
# Los tamaños de las dimensiones (matriz 2x2 y vector de tamaño 2) son compatibles
print( m1 * v1 )

# Es como si tuviéramos el vector v1 "apilado" dos veces...
mv1 = np.vstack((v1, v1))
print(mv1)

# ... y multiplicásemos las dos matrices
print( m1 * mv1 )

# Sin embargo, si mezclamos arrays con distinto número de dimensiones
# pero con tamaños no compatibles, se producirá un error
# P r i n t( m1 * v3 )

#Traceback (most recent call last):
  # File "/workspaces/First-Repository/Carpeta_Numpy.py", line 361, in <module>
    # print( m1 * v3 )
           # ~~~^~~~
# ValueError: operands could not be broadcast together with shapes (2,2) (3,) 


# Cuando mezclamos dos arrays con diferente número de dimensiones en operaciones elemento 
# a elemento, NumPy automáticamente toma el array de dimensión menor y replica la operación 
# con cada dimensión del array mayor, como si fuera un bucle.

# Es equivalente a tomar el array menor y extrusionar o apilar sus valores a lo largo del eje 
# que falte, hasta obtener un array compatible con el de dimensión mayor. Este mecanismo es conocido 
# como propagación o broadcasting.

# Para que funcione, el tamaño del array de dimensión menor sigue teniendo que ser compatible 
# con el mayor. En el último caso del ejemplo anterior, el vector v3 tiene tamaño 3. Al aplicar 
# el broadcasting, el último elemento de v3 no tiene un par correspondiente en la matriz m1, 
# así que no es posible aplicar la operación elemento a elemento.

# Además de todos los operadores que has visto, con NumPy también tenemos disponibles múltiples 
# funciones matemáticas universales para aplicarlas sobre arrays.

# Raíz cuadrada
print( np.sqrt(m1) )

# Funciones trigonométricas: Seno, coseno, tangente...
print( np.sin(m1) )
print( np.cos(m1) )
print( np.tan(m1) )

# Logaritmo
print( np.log(m1) )

# Exponencial (e^x)
print( np.exp(m1) )

# Lista completa de operaciones matemáticas
# https://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs 

## OPERACIONES ESTADÍSTICAS ##

# NumPy nos permite calcular valores agregados o estadísticos sobre un array, 
# como la suma de sus elementos o la media. Podemos realizar estas operaciones 
# tomando todos los elementos del array, o agregar en un determinado eje o dimensión 
# (por ejemplo, por filas o columnas en una matriz).

# Creamos una matriz
m3 = np.arange(1,10).reshape(3,3)
print(m3)

# Suma de los elementos de cada columna
print(np.sum(m3, axis = 0))

# Suma de los elementos de cada fila
print(np.sum(m3, axis = 1))

# Media
print(np.mean(m3))

# Desviación estándar
print(np.std(m3))

# Máximos y mínimos
print (np.min(m3, axis = 0))
print (np.max(m3, axis = 1))

## ÁLGEBRA DE VECTORES Y MATRICES ##

# Naturalmente, la librería NumPy incorpora las principales operaciones de transformación 
# y álgebra lineal con vectores y matrices. Alguna de ellas ya la hemos visto, como el cálculo 
# de la matriz traspuesta.

m1 = np.array([1, 3, 4, 7, 5, 8, 2, 9, 6]).reshape(3,3)
print(m1)

# Trasponer la matriz
print(m1.transpose())

# ... o más breve
print (m1.T)

# También disponemos del producto interno de vectores y matrices. Cuando tengas que realizar 
# estas operaciones, recuerda no confundirte con la multiplicación elemento a elemento de arrays 
# (operador '*').

# Para dos vectores...
v1 = np.array([1, 4, 6])
v2 = np.array([3, 5, 2])

# El producto interior de dos vectores
# genera un escalar
print(v1.dot(v2))

# Para dos matrices...
m1 = np.array([4, 1, 1, 2]).reshape(2,2)
m2 = np.array([1, 3, 5, 1]).reshape(2,2)

# El producto interior de dos matrices
# genera una matriz
mp1 = m1.dot(m2)
print(mp1)

# El producto interior de una matriz y un vector
# es un vector
v3 = np.array([3, 5])
mv = m1.dot(v3)
print(mv)
