# --------------
### PANDAS ###
# --------------

# -- [ PARA SABER MAS ] --
# http://pandas.pydata.org/ 
# http://pandas.pydata.org/pandas-docs/stable/10min.html 
# https://pandas.pydata.org/pandas-docs/stable/tutorials.html 
# https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html 


# -------------------------------------------------------------------------------------------------------
# --( 1 )-- PROCESAMIENTO Y ANALISIS DE DATOS: PANDAS
# -------------------------------------------------------------------------------------------------------


## ESTRUCTURAS DE DATOS BÁSICAS: SERIES ##
# ------------------------------------------------------------------------
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
print (s1)

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
print (temp_anual)

# Los índices son etiquetas, también pueden ser texto
# # P.ej. en una serie de temperaturas medias mensuales
# usamos los meses como índices.
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
	            index = ["Ene","Feb","Mar","Abr","May","Jun",
	                    "Jul","Ago","Sep","Oct","Nov","Dic"])
print (temp_mensual)

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
print (s1 * 2)

# ... operaciones elemento a elemento entre series
s2 = Series([2,3,4,5])
print (s1 - s2)


# DATAFRAMES #
# --------------------------------------------------------------------------------------
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
print (df1)

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
print (df2)

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
print (df3)

# Podemos listar la secuencia de etiquetas que forman el índice, o la secuencia de etiquetas 
# con los nombres de las columnas de un DataFrame. Como ves, la información de los nombres del índice 
# (filas) y de los nombres de las columnas se almacenan ambas en objetos de tipo Index.

# Índice asociado al DataFrame
print (df3.index)

# Columnas del DataFrame
print (df3.columns)

# Operaciones #

# Tamaño del DataFrame (num. filas, num. columnas)
print (df3.shape)

# La forma más rápida de sacar el número de filas
print (df3.shape[0])

# Tamaño total (num. total de elementos)
print (df3.size)

# Mostrar las N primeras filas (5 por defecto)
df3.head()

# o las N últimas
df3.tail(3)

# Conteo de elementos no nulos en cada columna
print (df3.count())

# Resumen con estadísticas básicas de cada columna
df3.describe()


# SELECCION Y FILTRADO #
# ----------------------------------------------------------------------------------------
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
print (df_meteo["lluvia_mm"])

# También podemos acceder a una columna como si fuera un atributo, usando la notación con punto.
print (df_meteo.temp_c)

# No obstante, aunque el acceso a una columna del DataFrame como si fuera un atributo puede resultar 
# un atajo muy cómodo, hay que tener cuidado. Si el nombre de una columna coincide con el nombre de alguno 
# de los atributos o métodos propios de la clase DataFrame, será esto a lo que estaremos accediendo, 
# no a la columna.

# Un DataFrame de ejemplo con fórmulas para el área
# de distintas figuras geométricas
df_geom = DataFrame({
	        'shape' : ["triangle","square","circle"],
	        'area' : ["b*h/2", "a*a", "PI*r*r"]})

# Accedemos a la columna "shape" con corchetes
print (df_geom["shape"])

# Así accedemos a un atributo propio de la clase DataFrame
# que nos dice el número de filas y columnas que tiene (su "forma")
print (df_geom.shape)

# Como ves, el atajo para acceder a una columna como un atributo no siempre va a funcionar. 
# Te recomendamos que utilices los corchetes como opción preferente. Y en especial, cuando tengas que asignar 
# valores a una columna, habrás de utilizar siempre la notación con corchetes.

# Además, utilizando los corchetes podemos dar una lista de nombres de columnas para elegir varias a la vez.
print (df_meteo[["imes","temp_c"]])

# Pero los corchetes también tienen otra funcionalidad. Si lo que indicamos entre corchetes es un rango o rebanada 
# utilizando el operador ':' (como hacemos con las listas normales), ¡entonces no seleccionamos columnas, sino filas!

# Indicamos un rango o "rebanada" de índices
print (df_meteo[0:4])

