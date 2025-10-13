### PANDAS ###

## ESTRUCTURAS DE DATOS BÁSICAS ##

# Series #

# La primera estructura de datos básica en Pandas son los objetos Series. 
# Puedes ver las series como una especie de array unidimensional. 
# los objetos Series utilizan internamente un array de NumPy para 
# almacenar los valores.

# Cargamos las librería Pandas y NumPy (también la usaremos en ejemplos)
import numpy as np
import pandas as pd

# Como Series y DataFrame se utilizan a menudo,
# podemos importarlos en el espacio de nombres directamente
from pandas import Series, DataFrame

# Creamos una serie a partir de una lista de valores
s1 = Series([3,5,7,9])
print(s1)

# para construir una serie es suficiente con proporcionar la lista de 
# datos que la componen, todos del mismo tipo. Al imprimir la serie aparecen dos columnas.
# en la primera columna aparecen los índices de posición de cada elemento en la serie.
# Los objetos Series almacenan tanto la secuencia de valores como una secuencia de etiquetas 
# asociadas a cada elemento, a la que nos referimos como el índice de la serie. Por defecto, 
# si no lo definimos de otra forma, el índice tomará la secuencia de valores indicando la posición 
# de cada elemento en la serie, empezando en cero. Como ya sabes, esto es equivalente a cómo 
# funcionan los índices de posición en las listas o en los arrays de NumPy. Pero podemos decidir 
# etiquetar de otras maneras a los elementos de la serie.

# Podemos utilizar valores que representen otra cosa para los índices
# P.ej. en una serie de temperaturas medias anuales
# usamos Años como índices 
temp_anual = Series([16.6, 16.2, 15.5, 17.0, 16.6, 16.5], 
	index = [2011, 2012, 2013, 2014, 2015, 2016])
print(temp_anual)

# Los índices son etiquetas, también pueden ser texto
# # P.ej. en una serie de temperaturas medias mensuales
# usamos los meses como índices.
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
	            index = ["Ene","Feb","Mar","Abr","May","Jun",
	                    "Jul","Ago","Sep","Oct","Nov","Dic"])
print(temp_mensual)

# Que demos etiquetas distintas para los índices al crear la serie no significa que los elementos cambien 
# su posición. Como puedes comprobar, los valores quedan en el mismo orden en el que los hayas especificado.
# A diferencia de las listas o de los arrays de NumPy, podemos utilizar las etiquetas como índices para 
# seleccionar elementos de las series.

# Seleccionar usando una lista de etiquetas o índices
temp_mensual[["Mar","Abr","May"]]

# Siguiendo con la herencia de funcionalidades de los arrays de NumPy, también podemos realizar 
# las mismas operaciones matemáticas con una serie y un valor escalar o bien elemento a elemento 
# entre dos series, o aplicar las operaciones de agregación.

# Podemos realizar las operaciones comunes con escalares...
s1 = Series([3,5,7,9])
print(s1 * 2)

# ... operaciones elemento a elemento entre series
s2 = Series([2,3,4,5])
print(s1 - s2)

# DATAFRAMES #

# Un DataFrame de la librería Pandas representa un conjunto de datos en forma tabular, 
# muy similar a una tabla en base de datos o también a una hoja de cálculo. Puedes verlo 
# como una colección de columnas o series alineadas, cada columna con su propio nombre o 
# etiqueta, y además pudiendo ser cada una de un tipo de dato distinto.

# Creamos un `DataFrame` utilizando un diccionario
df1 = DataFrame({'mes' : ["Ene","Feb","Mar","Abr","May","Jun",
	                          "Jul","Ago","Sep","Oct","Nov","Dic"],
	            'temp_c' : [7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 
	                             28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
	            'lluvia_mm' : [21, 22, 19, 39, 44, 26, 
	                                17, 17, 30, 36, 30, 21],
	            'humedad' : [75, 67, 59, 57, 54, 49, 
	                              47, 51, 57, 67, 73, 76]
                    })
print(df1)

# También podemos utilizar un array de Numpy o una serie para definir los valores de una columna.
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 
	                       28.2, 25.6, 20.8, 16.8, 12.3, 7.8])
df2 = DataFrame({'mes' : ["Ene","Feb","Mar","Abr","May","Jun",
	                          "Jul","Ago","Sep","Oct","Nov","Dic"],
	                 'imes' : np.arange(1, 13),
	                 'temp_c' : temp_mensual,
	                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 
	                                17, 17, 30, 36, 30, 21],
	                 'humedad' : [75, 67, 59, 57, 54, 49, 
	                              47, 51, 57, 67, 73, 76]
	       }, columns = ['mes','imes','temp_c','lluvia_mm','humedad'])
print(df2)

# De forma similar a las Series, los DataFrames también incorporan un índice que permite acceder a las filas. 
# Por defecto se asigna la secuencia de índices posicionales habitual, comenzando en cero. Pero también es 
# posible especificar cualquier otra secuencia de etiquetas para indexar el contenido del DataFrame.

# Vimos cómo crear una serie con etiquetas como índice
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 
	                       28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
	                     index = ["Ene","Feb","Mar","Abr","May","Jun",
	                              "Jul","Ago","Sep","Oct","Nov","Dic"])

# También podemos definir el índice en un DataFrame
df3 = DataFrame({'imes' : np.arange(1, 13),
	                 'temp_c' : temp_mensual,
	                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 
	                                17, 17, 30, 36, 30, 21],
	                 'humedad' : [75, 67, 59, 57, 54, 49, 
	                              47, 51, 57, 67, 73, 76]}, 
	                columns = ['imes','temp_c','lluvia_mm','humedad'],
	                index = ["Ene","Feb","Mar","Abr","May","Jun",
	                         "Jul","Ago","Sep","Oct","Nov","Dic"])
print(df3)

# Podemos listar la secuencia de etiquetas que forman el índice, o la secuencia de etiquetas 
# con los nombres de las columnas de un DataFrame. Como ves, la información de los nombres del índice 
# (filas) y de los nombres de las columnas se almacenan ambas en objetos de tipo Index.

# Índice asociado al DataFrame
df3.index

# Columnas del DataFrame
df3.columns

# Operaciones #

# Tamaño del DataFrame (num. filas, num. columnas)
df3.shape

# La forma más rápida de sacar el número de filas
df3.shape[0]

# Tamaño total (num. total de elementos)
df3.size

# Mostrar las N primeras filas (5 por defecto)
df3.head()

# o las N últimas
df3.tail(3)

# Conteo de elementos no nulos en cada columna
df3.count()

# Resumen con estadísticas básicas de cada columna
df3.describe()

# SELECCION Y FILTRADO #

# Con los DataFrames también podemos seleccionar por posición, o mediante las etiquetas, 
# o usando máscaras. La diferencia está en que un DataFrame tiene (al menos) dos ejes o dimensiones, 
# por lo que hay algún cambio en la forma de seleccionar y filtrar.

