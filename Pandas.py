--------------
### PANDAS ###
--------------


## ESTRUCTURAS DE DATOS BÁSICAS: SERIES ##
------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------
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
----------------------------------------------------------------------------------------
# Con los DataFrames también podemos seleccionar por posición, o mediante las etiquetas, 
# o usando máscaras. La diferencia está en que un DataFrame tiene (al menos) dos ejes o dimensiones, 
# por lo que hay algún cambio en la forma de seleccionar y filtrar.
# Podemos seleccionar una columna por su nombre, utilizando los corchetes [] o la notación con punto 
# (como si accediéramos a un atributo del DataFrame).

df_meteo = DataFrame({
	                 'imes' : np.arange(1, 13),
	                 'temp_c' : [7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 
	                             28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
	                 'lluvia_mm' : [21, 22, 19, 39, 44, 26, 
	                                17, 17, 30, 36, 30, 21],
	                 'humedad' : [75, 67, 59, 57, 54, 49, 
	                              47, 51, 57, 67, 73, 76]}, 
					 
	                columns = ['imes','temp_c','lluvia_mm','humedad'],
	                index = ["Ene","Feb","Mar","Abr","May","Jun",
	                         "Jul","Ago","Sep","Oct","Nov","Dic"])

# Podemos acceder a una columna con su nombre entre corchetes
df_meteo["lluvia_mm"]

# También podemos acceder a una columna como si fuera un atributo, usando la notación con punto.
df_meteo.temp_c

# No obstante, aunque el acceso a una columna del DataFrame como si fuera un atributo puede resultar 
# un atajo muy cómodo, hay que tener cuidado. Si el nombre de una columna coincide con el nombre de alguno 
# de los atributos o métodos propios de la clase DataFrame, será esto a lo que estaremos accediendo, 
no a la columna.

# Un DataFrame de ejemplo con fórmulas para el área
# de distintas figuras geométricas
df_geom = DataFrame({
	        'shape' : ["triangle","square","circle"],
	        'area' : ["b*h/2", "a*a", "PI*r*r"]})

# Accedemos a la columna "shape" con corchetes
df_geom["shape"]

# Así accedemos a un atributo propio de la clase DataFrame
# que nos dice el número de filas y columnas que tiene (su "forma")
df_geom.shape

# Como ves, el atajo para acceder a una columna como un atributo no siempre va a funcionar. 
# Te recomendamos que utilices los corchetes como opción preferente. Y en especial, cuando tengas que asignar 
# valores a una columna, habrás de utilizar siempre la notación con corchetes.

# Además, utilizando los corchetes podemos dar una lista de nombres de columnas para elegir varias a la vez.
df_meteo[["imes","temp_c"]]

# Pero los corchetes también tienen otra funcionalidad. Si lo que indicamos entre corchetes es un rango o rebanada 
# utilizando el operador ':' (como hacemos con las listas normales), ¡entonces no seleccionamos columnas, sino filas!

# Indicamos un rango o "rebanada" de índices
df_meteo[0:4]

# También podemos usar "rebanadas" de etiquetas si el índice del DataFrame está etiquetado
df_meteo["Ene":"Mar"]       # Seleccionar filas de enero a marzo

# Lo mismo ocurre si entre corchetes escribimos una expresión o máscara booleana. 
# La máscara resultante se aplicará a las filas.

# Seleccionar las filas (meses) en las que la temperatura supere los 20ºC
df_meteo[df_meteo.temp_c > 20.0]

# -- IMPORTANTE --
# Si usas un nombre (o una lista de nombres) entre corchetes, seleccionas columnas. 
# Si indicas un rango o rebanada usando ':', o una máscara booleana, seleccionas filas.
# No obstante, para evitar ambigüedades, existen dos mecanismos adicionales para 
# seleccionar filas y columnas: df.loc y df.iloc.

# | Método de Acceso          | Descripción                               |
# |---------------------------|-------------------------------------------|
# | df.loc[filas, columnas]   | Selección por etiquetas                   |
# | df.iloc[filas, columnas]  | Selección por posición (índices enteros)  |

# Con df.loc podemos seleccionar filas y columnas indicando sus nombres o etiquetas.

# Acceso mediante etiquetas con df.loc .Podemos seleccionar un elemento concreto ([fila, columna])
df_meteo.loc["May", "lluvia_mm"]

# seleccionar una fila entera
df_meteo.loc["May", ]

# seleccionar una columna entera
df_meteo.loc[:, "humedad"]

# o un subconjunto de filas y columnas
df_meteo.loc["Feb":"Abr", ["lluvia_mm","humedad"]]

# Mientras que df.iloc está pensado para seleccionar indicando la posición (como en una lista o un array de NumPy).

# Acceso mediante índices de posición con df.iloc. Podemos seleccionar un elemento concreto ([fila, columna])
df_meteo.iloc[6, 2]

# seleccionar una fila entera
df_meteo.iloc[6, ]

# seleccionar una columna entera
df_meteo.iloc[:, 1]

# o un subconjunto de filas y columnas
df_meteo.iloc[0:3, 1:3]

# -- ATENCION --
# Fíjate en que, a diferencia de lo que ocurre con las rebanadas de índices numéricos, cuando seleccionamos 
# un rango o rebanada con etiquetas también se incluye el elemento del límite superior del rango.
# Tanto con df.loc como con df.iloc podemos utilizar también máscaras booleanas para seleccionar 
# tantas filas como columnas si queremos. Naturalmente, podemos utilizar estos selectores para asignar 
# valores a elementos del DataFrame.

# Aumentar en 1ºC la temperatura de los meses de Junio a Agosto
df_meteo.loc["Jun":"Ago","temp_c"] = df_meteo.loc["Jun":"Ago","temp_c"] + 1
print(df_meteo)

# También podemos añadir e inicializar una columna nueva de forma sencilla usando los corchetes.

# Añadir una columna, con un mismo valor para todas las filas
df_meteo["limite_temp_c"] = 50

# Añadir una columna, dando valores individuales a cada elemento mediante una lista o una expresión:
# Ej. pasar la temperatura a grados Fahrenheit
df_meteo["temp_F"] = 1.8 * df_meteo["temp_c"] + 32
print(df_meteo)


## LEYENDO DATOS DE FICHERO ##
-------------------------------------------------------------------------------
Pandas incluye varias funciones para leer datos tabulares de ficheros de texto:

# | Función         | Descripción                                                                              		|
# |-----------------|-----------------------------------------------------------------------------------------------|
# | pd.read_csv()   | Carga datos de un fichero de tipo CSV, con los campos separados por comas ';'            		|
# | pd.read_table() | Carga datos de un fichero de texto tabular, con los campos separados por tabuladores ('\t') 	|
# | pd.read_fwf()   | Carga datos de un fichero de texto con columnas de ancho fijo                             	|

# Para ver cómo funcionan, vamos a leer los datos de uno de los ficheros CSV que están incluidos en el material
# de la unidad. En este caso, vamos a cargar el fichero NYC_flights_2013_MINI.csv
# http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236 

# Ajusta la ruta de directorios para que apunte adonde hayas descargado los ficheros
df_flights = pd.read_csv("./U09_datasets/NYC_flights_2013_MINI.csv", sep = ";")

# Vemos qué tamaño tiene (filas, columnas)
df_flights.shape

# Mostramos las primeras filas y columnas del DataFrame
df_flights.iloc[0:5, 0:10]

# Las funciones read_csv y read_table permiten especificar un gran número de opciones mediante sus argumentos. 
# A continuación, te mostramos algunos de los principales. Para ver la lista completa, puedes consultar:
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html 
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_table.html

# | Argumentos de pd.read_csv() | Descripción                                                                           |
# |-----------------------------|---------------------------------------------------------------------------------------|
# | filepath                    | Fichero a cargar. Puede ser una ruta de fichero local o una URL                       |
# | sep                         | Carácter delimitador de campos. Por defecto ';' para read_csv y '\t' para read_table  |
# | header                      | Indica si el fichero contiene una fila con los nombres de las columnas y              |
# |								| puede indicar nº de fila (0) 															|
# | names                       | Lista opcional de nombres para las columnas                                           |
# | na_values                   | Lista de cadenas que representan valores ausentes (NAs) en el fichero                 |
# | quotechar                   | Carácter utilizado en el fichero para entrecomillar cadenas de texto                  |
# | encoding                    | Codificación o juego de caracteres utilizado (p.ej. ascii, latin1, utf8)              |


## ESCRIBIENDO DATOS A FICHERO ##
----------------------------------------------------------------------------------------------------------------
# También podemos salvar el contenido de nuestros DataFrames y Series a un fichero de texto tipo CSV o tabulado. 
# La forma más rápida y simple es utilizando el método to_csv.

# Seleccionamos las primeras filas para el ejemplo
df_mini = df_flights.head()

# Guardamos en fichero

df_mini.to_csv("./Prueba_export_pandas.csv", 
	               sep = ";", na_rep = "", header = True, 
	               index = False, index_label = False)

# Al igual que las funciones para leer, el método to_csv incluye múltiples opciones para controlar cómo se exporta 
# y salva la información. Las más importantes son las siguientes; la lista completa puedes consultarla en:
# http://pandas.pydata.org/pandas-docs/version/0.20.3/generated/pandas.DataFrame.to_csv.html 


## OPERACIONES BINARIAS. ALINEACION DE INDICES ##
--------------------------------------------------------------------
# Podemos aplicar los operadores aritméticos comunes a Series y DataFrames, como hacemos con los arrays en NumPy. 
# Solo que, en el caso de Pandas, antes de efectuar la operación se alinean los índices de las dos estruturas 
# de datos sobre las que se esté trabajando. ¿En qué consiste esa alineación? 
# Pueden ser los índices posicionales que se crean automáticamente por defecto 
# o bien etiquetas especificadas de forma explícita por nosotros.

# Cuando utilizamos dos variables (Series o DataFrames) en una de estas operaciones, lo primero que va a hacer la 
# librería Pandas de forma automática es alinear o emparejar los elementos de ambas variables que tengan el mismo índice:

# Definimos dos series
fruta_kg = Series({'peras': 2, 'manzanas': 1, 'naranjas': 3})
fruta_precio = Series({'manzanas': 1.95, 'naranjas': 1.90, 'peras': 1.50, 'uva': 2.60})
	
# Multiplicamos
fruta_kg * fruta_precio

# Antes de realizar la multiplicación, Pandas ha alineado los elementos de ambas Series utilizando sus índices, 
# de manera que la operación se aplique entre los pares de elementos correctos. El resultado incluye todos los índices 
# que aparecen en cualquiera de las dos Series. ¿Pero qué pasa con los elementos que están solo en una de las variables 
# (como la uva en el ejemplo)? En estos casos, Pandas da como resultado un valor especial: NaN.

# -- IMPORTANTE --
# El valor NaN (Not a Number) es la forma que tiene Pandas de indicar que faltan datos o que no se ha podido calcular 
# el valor. En general, es un valor intercambiable con None, y es similar al valor NA (not available) de R. Cualquier 
# operación con NaN devuelve otro NaN.

# Si operamos con DataFrames ocurre lo mismo, con la diferencia de que la alineación de índices 
# ocurre tanto para filas como para columnas.

# Preparamos un DataFrame con precios de dos tiendas
df_precio_fruta = DataFrame({
							'tienda_1' : [1.95, 1.90, 1.50, 2.60],
							'tienda_2' : [1.80, 1.95, 1.60, 2.40]},
							index = ["manzanas","naranjas","peras","uvas"])
	
# y otro DataFrame con la compra en cada una de las tiendas:
lista_compra_1 = Series({"peras" : 1.5, "naranjas" : 3})
lista_compra_2 = Series({"manzanas" : 1})
df_lista_compra = DataFrame({
	'tienda_1' : lista_compra_1,
	'tienda_2' : lista_compra_2})

# y operamos con ambos DataFrames
df_precio_fruta * df_lista_compra

# También podemos utilizar un objeto Series para operar sobre todas las filas o todas las columnas de un DataFrame.

lista_compra = Series({"peras" : 1.5, "naranjas" : 3, "manzanas" : 1})
	
# Multiplicamos la lista de la compra por los precios de cada tienda
df_precio_fruta.multiply(lista_compra, axis=0)

# Como ves, en este caso no hemos utilizado directamente el operador de multiplicación '*', sino el método 
# multiply(). El motivo es que el comportamiento por defecto es efectuar la operación por filas. En este caso, 
# nosotros queríamos multiplicar cada columna del DataFrame por el objeto Series. Para ello, los métodos equivalentes 
# a los operadores matemáticos incluyen un argumento axis que nos permite indicar si queremos propagar la operación por 
# filas (opción por defecto) o por columnas del DataFrame (indicando 'axis = 0').
# En la tabla siguiente tienes un resumen de los principales operadores y sus métodos equivalentes para Series y DataFrames.
#
# | Operador | Método Series/DataFrame        |
# |---------|---------------------------------|
# | +       | add()                           |
# | -       | sub(), subtract()               |
# | *       | mul(), multiply()               |
# | /       | div(), divide()                 |
# | //      | floordiv()                      |
# | %       | mod()                           |
# | **      | pow()                           |


## VALORES AUSENTES O NULOS ##
-----------------------------------------------------------------------------------------------------------------------
# Pandas utiliza el elemento especial NaN para indicar que cierto valor está ausente o bien que no ha podido realizarse 
# un cálculo. Al trabajar con datos en problemas reales, es normal (y casi inevitable) que aparezcan huecos en los datos, 
# valores no definidos o no válidos. Pandas incluye algunas funcionalidades muy útiles para lidiar con estos casos.
# Para empezar, podemos saber qué elementos son nulos utilizando isnull() (o su complementario, notnull()).

# Teníamos estas dos Series:
fruta_kg = Series({'peras': 2, 'manzanas': 1, 'naranjas': 3})
fruta_precio = Series({'manzanas': 1.95, 'naranjas': 1.90, 'peras': 1.50, 'uva': 2.60})
	
# Multiplicamos...
fruta_res = fruta_kg * fruta_precio
	
# y vemos qué elementos son nulos
fruta_res.isnull()

# O al revés, cuáles son válidos
fruta_res.notnull()

# En ocasiones, nos puede convenir quitarnos de en medio los valores nulos para que no nos 
# molesten mientras trabajamos. Para ello usamos dropna().
fruta_res.dropna()

# Si utilizamos dropna() con un DataFrame, podemos indicar si queremos descartar las filas con algún NaN 
# (comportamiento por defecto), o si queremos descartar las columnas con algún NaN.

# Si trabajamos con DataFrames
df_cuenta = DataFrame({
	                "tienda_1" : Series({"peras" : 2.25, "naranjas" : 5.70}),
	                "tienda_2" : Series({"peras" : 2.40, "naranjas" : 5.85, "uva" : 2.60}),
	                "tienda_3" : Series({"manzanas" : 1.70, "peras" : 2.30, "naranjas" : 5.70, "uva" : 3})})

# podemos descartar las filas con NAs
df_cuenta.dropna()

# o bien las columnas con NAs
df_cuenta.dropna(axis=1)

# Claro que también podemos preferir mantener todos los elementos, pero reemplazar los NA por 
# algún otro valor (p.ej. por un cero). Eso lo hacemos con fillna(). De hecho, esta operación es tan común 
# que Pandas incluye un argumento fill_value en sus métodos aritméticos para poder sustituir los 
# NaN del resultado con el valor que le indiquemos.

# Si usamos el método aritmético (`mul`) en lugar del operador (`*`)
# podemos utilizar el argumento `fill_value` directamente
fruta_kg.mul(fruta_precio, fill_value=0)


## FUNCIONES BÁSICAS DE AGREGACION Y ESTADISTICAS ##
---------------------------------------------------------------------------------------
# Pandas también incluye las operaciones básicas estadísticas y de cálculo de agregados.

# Supongamos que tenemos medidas del peso de varias personas (p1, p2, p3) a lo largo de varios años (2012..2016)
# FIJATE en el valor `None`
df_pesos = DataFrame({
	        "p1" : [ 82.9, 79.5,  80.1, None,  78.9], 
	        "p2" : [ 63.8, 63. ,  63.7, 65.2,  65.2],
	        "p3" : [ 73.5, 72.3,  71.8, 71.4,  69. ]
	        }, index = [2012, 2013, 2014, 2015, 2016])
	
# Podemos calcular el peso medio de cada persona a lo largo del tiempo
# (promedio de valores de todas las filas para cada columna)
df_pesos.mean()				# es equivalente a `df_pesos.mean(axis = 'rows')

# O calcular la media de los pesos observados cada año (promedio por valores de todas las columnas para cada fila, 
#  usando `axis = columns`)
df_pesos.mean(axis = 'columns')

# El comportamiento por defecto de las funciones estadísticas es calcular los agregados tomando los valores de todas 
# las filas, a lo largo de cada columna, reduciendo el resultado a una sola fila o serie (equivalente a usar el argumento 
# axis = 'rows').
# Si queremos calcular el agregado basado en los valores de todas las columnas a lo largo de cada fila, utilizamos 
# el argumento axis = 'columns'.

# ¿Te has fijado en el valor None que hemos metido en el DataFrame? Pandas lo transforma directamente a NaN. Sin embargo, 
# no afecta a los cálculos de mean(). En estas funciones de agregación, Pandas descarta por defecto los elementos con valor NaN. 
# Si preferimos que los tenga en cuenta, podemos utilizar el argumento 'skipna = False'. Ten en cuenta que, en este caso, las columnas 
# (o filas) que tengan algún valor NaN darán como resultado otro NaN.
df_pesos.mean(skipna = False)

# A continuación, tienes un cuadro resumen de las principales funciones de agregación y 
# estadísticas que puedes usar con Series y DataFrames:

# | Función       | Descripción                          |
# |---------------|--------------------------------------|
# | count()       | Número total de elementos (no nulos) |
# | sum()         | Suma de todos los elementos          |
# | prod()        | Producto de todos los elementos      |
# | mean()        | Valor medio                          |
# | median()      | Mediana                              |
# | std()         | Desviación típica                    |
# | var()         | Varianza                             |
# | quantile(q)   | Cuantil q-ésimo                      |
# | min()         | Valor mínimo                         |
# | max()         | Valor máximo                         |
# | first()       | Valor inicial                        |
# | last()        | Valor final                          |


## ÍNDICES JERÁRQUICOS ##
--------------------------------------------------------------------------------------------------------------------
# En algunas ocasiones nos vamos a encontrar con datos que encajarían mejor en una estructura con 
# más dimensiones, o en los que una de sus dimensiones esté compuesta por varios niveles o jerarquías. Pandas 
# ofrece la posibilidad de definir índices multi nivel o jerárquicos en cualquiera de las dimensiones de sus objetos.

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Recuerda ajustar la ruta de directorios para que apunte adonde hayas descargado los ficheros
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")
meteo_mes.head(8)

# Como ves, tenemos una columna con el año y otra con el mes. Las filas del DataFrame llevan la indexación secuencial por defecto. 
# En este caso, podría ser más natural que el año y el mes sirvieran de índice. Vamos a hacerlo, utilizando el método set_index().

# Ajustamos el índice del DataFrame para que use las columnas 'año' y 'mes'
meteo_mes.set_index(["año","mes"], inplace=True)
meteo_mes.head(10)

# Con set_index() le pedimos que utilice una o más columnas como nuevo índice para las filas. En este ejemplo puedes comprobar 
# como los valores de año y mes han reemplazado al índice secuencial de las filas, a la izquierda de la tabla, dejando 
# las columnas restantes del DataFrame como estaban. Este nuevo índice decimos que es jerárquico porque está organizado 
# en varios niveles. Cada columna indicada al definir el índice pasa a ser un nuevo nivel, organizados en el mismo orden 
# en el que se hayan especificado.

## -- ATENCION --
# Fíjate que en set_index() hemos incluido el argumento inplace=True. Con esta opción le indicamos que queremos que modifique 
# el contenido o estructura de la propia variable. Sin esta opción, el comportamiento por defecto es devolver una copia
# del DataFrame (o Series) con la modificación aplicada, dejando la variable original intacta. Pandas ofrece esta opción 
# en muchas de las operaciones con Series y DataFrames. Dependiendo de la situación te convendrá un modo u otro, pero tenlo 
# en cuenta para no encontrarte con resultados inesperados.

# Examinemos la definición del índice.
meteo_mes.index

# Los índices jerárquicos son objetos de clase MultiIndex. Podemos ver que está formado por dos niveles (levels), 
# el primer nivel con los valores de los años ([2015, 2016]) y el segundo nivel con los valores de los meses 
# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).

# En realidad, en este ejemplo las columnas con las variables de observaciones o medidas son la temperatura 
# y la velocidad del viento. Podemos considerar a la columna 'ciudad' como otro nivel para indexar. 
# Pero antes de incluirla, tenemos que limpiar la actual definición del índice.

# Para poder redefinir el índice, primero tenemos que hacer `reset`
meteo_mes.reset_index(inplace=True)

# Volvemos a tener el DataFrame como al principio
meteo_mes.head()

# Y ahora definimos de nuevo el índice.
meteo_mes.set_index(["ciudad","año","mes"], inplace=True)
meteo_mes.head(10)


## SELECCIONANDO ELEMENTOS ##
-------------------------------------------------------------------------------------------
# ¿Cómo accedemos a los elementos cuando tenemos un índice jerárquico? Es fácil si piensas 
# en cada elemento de este índice como en una tupla ordenada de sus valores.

# Para seleccionar un elemento mediante etiquetas debemos usar `loc`
meteo_mes.loc[("Bilbao", 2015, 1), :]

# ahora restringimos solo el primer nivel del índice
meteo_mes.loc[("Bilbao", ), :].head()
lib/python3.6/site-packages/pandas/core/indexing.py:1325: PerformanceWarning: indexing past lexsort depth may impact performance.
return self._getitem_tuple(key)

## -- IMPORTANTE --
# Antes de continuar, ¿te ha salido un mensaje de aviso? Algo como:
# PerformanceWarning: indexing past lexsort depth may impact performance.
# Con este mensaje Pandas viene a decirnos que estamos filtrando por un índice que no tiene sus valores correctamente ordenados. 
# La operación va a funcionar igual, pero puede ser mucho más lenta que si tuviera el índice ordenado nivel a nivel.
# Podemos reordenar el índice del DataFrame usando sort_index().

# Reordenamos el índice de filas (axis=0)
# empezando por el primer nivel (level=0)
meteo_mes.sort_index(level=0, axis=0, inplace=True)
meteo_mes.loc[("Bilbao", ), :].head()


## INDICES JERARQUICOS SOBRE COLUMNAS ##
---------------------------------------------------------------------------------------------------------
# Las columnas de un DataFrame no dejan de ser un índice, como ocurre con las filas. Así que sí, 
# podemos tener índices jerárquicos también sobre las columnas de un DataFrame.

# Vamos a extraer DataFrames parciales con los datos de algunos municipios. Datos completos de Bilbao, Valencia y Zaragoza
bilbao = meteo_mes.loc[("Bilbao",) , :]
valencia = meteo_mes.loc[("Valencia",) , :]
zgz = meteo_mes.loc[("Zaragoza",) , :]
	
# Y los combinamos en un solo DataFrame:
meteo_bvz = pd.concat([bilbao, valencia, zgz], axis=1)
meteo_bvz.head()

# La función pd.concat() de Pandas permite concatenar varios DataFrame, añadiendo las filas de cada uno al final 
# del anterior (esta es la opción por defecto, 'axis = 0'), o bien añadiendo las columnas de cada uno a continuación 
# del anterior (con la opción 'axis = 1').

# Como ves, al concatenar por columnas, los nombres están repetidos.

## -- IMPORTANTE --
# Es importante que en el DataFrame resultante solo queden aquellas columnas con las que se desee trabajar.
# Por lo que será necesario que antes del proceso de concatenación se eliminan aquellas que no vayan a resultar relevantes 
# o que durante el proceso de concatenación se seleccionen solo aquellas que se desean conservar en el DataFrame final.

# Podemos crear un índice multinivel usando los métodos de `pd.MultiIndex` de Pandas 
idx = pd.MultiIndex.from_product([["Bilbao","Valencia","Zaragoza"], 
	                                  ["temp_c","viento_vel_kmh"]], 
	                                 names = ["ciudad","variable"])
# Reemplazamos el índice con los nombres de columnas actuales por el nuevo índice multinivel
meteo_bvz.columns = idx
meteo_bvz.head()

# En el método from_product() de la clase MultiIndex primero pasamos una lista que a su vez contiene una lista de etiquetas 
# por cada nivel del índice. En nuestro ejemplo, la primera sublista tiene los nombres de las ciudades, y la segunda el nombre 
# de las variables. El índice se creará con tantas columnas como combinaciones entre elementos de cada nivel 
# (su producto cartesiano). En el argumento names indicamos el nombre de cada nivel del índice jerárquico.
# Ahora podemos seleccionar también usando los distintos niveles de las columnas.

# Indicando solo el primer nivel
meteo_bvz["Valencia"].head()

# O especificando todos los niveles
meteo_bvz[("Valencia","temp_c")].head()

# También podemos seleccionar simultáneamente por filas y columnas multinivel
meteo_bvz.loc[(2016, [1,3]), "Bilbao"]

# Si necesitamos hacer selecciones más complejas, como hacer rebanadas de los distintos niveles, la forma más sencilla 
# es utilizar un objeto IndexSlice. Se trata de una herramienta auxiliar que se encarga de facilitarnos la manera 
# de escribir expresiones de selección multinivel complicadas.

# Creamos un objeto IndexSlice
ixs = pd.IndexSlice

# y lo utilizamos directamente para seleccionar rebanadas en índices multi-nivel
meteo_bvz.loc[ixs[2016, 2:5], ixs["Bilbao",:]]


## CONCATENANDO DATOS ##
-------------------------------------------------------------------------------------
# En uno de los ejemplos del apartado anterior ya usamos la función pd.concat(). Con esta función podemos combinar 
# dos o más Series o DataFrames, concatenándolos por cualquiera de sus ejes, por filas o por columnas.