# También podemos usar "rebanadas" de etiquetas si el índice del DataFrame está etiquetado
print (df_meteo["Ene":"Mar"]) # --> Seleccionar filas de enero a marzo

# Lo mismo ocurre si entre corchetes escribimos una expresión o máscara booleana. 
# La máscara resultante se aplicará a las filas.

# Seleccionar las filas (meses) en las que la temperatura supere los 20ºC
print (df_meteo[df_meteo.temp_c > 20.0])

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
print (df_meteo.loc["May", "lluvia_mm"])

# seleccionar una fila entera
print (df_meteo.loc["May", ])

# seleccionar una columna entera
print (df_meteo.loc[:, "humedad"])

# o un subconjunto de filas y columnas
print (df_meteo.loc["Feb":"Abr", ["lluvia_mm","humedad"]])

# Mientras que df.iloc está pensado para seleccionar indicando la posición (como en una lista o un array de NumPy).

# Acceso mediante índices de posición con df.iloc. Podemos seleccionar un elemento concreto ([fila, columna])
print (df_meteo.iloc[6, 2])

# seleccionar una fila entera
print (df_meteo.iloc[6, ])

# seleccionar una columna entera
print (df_meteo.iloc[:, 1])

# o un subconjunto de filas y columnas
print (df_meteo.iloc[0:3, 1:3])

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
# -------------------------------------------------------------------------------
# Pandas incluye varias funciones para leer datos tabulares de ficheros de texto:

# | Función         | Descripción                                                                              		|
# |-----------------|-----------------------------------------------------------------------------------------------|
# | pd.read_csv()   | Carga datos de un fichero de tipo CSV, con los campos separados por comas ';'            		|
# | pd.read_table() | Carga datos de un fichero de texto tabular, con los campos separados por tabuladores ('\t') 	|
# | pd.read_fwf()   | Carga datos de un fichero de texto con columnas de ancho fijo                             	|

# Para ver cómo funcionan, vamos a leer los datos de uno de los ficheros CSV que están incluidos en el material
# de la unidad. En este caso, vamos a cargar el fichero NYC_flights_2013_MINI.csv que viene de la siguiente URL:
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
# | sep               e          | Carácter delimitador de campos. Por defecto ';' para read_csv y '\t' para read_table  |
# | header                      | Indica si el fichero contiene una fila con los nombres de las columnas y              |
# |								| puede indicar nº de fila (0) 															|
# | names                       | Lista opcional de nombres para las columnas                                           |
# | na_values                   | Lista de cadenas que representan valores ausentes (NAs) en el fichero                 |
# | quotechar                   | Carácter utilizado en el fichero para entrecomillar cadenas de texto                  |
# | encoding                    | Codificación o juego de caracteres utilizado (p.ej. ascii, latin1, utf8)              |


## ESCRIBIENDO DATOS A FICHERO ##
# ----------------------------------------------------------------------------------------------------------------
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


# -------------------------------------------------------------------------------------------------------
# --( 2 )-- OPERACIONES CON DATOS
# -------------------------------------------------------------------------------------------------------


## OPERACIONES BINARIAS. ALINEACION DE INDICES ##
# --------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------
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
# --------------------------------------------------------------------------------------------------------------------
# En algunas ocasiones nos vamos a encontrar con datos que encajarían mejor en una estructura con 
# más dimensiones, o en los que una de sus dimensiones esté compuesta por varios niveles o jerarquías. Pandas 
# ofrece la posibilidad de definir índices multi nivel o jerárquicos en cualquiera de las dimensiones de sus objetos.

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Recuerda ajustar la ruta de directorios para que apunte adonde hayas descargado los ficheros
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")
print(meteo_mes.head(8).to_string())
# Como ves, tenemos una columna con el año y otra con el mes. Las filas del DataFrame llevan la indexación secuencial por defecto. 
# En este caso, podría ser más natural que el año y el mes sirvieran de índice. Vamos a hacerlo, utilizando el método set_index().

