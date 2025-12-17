"""
===============================================================================
PROGRAMA: OPERACIONES CON SERIES Y DATAFRAMES ALEATORIOS (PANDAS Y NUMPY)
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa genera datos aleatorios y realiza varias operaciones básicas
con estructuras de datos de Python, NumPy y Pandas.

Trabaja con:
- Una lista de Python convertida a Serie (serieA)
- Un array de NumPy convertido a Serie (serieB)
- Funciones para:
  * Encontrar posiciones de múltiplos de 3 en una serie
  * Encontrar elementos comunes entre dos series
  * Encontrar elementos únicos de la primera serie respecto a la segunda
- Un DataFrame que combina serieA y serieB con nombre de índice
- Una tercera serie (serieC) de 35 valores que se transforma en un DataFrame
  de 7 filas y 5 columnas

OBJETIVOS QUE CUBRE:
--------------------
1) Generar una lista de 10 enteros aleatorios entre 0 y 20 y crear serieA.
2) Generar un array de 10 enteros aleatorios entre 0 y 20 y crear serieB.
3) Detectar las posiciones en serieA cuyos valores sean múltiplos de 3.
4) Identificar valores comunes entre serieA y serieB.
5) Identificar valores de serieA que no estén en serieB.
6) Combinar serieA y serieB en un DataFrame y nombrar el índice.
7) Generar serieC de 35 valores y convertirla en un DataFrame 7x5.

NOTAS IMPORTANTES:
------------------
- random.randint(0, 20) puede generar valores repetidos.
- numpy.random.randint(0, 21, size=10) también puede generar repetidos.
- Las funciones de "comunes" y "únicos" que se implementan aquí devuelven
  valores sin duplicados en el resultado mostrado, aunque las series originales
  sí puedan tener repetidos.
- El patrón "for-else" se usa en encontrar_unicos para detectar si un elemento
  no aparece en la segunda serie.

===============================================================================
"""

import random
import numpy
import pandas

# Generación de una LISTA de Python de 10 enteros aleatorios entre 0 y 20
def generar_numeros():
    # Devuelve una lista de 10 números aleatorios (pueden repetirse)
    return [random.randint(0, 20) for i in range(10)]

# Generación de un ARRAY de NumPy de 10 enteros aleatorios entre 0 y 20
def generar_array():
    # numpy.randint usa límite superior exclusivo,
    # por eso se pone 21 para incluir el 20
    return numpy.random.randint(0, 21, size=10)

# Función: encontrar_posicion
#    - Recibe una serie
#    - Guarda y muestra las POSICIONES de los múltiplos de 3
def encontrar_posicion(serie):
    posiciones = []

    # enumerate nos da (indice, valor) en cada iteración
    for i, numeros in enumerate(serie):
        # Si el valor es múltiplo de 3, guardamos su índice
        if numeros % 3 == 0:
            posiciones += [i]

    print("Posiciones con valores que son múltiplos de 3: ", posiciones)

# Función: encontrar_comunes
#    - Recibe dos series
#    - Busca valores que aparecen en ambas (sin repetirlos en el resultado)
def encontrar_comunes(serie1, serie2):
    comunes = []

    # Doble bucle para comparar cada elemento de serie1 con cada elemento de serie2
    for a in serie1:
        for b in serie2:
            if a == b:
                # Evitamos duplicados en la lista de salida
                if a not in comunes:
                    comunes += [a]

    print("Elementos comunes entre las series:", comunes)

# Función: encontrar_unicos
#    - Recibe dos series
#    - Muestra los elementos de la PRIMERA serie que NO están en la SEGUNDA
#    - Usa el patrón for-else:
#        * Si se encuentra igualdad, break
#        * Si no se rompe el bucle interno, entra en el else
def encontrar_unicos(serie_1, serie_2):
    unicos = []

    for a in serie_1:
        for b in serie_2:
            if a == b:
                # Si existe en la segunda serie, dejamos de buscar
                break
        else:
            # Solo entra aquí si NO se encontró ningún b igual a a
            if a not in unicos:
                unicos += [a]

    print("Elementos unicos entre las series:", unicos)

# Serie A a partir de una lista de Python
serieA = pandas.Series(generar_numeros(), name="serieA")
print(serieA)

# Serie B a partir de un array de NumPy
array = generar_array()
serieB = pandas.Series(array, name="serieB")
print(serieB)

# Invocacion de funciones sobre las series
encontrar_posicion(serieA)
encontrar_comunes(serieA, serieB)
encontrar_unicos(serieA, serieB)

# DataFrame combinando serieA y serieB + nombre del índice
dataframe = pandas.DataFrame({"serieA": serieA, "serieB": serieB})
dataframe.index.name = "indice"
print(dataframe)

# Creamos una serie de 35 números aleatorios entre 1 y 9
serieC = pandas.Series(numpy.random.randint(1, 10, 35))

# Convertimos a array y le damos forma de matriz 7x5
matriz = serieC.to_numpy().reshape(7, 5)

# Creamos el DataFrame final con nombres de columnas
df = pandas.DataFrame(matriz, columns=[f"columna_{i+1}" for i in range(5)])
print(df)