# Ajustamos el índice del DataFrame para que use las columnas 'año' y 'mes'
meteo_mes.set_index(["año","mes"], inplace=True)
print(meteo_mes.head(10).to_string())
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
print(meteo_mes.head().to_string())
# Y ahora definimos de nuevo el índice.
meteo_mes.set_index(["ciudad","año","mes"], inplace=True)
print(meteo_mes.head(10).to_string())
## SELECCIONANDO ELEMENTOS ##
# -------------------------------------------------------------------------------------------
# ¿Cómo accedemos a los elementos cuando tenemos un índice jerárquico? Es fácil si piensas 
# en cada elemento de este índice como en una tupla ordenada de sus valores.

# Para seleccionar un elemento mediante etiquetas debemos usar `loc`
meteo_mes.loc[("Bilbao", 2015, 1), :]

# Reordenamos el índice de filas (axis=0)
# empezando por el primer nivel (level=0)
meteo_mes.sort_index(level=0, axis=0, inplace=True)
print(meteo_mes.loc[("Bilbao", ), :].head().to_string())
## INDICES JERARQUICOS SOBRE COLUMNAS ##
# ---------------------------------------------------------------------------------------------------------
# Las columnas de un DataFrame no dejan de ser un índice, como ocurre con las filas. Así que sí, 
# podemos tener índices jerárquicos también sobre las columnas de un DataFrame.

# Vamos a extraer DataFrames parciales con los datos de algunos municipios. Datos completos de Bilbao, Valencia y Zaragoza
bilbao = meteo_mes.loc[("Bilbao",) , :]
valencia = meteo_mes.loc[("Valencia",) , :]
zgz = meteo_mes.loc[("Zaragoza",) , :]
	
# Y los combinamos en un solo DataFrame:
meteo_bvz = pd.concat([bilbao, valencia, zgz], axis=1)
print(meteo_bvz.head().to_string())
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
print(meteo_bvz.head().to_string())
# En el método from_product() de la clase MultiIndex primero pasamos una lista que a su vez contiene una lista de etiquetas 
# por cada nivel del índice. En nuestro ejemplo, la primera sublista tiene los nombres de las ciudades, y la segunda el nombre 
# de las variables. El índice se creará con tantas columnas como combinaciones entre elementos de cada nivel 
# (su producto cartesiano). En el argumento names indicamos el nombre de cada nivel del índice jerárquico.
# Ahora podemos seleccionar también usando los distintos niveles de las columnas.

# Indicando solo el primer nivel
print(meteo_bvz["Valencia"].head().to_string())
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


# -------------------------------------------------------------------------------------------------------
# --( 3 )-- TRANSFORMANDO LOS DATOS
# -------------------------------------------------------------------------------------------------------


## CONCATENANDO DATOS ##
# -------------------------------------------------------------------------------------
# En uno de los ejemplos del apartado anterior ya usamos la función pd.concat(). Con esta función podemos combinar 
# dos o más Series o DataFrames, concatenándolos por cualquiera de sus ejes, por filas o por columnas.
# Preparamos dos DataFrame sencillos de ejemplo

df1 = DataFrame({'x' : np.arange(1,5), 'y' : np.arange(5, 9)})
df2 = DataFrame({'x' : np.arange(1,4), 'z' : np.arange(11, 14)})
print(df1)
print(df2)

# Concatenamos las filas de los dos DataFrames (equivalente a poner explícitamente la opción `axis='rows'`)
print(pd.concat([df1, df2]).to_string())
# El argumento principal de pd.concat() es una lista con los DataFrames que queremos concatenar. Si no indicamos 
# nada más, concatena las filas de todos los DataFrames. Esto es equivalente a poner de forma explícita la opción 
# axis = 'rows'. Fíjate que como el primer DataFrame no tiene columna z, en el resultado las filas que vienen de df1 
# muestran el valor NaN para esa columna. De la misma forma, como el segundo DataFrame no tiene columna y, 
# en el DataFrame final las filas que vienen de df2 muestran el valor NaN para esa columna. Probablemente también 
# te has dado cuenta de que en el índice de filas (a la izquierda) hay valores repetidos, porque pd.concat() 
# ha mantenido los índices de los DataFrames originales. Podemos pedirle que descarte estos índices originales 
# y cree unos nuevos.

print(pd.concat([df1, df2], ignore_index=True).to_string())
# Si lo que necesitamos es concatenar las columnas, basta con indicar la opción axis = 'columns'.
print(pd.concat([df1, df2], axis = 'columns').to_string())
# Como ves, aparecen valores NaN en las dos últimas columnas de la fila 3, porque el DataFrame df2 
# solo tenía valores de las filas 0 a la 2. Además, la columna x está duplicada, ya que la tenemos 
# en los dos DataFrames. Es el mismo comportamiento que al concatenar filas.

# Para lidiar con los nombres de filas o columnas duplicados, otra opción aparte de ignorar los índices 
# originales es añadir un nivel por cada DataFrame que combinamos.

# Añadir un nivel etiquetando los datos de cada DataFrame
print(pd.concat([df1, df2], axis = 'columns', keys = ["DF1","DF2"]).to_string())
## COMBINANDO DATOS: MERGE Y JOIN ##
# ---------------------------------------------------------------------------------------------
# Se pueden combinar objetos data.frame usando merge u otras funciones de librerías externas.
# Esta forma de combinar datos tabulares es análoga a las típicas operaciones JOIN del lenguaje SQL.
# En Pandas disponemos del método pd.merge() como herramienta principal para combinar datos.

# Primero los datos de peliculas
peliculas = pd.read_csv("./U09_datasets/sample_movie_list.csv", sep=";")
print(peliculas.head().to_string())
# y unos datos de valoración de los espectadores
valoracion = pd.read_csv("./U09_datasets/sample_movie_rating.csv", sep=";")
print (valoracion.head())

# Ahora podemos cruzar los dos DataFrames con pd.merge().
print(pd.merge(peliculas, valoracion).head().to_string())
# El método pd.merge() identifica automáticamente las columnas que aparecen con el mismo nombre 
# en los dos DataFrames y las usa como clave de unión. Si queremos indicar o restringir manualmente 
# qué columnas usar como clave de unión, utilizamos la opción on.

print(pd.merge(peliculas, valoracion, on=['title']).head().to_string())
# Ahora miramos cuantas filas tiene cada dataframe:
print("Filas en peliculas:", peliculas.shape[0])
print("Filas en valoraciones:", valoracion.shape[0])
print("Filas en merge:", pd.merge(peliculas, valoracion).shape[0])

# pd.merge() por defecto devuelve solo las combinaciones de filas cuya clave aparece en ambos DataFrames.
# En este caso, hay películas para las que no tenemos valoración, así que esas filas quedan descartadas.
# Podemos controlar si queremos que se incluyan todas las filas del primer, segundo o ambos DataFrames 
# a pesar de que las claves no tengan correspondencia en los dos. Lo hacemos con la opción how, 
# que puede tomar los siguientes valores.

# | Valor   | Descripción                                                                            | SQL               |
# |---------|----------------------------------------------------------------------------------------|-------------------|
# | 'inner' | Incluye filas si la clave está en ambos DataFrames (opción por defecto)                | INNER JOIN        |
# | 'left'  | Todas las filas del DataFrame izquierdo; completa el derecho con NaN si faltan claves  | LEFT OUTER JOIN   |
# | 'right' | Todas las filas del DataFrame derecho; completa el izquierdo con NaN si faltan claves  | RIGHT OUTER JOIN  |
# | 'outer' | Todas las filas de ambos DataFrames; completa con NaN si faltan claves en uno u otro   | OUTER JOIN        |

# Probemos con nuestros DataFrames.
print(pd.merge(peliculas, valoracion, how='left').head().to_string())
# ahora aparecen películas en el cruce que antes quedaban descartadas por no tener valoración. 
# En estas nuevas filas incluidas ahora, las columnas del segundo DataFrame toman 
# valor NaN, es decir, ausente o nulo. Algunas veces los nombres de las columnas a cruzar no 
# aparecen igual en los DataFrames.

generos = pd.read_csv("./U09_datasets/sample_movie_genres.csv", sep=";")
print(generos.head())

# En estos casos usamos los argumentos left_on y right_on para indicar explícitamente 
# qué columnas usar como claves en cada DataFrame

print(pd.merge(peliculas, generos, left_on="title", right_on="movie_title").head().to_string())
# El resultado contiene las columnas utilizadas como clave de ambos DataFrames, lo cual es redundante. 
# Podemos descartar una de las columnas utilizando drop().

print(pd.merge(peliculas, generos, left_on="title", right_on="movie_title").drop("movie_title", axis="columns").head().to_string())
# Si los dos DataFrames tienen definido un índice común a nivel de filas, podemos utilizarlo para hacer el cruce:
# Vamos a utilizar el título como índice en ambos DataFrame
peliculas.set_index("title", inplace=True)
generos.set_index("movie_title", inplace=True)

# y ahora cruzamos indicando que queremos usar 
# el `left_index` y el `right_index`
print(pd.merge(peliculas, generos, left_index=True, right_index=True).head().to_string())
# Al igual que anteriormente con la concatenación, la operación de cruzar dos DataFrames por su 
# índice es tan habitual que Pandas incluye un método más directo por comodidad: join().

# Podemos usar el método `join()` de un DataFrame
print(peliculas.join(generos).head().to_string())
## ORDENANDO ELEMENTOS ##
# -------------------------------------------------------------
# Ordenar nuestros datos es otra operación básica disponible tanto para Series como DataFrames.
# Si queremos ordenar por los valores, tenemos el método sort_values().

# Ordenamos un objeto Series
temp_mensual = Series([7.2, 7.3, 12.1, 15.7, 20.3, 24.8, 
	                       28.2, 25.6, 20.8, 16.8, 12.3, 7.8],
	                     index = ["Ene","Feb","Mar","Abr","May","Jun",
	                              "Jul","Ago","Sep","Oct","Nov","Dic"])
print(temp_mensual.sort_values())

# Si vamos a ordenar un DataFrame, tendremos que indicar la(s) columna(s) 
# a utilizar (si es más de una, las incluimos en una lista).

df_meteo = DataFrame({'imes' : np.arange(1, 13),
	                      'temp_c' : temp_mensual,
	                      'lluvia_mm' : [21, 22, 19, 39, 44, 26, 
	                                     17, 17, 30, 36, 30, 21],
	                      'humedad' : [75, 67, 59, 57, 54, 49, 
	                                   47, 51, 57, 67, 73, 76]}, 
	                   columns = ['imes','temp_c','lluvia_mm','humedad'],
	                    index = ["Ene","Feb","Mar","Abr","May","Jun",
	                             "Jul","Ago","Sep","Oct","Nov","Dic"])
# ordenar por la columna `lluvia_mm`
print(df_meteo.sort_values("lluvia_mm"))

# Además de ordenar por sus valores, también podemos ordenar una colección de datos por su índice mediante el método 
# sort_index(). Esto puede resultar útil cuando el índice está formado por etiquetas (y no el secuencial por defecto)

# Ordenar las filas lexicográficamente
# según la etiqueta del índice (meses)
print(df_meteo.sort_index())


## ELIMINAR DUPLICADOS ##
# ----------------------------------------------------------------------------------------------------------------
# Otra circunstancia común cuando trabajemos con datos es que aparezca información duplicada. En ocasiones serán 
# registros completos, pero otras veces pueden ser solo valores o medidas múltiples que comparten el resto de variables.

# Cargamos datos de reparto de actores por película
reparto = pd.read_csv("./U09_datasets/sample_movie_cast.csv", sep=";")
print (reparto.head())

# El DataFrame de ejemplo contiene algunos de los actores que han protagonizado cada película. 
# Ahora nos gustaría quedarnos simplemente con una lista de actores.

# Extraemos solo los actores
actores = reparto[["actor_name","actor_fb_likes"]].copy().head()

# Pero probablemente vamos a tener actores repetidos porque hayan aparecido en varias de las películas de nuestra lista. 
# Empleamos el método duplicated() para averiguarlo.

actores.duplicated(["actor_name"]).any()
True

# Por defecto, duplicated() tiene en cuenta todas las columnas de un DataFrame para decidir si una fila está repetida 
# o no. Como alternativa, se puede especificar un subconjunto de las columnas (como en este ejemplo).
# El método duplicated() devuelve una serie con tantos valores booleanos como elementos. La primera vez que aparece 
# un elemento devuelve False, y las siguientes ocurrencias las marca con True.

# Ahora podemos eliminar las filas duplicadas con drop_duplicates().

actores.drop_duplicates(["actor_name"], inplace=True)
actores.duplicated(["actor_name"]).any()
False


## APLICANDO FUNCIONES ##
# ---------------------------------------------------------------------------------------------------------------
# Podemos necesitar aplicar una función recorriendo uno de los ejes de nuestros datos. Por ejemplo, fila a fila 
# en un DataFrame (o columna a columna). Pandas nos permite hacer esto mismo mediante el método apply().

# Calcular la diferencia entre ingresos y presupuesto de cada película
peliculas.apply(lambda p: p.gross - p.budget, axis="columns").head()

# En este ejemplo hemos usado una expresión lambda sencilla, pero podemos utilizar una expresión o función todo 
# lo compleja que necesitemos para nuestros cálculos.


## DISCRETIZANDO VARIABLES ##
# -------------------------------------------------------------------------------------
# Otra transformación típica de datos es la discretización o agrupación en rangos de valores de una determinada variable. 
# Para ello en Pandas disponemos de la función pd.cut().

# Por ejemplo, vamos a clasificar el año de estreno de las peliculas de nuestro dataset por décadas (más o menos).
# Tomamos el año de estreno de las películas
peliculas['year'].head()

# Utilizamos `pd.cut()` para dividir en intervalos
pd.cut(peliculas['year'], bins=[1900, 1980, 1990, 2000, 2010, np.inf]).head()

# Para cada valor de la serie, pd.cut() devuelve la etiqueta de la categoría o rango correspondiente. En este caso, 
# vemos que hay cinco categorías, cuyos límites están comprendidos entre cada par de valores de la lista que hemos 
# indicado en el argumento bins. Si queremos cambiar las etiquetas que se crean por defecto, podemos pasar una lista 
# o un array de nombres en el argumento labels. Una vez que tenemos nuestra variable discretizada, podemos contar 
# cuántos casos hay en cada rango con la función pd.value_counts().

decadas = pd.cut(peliculas['year'], 
	               bins=[1900, 1980, 1990, 2000, 2010, np.inf], 
	              labels = ['<1980', '1980s', '1990s', '2000s', '>2010'])
pd.Series(decadas).value_counts()


# -------------------------------------------------------------------------------------------------------
# --( 4 )-- AGRUPANDO Y AGREGANDO DATOS
# -------------------------------------------------------------------------------------------------------


# Uno de los procedimientos de análisis de datos más común consiste en dividir nuestro conjunto 
# de datos en grupos disjuntos en base a algún criterio o variables y realizar algún tipo de operación 
# o análisis sobre cada grupo, como calcular estadísticas del grupo (valores medios, mínimos, máximos, etc.).

# Este tipo de procesos sobre grupos de datos te resultará familiar si has trabajado con bases de datos, 
# ya que es similar a las cláusulas tipo GROUP BY de SQL. En el mundo del Big Data este modelo de computación 
# es conocido como map-reduce "split, apply, combine".

# En Pandas, los objetos de tipo DataFrame incorporan el método groupby() para ejecutar estos procesos.

# Volvamos a cargar los datos meteorológicos
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")

# Calculamos valores promedio agrupando por ciudad
meteo_mes.groupby('ciudad').mean()

# En este ejemplo hemos agrupado las filas según la columna ciudad y después hemos pedido calcular 
# los valores promedio para cada grupo. Como ves, la función mean() se ha aplicado a todas las columnas 
# (en este caso, a las de tipo numérico). Este es el comportamiento por defecto cuando usamos funciones 
# de agregación sobre el resultado de df.groupby().

# Podemos seleccionar las columnas sobre las que queremos aplicar la función, indexando como haríamos con un DataFrame:
# Indexamos columnas sobre el resultado de `df.groupby()
# antes de aplicar la función
meteo_mes.groupby('ciudad')['temp_c'].mean()

# El método df.groupby() también nos permite especificar varias columnas como criterio de agrupación. 
# En este caso, utilizamos una lista con los nombres de las columnas para agrupar.

# Valor promedio agrupando por ciudad y año
meteo_mes.groupby(['ciudad','año'])['temp_c'].mean().head()

# El método df.groupby() devuelve un objeto de tipo DataFrameGroupBy. A efectos prácticos, 
# podemos considerarlo como una colección de DataFrames, uno por grupo creado.
# Sobre los grupos resultantes podemos aplicar directamente cualquiera de las funciones de agregación 
# y estadísticas que ya te hemos presentado. Pero hay mucho más. Disponemos de varios métodos para 
# realizar distintos tipos de operaciones sobre cada grupo.


## AGREGADOS SOBRE GRUPOS ##
# ------------------------------------------------------------------------------------------------------------------------
# Empecemos por el método aggregate(). Este método nos permite calcular múltiples valores agregados de forma simultánea, 
# indicando en una lista las funciones de agregación a utilizar.

# Agrupamos por ciudad y calculamos los valores de media y mediana de temperatura y velocidad de viento para cada ciudad:
# opción rápida, igual que tu idea pero correcta
meteo_mes.groupby('ciudad')[['temp_c','viento_vel_kmh']].agg(['mean','median','min'])


# ¿Has prestado atención cómo hemos usado el método aggregate()? Este ejemplo te muestra distintas formas de especificar 
# las funciones de agregación a aplicar. En el primer elemento hemos escrito una cadena de texto para referirnos a la media. 
# Pandas permite hacer esto con las operaciones comunes incluidas, él se encarga de traducir la cadena de texto a la función 
# correspondiente. En el segundo elemento hemos utilizado directamente el nombre de una función y no una cadena de texto 
# (en este caso el método para calcular la mediana de la librería NumPy). Y en el último elemento incluimos una expresión 
# lambda a medida (también podríamos haber puesto el nombre de una función definida por nosotros. Ha creado un índice 
# jerárquico para las columnas. En el primer nivel tienes los nombres de las columnas originales y en el segundo nivel 
# el nombre de los agregados que hemos calculado.


## FILTRAGO DE GRUPO ##
# ------------------------------------------------------------------------------------------------------------------------
# El método filter() nos permite decidir si queremos incluir los datos de un grupo o no, en base a una función de filtrado 
# sobre el conjunto de valores de cada grupo. La función de filtrado debe devolver un valor booleano para cada valor 
# de entrada. Por ejemplo, vamos a filtrar y descartar las ciudades cuya velocidad de viento promedio supere los 12km/h.

meteo_mes.groupby('ciudad').filter(lambda x: x['viento_vel_kmh'].mean() < 12).head()

# Ten en cuenta que el resultado de esta operación es un DataFrame como el original, 
# pero sin los datos de los grupos excluidos.


## TRANSFORMACION DE DATOS POR GRUPOS ##
# ------------------------------------------------------------------------------------------------------------------------
# Cuando calculamos valores agregados por grupos, estamos reduciendo el DataFrame de cada grupo con sus múltiples 
# filas u observaciones a una sola fila con los resultados de la agregación. Pero podemos estar interesados en mantener 
# los registros o filas originales, y simplemente modificar sus valores en base a las características de cada grupo. 
# Un ejemplo típico sería la normalización de variables por grupos. Para este tipo de operaciones 
# utilizamos el método transform().

# Normalizamos la variable `temperatura` por grupos
Z_temp_c = meteo_mes.groupby('ciudad')['temp_c'].transform(lambda x: (x - x.mean())/x.std())
print(pd.concat([meteo_mes, Z_temp_c], axis = 'columns').head().to_string())
# La función que usemos debe devolver un valor de salida simple para cada valor de entrada. El resultado de transform() 
# es un objeto Series con un valor por cada fila (temperatura) del DataFrame original.


## APLICANDO FUNCIONES ARBITRARIAS ##
# ------------------------------------------------------------------------------------------------------------------------
# Si lo que queremos es devolver directamente un DataFrame por cada grupo, podemos utilizar el método apply(). 
# El argumento debe ser una función que recibirá el DataFrame correspondiente a un grupo y que devolverá un nuevo 
# DataFrame arbitrario como resultado.

# Función que añade una nueva columna  con la variable temperatura normalizada
def fnorm(x):
	x['Z_temp_c'] = (x['temp_c'] - x['temp_c'].mean())/x['temp_c'].std()
	return x
# Aplicar la función por grupos
meteo_col_aggs = (meteo_mes.groupby('ciudad')[['temp_c', 'viento_vel_kmh']].agg(['mean', 'median', 'min']))

## REORGANIZANDO FILAS Y COLUMNAS. TABLAS RESUMEN ##
# ---------------------------------------------------------------------------------------------
# ¿Y si quisiéramos que los valores promedio para cada año aparecieran organizados en columnas? 
# En Pandas podemos hacer esto con el método unstack()

print(meteo_mes.groupby(['ciudad','año'])['temp_c'].mean().unstack().to_string())
# unstack() por defecto toma el nivel más interno del índice (en este caso año) y "desapila" los datos, 
# generando una nueva columna por cada valor del índice. Dicho de otra forma, pivotamos un nivel del índice 
# de filas al eje de columnas. La operación contraria para pivotar o mover niveles del eje de columnas 
# al eje de filas la realizamos con stack().

# Retomemos otro ejemplo anterior con múltiples agregados por columna
meteo_col_aggs = meteo_mes.groupby('ciudad').agg(
    temp_mean=('temp_c','mean'),
    temp_median=('temp_c','median'),
    temp_min=('temp_c','min'),
    viento_mean=('viento_vel_kmh','mean'),
    viento_median=('viento_vel_kmh','median'),
    viento_min=('viento_vel_kmh','min'),)

meteo_mes.groupby('ciudad')[['temp_c','viento_vel_kmh']].agg(['mean','median','min'])

# Apilar como filas el primer nivel del eje de columnas
print(meteo_col_aggs.stack(level = 0).head().to_string())
# Aquí hemos apilado explícitamente el primer nivel del eje de columnas, utilizando el argumento 'level = 0'.
# La generación de tablas resumen de valores agregados, combinando distintas dimensiones en los ejes de filas 
# y columnas, es algo de uso cotidiano. Es posible que ya las hayas utilizado y te suenen por el nombre de pivot tables
# o tablas dinámicas en otros contextos. Pandas proporciona un mecanismo muy sencillo para generar este tipo de tablas, 
# mediante el método pd.pivot_table().

# Crear una tabla resumen con la temperatura promedio para cada ciudad (filas) y año (columnas):
print(meteo_mes.pivot_table('temp_c', index = 'ciudad', columns = 'año', aggfunc='mean').to_string())
# El primer argumento indica las columnas con los valores que queremos procesar. Con el segundo argumento (index) 
# especificamos los valores para el eje de filas, y con el tercero el eje de columnas. Por último, indicamos 
# la función de agregación a aplicar a cada grupo (por defecto calcula la media).
































