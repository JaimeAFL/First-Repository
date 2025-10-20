### FUNCIONES ###

# Una función es un conjunto de operaciones que sirven para completar un cálculo o tarea específica y que se agrupan 
# y encapsulan como unidades de código independientes para poder ser reutilizadas a lo largo de nuestro programa siempre 
# que sea necesario. El uso de funciones nos permite no tener que reescribir el mismo código en distintas partes de nuestro 
# programa, sustituyéndolo por llamadas a una función. No solo tiene la ventaja de la reutilización y evitarnos escribir 
# mucho más código. También hace los programas más modulares y fáciles de leer, depurar y modificar. En Python indicamos que 
# vamos a definir una función utilizando la plabra reservada 'def'.

#Vamos a definir la función:
def mi_primera_funcion():
    print ("Soy la primerita función")

# Podemos dividir la definición en dos partes: el encabezado y el cuerpo. El encabezado empieza con la palabra clave 'def', 
# seguida del nombre de la función (mi_primera_funcion). Para los nombres de funciones se aplican las mismas reglas que para 
# los nombres de variables. Después del nombre de la función se colocan los paréntesis de apertura y cierre y finalmente los 
# dos puntos (:) para indicar el final de la cabecera. Justo después del encabezado, en la linea siguiente, comienza el cuerpo 
# de la función, que es donde incluiremos todas las instrucciones quer componen el cálculo o tarea que queremos implementar. 
# Al igual que vimos con las sentencias de control de flujo, este cuerpo va identado respecto a la cabecera. La primera línea 
# que vuelva al mismo nivel de identación que el encabezado nos marcará el fin de la función. Una vez que tenemos definida la 
# función, ya podemos utilizarla. Para 'invocar' una función, simplemente utilizaremos su nombre seguido de los paréntesis.

mi_primera_funcion()

# En el caso de las funciones, Python permite añadir una documentación específica añadiendo una cadena de texto justo entre el 
# encabezado y el cuerpo de la función. Aestas cadenas en Python se las conoce como 'docstring'. Normalmente se utilizan cadenas 
# rodeadas por comillas triples. Utiliza las docstrings para describir qué es lo que hacen tus funciones y qué parámetros necesitan.

def mi_primera_funcion():
    """ Función trivial de ejemplo. Imprime un mensaje de prueba."""
    print ("Soy la primerita función")

# Podemos  hacer que la función devuelva un valor como resultado utilizando la sentencia 'return'. Podemos añadir parámetros 
# que necesita la función para utilizarlos en sus cálculos. Indicamos los parámetros a la función añadiéndolos entre los 
# paréntesis de la definición, como nombres de variables.

# Definimos una nueva función que devuelve el cuadrado del número x que pasamos como argumento
def cuadrado (x):
    """ Devuelve el cuadrado del número x"""
    return x**2
# Probamos que funciona
print ("El cuadrado de 7 es", cuadrado(7))
print ("El cuadrado de 12 es", cuadrado (12))

# En esta nueva función 'cuadrado' hemos incluido el parámetro 'x'. Dentro del cuerpo de la función podemos utilizar el parámetro 
# como si fuera una variable normal. Cuando llamamos a la función dentro de la sentencia 'print', lo hacemos indicando entre paréntesis 
# cuál es el valor que queremos dar a 'x' en esta ejecución. Estamos haciendo algo similar a una asignación de variables. Solo que el 
# parámetro 'x' es una especie de variable 'local', únicamente va a existir y ser visible dentro de la función. Una función puede recibir 
# parámetros, cada uno del tipo que sea necesario. También puede devolver cualquier tipo de elemento.

# Una función con dos parámetros y que devuelve una lista definida por compresión
def llama_a_la_puerta_de(persona, n_veces):
    """ Llama al a puerta de la persona las veces que haga falta"""
    return ["Toc, toc, toc!" + persona + "!" for i in range (n_veces)]
print (llama_a_la_puerta_de(" Penny", 3))

# Al definir una función, también podemos especificar un valor por defecto para cualquiera de los parámetros. Se indica como si 
# hicieramos una asignación del parámetro en el encabezado. El valor por defecto o por omisión solamente se aplicará si al llamar a la función 
# no incluimos un valor explícito para ese parámetro (omitimos su valor).

# Redefinimos la función con dos parámetros indicando un valor por omisión para 'n_veces'.
def llama_a_la_puerta_de (persona, n_veces = 3):
    """ Llama a la puerta de la persona las veces que haga falta"""
    return ["Toc, toc, toc!" + persona + "!" for i in range (n_veces)]

# Ahora podemos usar la función sin especificar 'n_veces' y tomará el valor por omisión.
llama_a_la_puerta_de(" Penny")

# Si incluimos un valor para el parámetro se ignora el valor por omisión.
print (llama_a_la_puerta_de (" Amy", 1))

# Al definir una función, los parámetros para los que no se especifique un valor por defecto deben ir delante de los parámetros con valor por 
# omisión. Al llamar a una función es obligatorio dar valores para todos los parámetros que no tengan valor por omisión especificado. Por defecto, 
# deben proporcionarse los valores en el mismo orden en el que se han definido los parámetros. No obstante, podemos llamar a una función indicando 
# los valores para cada parámetro por su nombre, como pares 'nombre parámetro = valor'. Haciéndolo así, podemos dar valor a los parámetros en el 
# orden que queremos.

print (llama_a_la_puerta_de (n_veces = 3, persona = "Howard"))

# En el cuerpo de una función se puede llamar otras funciones. Y naturalmente, una función también se puede llamar así misma. Es lo que llama 
# una definición recursiva. Este tipo de contrucciones son habituales en definiciones de series o progresiones matemáticas o para recorrer 
# determinados tipos de estrcturas de datos.

# Tomaremos como ejemplo la sucesión de Fibonacci
# Fib(0) = 0;  Fib (1) = 1; Fib (n) = Fib (n -1) + Fib (n - 2)

# El elemento n-ésimo de la sucesión (para n >= 2) se construye sumando los elementos para (n - 1), Esto es una definición recursiva.

def fibonacci (n):
    """ Calcula el n-ésimo elemento de la serie de Fbonacci"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
print (fibonacci (3))
print (fibonacci (6))

# ¿Cuales son las ventajas de las funciones recursivas? el código es sencillo y fácil de entender. Si quisiéramos hacer lo mismo usando 
# bucles tendríamos que utilizar más variables y almacenar resultado intermedios. Las funciones recursivas encajan muy bien para este 
# tipo de casos.

# Sim embargo también tiene inconvenientes. Suelen consumir mucha más memoria y tiempo de ejecución cuando el número de veces que se tienen
# que llamar a sí mismas es grande. Esto hace que sean más complicadas de depurar si hay algún error. Si no tiene cuidado al programarlas podemos 
# caer en una recursión infinita, de la que no se pueda salir sin un error o una interrupción externa.


## LAMBDA ##

# En ocasiones, necesitamos utilizar una pequeña función para realizar algún cálculo en un punto específico de nuestro programa y nada más. 
# En Python podemos conseguir esto utilizando las funciones anónimas, también llamadas funciones o expresiones 'lambda', por la cláusula
# que se utiliza para definirlas. Una función anónima efectivamente comienza con la palabra lambda (el lugar de 'def como las funciones normales)
# y no tiene un nombre identificador. Puede tener cualquier número de argumentos, pero su cuerpo solamente puede constar de una 
# expresión que devuelva un valor.

# Creamos una función anónima y se la asignamos a la variable 'triple'
triple = lambda x: 3 * x
print (triple(5))

# Después de la palabra clave 'lambda' colocamos todos los parámetros separados por comas. No ponemos paréntesis. Después de la lista de parámetros 
# se ponen dos puntos (:) y seguidamente la expresión que calcula el resultado a devolver. 

# Sin embargo, la verdadera utilidad viene cuando tenemos funciones que pueden recibir otras funciones como parámetros. O funciones que devuelven 
# como resultado otra función. Veamos un ejemplo para entender de qué hablamos.
def genera_multiplicador (n):
    """ Esta función crea y devuelve a su vez una nueva función que multiplicará cualquier valor por n"""
    return lambda x: x * n

# Vamos a generar una nueva función que multiplique su entrada por 2
doble = genera_multiplicador (2)
# La variable 'doble' apunta ahora a una función anónima que devuelve sun entrada multiplicada por 2
print (doble(3))
print (doble(5))

# Ahora vamos a generar una nueva función que multiplique su entrada por 3
triple = genera_multiplicador(3)
# La variable 'triple' apunta ahora a una función anónima que devuelve su entrada multiplicada por 3
print (triple(7))
print (triple(9))

# Empezamos definiendo la función 'genera_multiplicador'. Es una función normal, con su 'def' y que recibe el parámetro 'n'. En lugar de devolver 
# un valor "normal", como habíamos visto hasta ahora, esta función devuelve una expresión 'lambda'. Devuelve otra función. En este caso, devuelve 
# una función 'lambda' que, a su vez, lo que hace es tomar su parámetro 'x' y devolverlo multiplicado por 'n'.

# La función 'genera_multiplicador' sería nuestra maquina configurable (mediante el parámetro 'n') y las funciones anónimas que devuelve serían 
# las herramientas prepraradas para cada paso concreto. Solamente hay una sutiliza más. Si el parámetro 'n' en realidad está definido en la función 
# 'genera_multiplicador' ¿Cómo es que la función 'lambda' se acuerda del valor correcto de 'n' que tiene que utilizar?. En el ejemplo llamamos 
# primero a 'genera_multiplicador' con 'n = 2' y asignamos la función anónima a la variable 'doble'. Después volvemos a llamar a 'genera_multiplicador' 
# con 'n = 3' y asignamos la función anónima devuelta a la variable 'triple'. 

# ¿Por qué la función anónima que hay en 'doble' mantiene el valor 'n = 2' (lo recuerda) y no ha cambiado a 'n = 3'?. En relidad, al devolver la función 
# 'lambda' dentro de 'genera_multiplicador', Python no solo devuelve una función anónima, si no que la empaqueta con un contexto, es decir, con los 
# valores que tenía cada varable visible en ese momento.

# FUNCIONES DE ORDEN SUPERIOR #

# A las funciones que reciben como parámetro otra función, o que devuelven como resultado otra función, se las denomina de 'orden superior'
# Existen algunas funciones de orden superior cuyo uso está tan extendido que ya están dentro del lenguaje. Se trata de 'map', 'filter' y 'reduce'.

# MAP

# La función 'map' sirve para aplicar (o mapear) otra función 'f' (que recibe como parámetro) a todos los elementos de una secuencia o colección.
cuadrados = map (lambda x: x**2, [1,2,3,4,5])
print (list (cuadrados))
# A 'map' le pasamos como primer argumento una función. En este caso, una función anónima usando una expresión 'lambda' (lambda x: x**2) que devuelve 
# su valor de entrada elevado al cuadrado. El segundo argumento de 'map' es una colección de elementos. Aquí le pasamos una lista de números ([1,2,3,4,5]) 
# que queremos elevar al cuadrado. Lo que va a hacer la función 'map' es ir tomand0o uno a uno los valores de la secuencia y ejecutar la función 
# que le hemos pasado como primer argumento con cada uno de estos valores.
# 'map' no devuelve inmediatamente la lista con lso valores resultantes. Lo que devuelve 'map' es un tipo especial de4 objeto que se denomina 'iterador' 
# que es una variante der lso generadores. Este es un objeto que se encarga de hacer cálculos para generar lso valores resultantes uno a uno conforme los 
# necesites y se los vayas pidiendo, iterando sobre la colección de entrada, en lugar de construir la secuencia entera de golpe, lo que permite ahorrar 
# espacio de memoria ya que no tenemos que almacenar los resultados de una vez.

# FILTER

# La función 'filter' sirve para seleccionar (o filtrar) aquellos elementos de una secuencia o colección que cumplen una condición determinada. 
# La condición se le pasa a 'filter' en forma de otra función.
pares = filter(lambda x: x % 2 == 0, [1,2,3,4,5])
print (list(pares))

# A 'filter' le pasamos como primer argumento una función. Le pasamos una función anónima (lambda x: x % 2 == 0) que devuelve verdadero si su valor 
# de entrada es un número par y falso en caso contrario. La función que le pasamos a 'filter' siempre debe devolver valores True y False. El segundo 
# argumento de 'filter' es de nuevo una colección de elementos.
# Lo que va a hacer 'filter' en este caso es ir tomando cada uno de lso valores de la secuencia y ejecutar la función que le pasamos como primer argumento 
# con cada uno de dichos valores, devolviendo solamente los elementos para los que el resultado sea True. En realidad 'filter' devuelte también un objeto 
# de tipo iterador. Por eso utilizamos 'list' al final del ejemplo para obtener una lista de los resultados.

# REDUCE 

# La función 'reduce' sirve para ejecutatr otra función 'f' de forma acumulativa sobre una colección de elementos
import functools
suma = functools.reduce(lambda x,y: x + y, [1,2,3,4,5])
print (suma)

# En la primera línea estamos cargando el módulo 'functools'. Para cargar componentes de una librería de Python utilizamos la palabra reservada 'import'.
# En la segunda línea usamos la función 'reduce' del módulo 'functools'. Si te fijas, el primer argumento de 'reduce es nuevamente una función (Lambda x,y: x + y). 
# El segundo argumento vuelve a ser una colección de valores. La diferencia aquí reside en que la función que le pasemos a 'reduce' debe ser una función que 
# tome dos argumentos y devuelva un solo valor. En este caso, la funcvión anónima recibe dis valores 'x' e 'y' y devuelve la suma de ambos.
# ¿Y qué hace exactamente 'reduce'? Pues empieza tomando los dos primeros elementos de la lista de entrada ([1,2,3,4,5]) y ejecuta la función. Toma 
# el resultado y el siguiente elemento de la lista y vuelve a ejecutar la función. 'reduce' continuar´´´´a con el proceso hasta agotar todos los elementos 
# de la lista. Al terminar, devolverá el resultado final que haya dado la última evaluación de la función.

#  1   2   3   4   5
#  |   |   |   |   |
# (1 + 2)  |   |   |
# (  3  +  3)  |   |
# (      6  +  4)  |
# (         10  +  5) = 15

# UTILIDAD DE LAS FUNCIONES DE ORDEN SUPERIOR

# Las herramientas de orden superior puede nser unas herramientas muy útiles y potentes para ayudar a resolver algunos problemas. No obstante, en buena parte de los 
# casos Python te ofrece formas alternativas de conseguir el mismo resultado de una forma más sencilla y legible. Empecemos con 'map'

# calcular cuadrados usando 'map'
cuadrados = map (lambda x: x**2, [1,2,3,4,5])
print (list(cuadrados))

# calcular cuadrados usando un generador
cuadrados_2 = (x**2 for x in [1,2,3,4,5])

# Si queremos directamente una lista, podemos definirla por comprensión
lista_cuadrados = [ x**2 for x in [1,2,3,4,5]]
print (lista_cuadrados)

# Podemos conseguir el mismo resultado utilizando una expresión de tipo generador con una expresión por comprensión. O si queremos directamente guardar el 
# resultado como una lista, usar una lista por comprensión. Si intentas volver a extraer valores de un generador ya agotado, obtendrás una lista vacía ([]). 
# Esto mismo ocurrirá con el iterador devuelto por 'map'. En cambio, con la lista por comprensión, obtienes una lista y la tienes disponible mientras la necesites. 
# Pasemos al ejemplo con 'filter'.

# extraer los números pares usando 'filter'
pares = filter (lambda x: x % 2 ==0, [1,2,3,4,5])
print (list (pares))

# Hacemos lo mismo usando un generador
pares_2 = (x for x in [1,2,3,4,5] if x % 2 == 0)
print (list(pares_2))

# O si queremos una lista, la definimos por cromprensión
lista_pares = [ x for x in [1,2,3,4,5] if x % 2 == 0]
print (lista_pares)

# Otra vez conseguimos lo mismo utilizando definiciones por comprensión, solo que esta vez añadiendo una cláusula 'if' con la misma condición 
# que en la función de filtrado. Y por último con la función 'reduce'.

import functools
# calcular la suma de elementos usando 'reduce'.
suma = functools.reduce (lambda x,y: x + y, [1,2,3,4,5])
print (suma)

# La forma alternativa de aplicar una función de forma acumulativa es usando un bucle
otra_suma = 0
for x in [1,2,3,4,5]:
    otra_suma = otra_suma + x
print (otra_suma)

# Si queremos aplicar una función a una colección de valores, acumulando o combinando los resultados, la forma general de hacerlo será mediante un bucle. 
# Este tipo e operadores de cálculo acumulado o de reducción a un único valor, son tan comunes que Python proporciona directamente estas funciones.
print (sum ([1,2,3,4,5]))
print (min ([1,2,3,4,5]))
print (max ([1,2,3,4,5]))

# ¿Cuando utilizar 'filter, 'reduce' y 'map'?. Los ejemplos que hemos visto son casos típicos pàra resolverlos utilizando estos generadores o listas 
# por comprensión en Python. Es la solución más extendida. Sin embargo, también habrá casos en los que los cálculos o funciones a aplicar no sean tan 
# simples. Las funciones 'filter, 'reduce' y 'map' no solo aceptan funciones lambda, también aceptan las funciones habituales, siempre que respeten el 
# número de parámetros y el tipo de resultado a devolver. La potencia más grande viene normalmente cuando hay que combinar estas operaciones de filtrado, 
# mapeo y reducción o acumulación. Se trata de un esquema bastante típico en procesamiento de datos, y en el que podemos aplicar las funciones de 'filter, 
# 'reduce' y 'map' de forma encadenada.

# Cuando tengas que decidir entre varias formas de resolver la misma tarea, intenta elegir la solución que simplifique el código aprovechando las herramientas 
# que tienes haciéndolo también fácil de entender. No obstante, en caso de duda y si el tiempo apremia, utiliza la técnica que mejor domines.


### MÓDULOS Y PAQUETES ###

# Conforme empezamos a desarrollar programas con estructuras cada vez más complejas, tenemos la necesidad de poder guardar nuestro código de una forma 
# organizada para poder reutilizarlo. Los módulos son la forma de organizar nuestro código, agrupando definiciones y funcionalidades relacionadas en unidades 
# que podemos cargar y reutilizar en nuestros programas. En Python, cada archivo de código terminado con el sufijo '.py' es un módulo.

# %load U09_src/mimodulo.py
"""" Ejemplo de módulo con definición de funciones y declaración de variables"""

# Definamos funciones del módulo
def fibonacci (n):
    """Calcula el n-ésimo elemento de la serie de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)

def genera_multiplicador(n):
    """ Esta función crea y devuelve a su vez una nueva función que multiplicará cualquier valor por n"""
    return lambda x: x * n
# Declaramos variables del módulo

# Asignamos a esta variable la función multiplicadora por 2
doblar = genera_multiplicador(2)
# Asignamos a esta variable la función multiplicadora por 3
triplicar = genera_multiplicador (3)


## CARGAR MODULOS Y ESPACIOS DE NOMBRES ##

# Para cargar el contenido de un módulo y tener acceso a sus funciones, clases, variables etc. utilizamos el comando 'import' seguido del nombre del módulo.

# Vamos a importar nuestro primer modulo
import U09_src.mimodulo as mimodulo
# Ya podemos utilizar sus fubnciones 
print (mimodulo.fibonacci(10))

# Al hacer el 'import' no ponemos el nombre del fichero completo con su extensión. En Python el nombre del módulo se toma de la primera parte del nombre 
# del fichero sin el '.py'.Una vez que hemos cargado el módulo de esta forma, podemos acceder a su contenido a través del nombre dle módulo, siguiendo 
# con un punto (.) y el nombre de la función o variable que queremos usar.

# ¿Pero por qué tenemos que anteponer el nombre del módulo?. Piensa que en nuestars aplicaciones fácilmente acabaremos teniendo muchos módulos, y es posible 
# que tengamos funciones o variables o cualquier otro objeto con el mismo nombre en distintos módulos ¿Como hacer para que no haya confusión al importarlos 
# y usarlos, cómo hacer que no colisionen? Para eso Python utiliza el concepto de espacios de nombres (o namespaces en inglés). Es un directorio en el que se 
# van anotando los nombres de todos los objetos que vamos creando. No puede haber dos objetos con el mismo nombre dentro de un namespace.

# Cuando iniciamos uan nueva sesión de Pythoin con el itnérprete interactivo, o al ejecutar un programa o script, se crea un nuevo espacio de nombres global 
# asociado a esa sesión. En este espacio de nonmbres se añaden a su vez todos los símbolos, todos los nombres de los objetos predefinidos integrados en el 
# lenguaje. También se añadirán todos los objetos que nosotros vayamos definiendo directamente en la sesión.

# Volviendo a lso módulos, en Python cada uno tiene su propio espacio de nombres, que contiene los identificadores de todos los elementos definidos dentro 
# del módulo. Así que puedes tener dos variables o dos funciones con el mismo nombre en distintos módulos. Cada objeto estará incluido en su namespace 
# correspondiente y no habrá conflictos entre ellos. Al importar un módulo también se le puede asociar un alias, normalmente para abreviar el nombre original del módulo.

# Importamos nuestro módulo, pero con un alias más cortito
import U09_src.mimodulo as m
print (m.fibonacci(5))

# También es posible importar directamente un elemento del módulo deseado a nuestro espacio de nombres actual. La sintaxis en este caso sería:
"From nombre_modulo import nombre_elemento"

# Vamos a importar únicamente la definición de 'doblar' de 'mimodulo' incluyéndola en nuestro espacio de nombres actual
from U09_src.mimodulo import doblar
# Ahopra podemos usar 'doblar' como si la hubiéramos definido en este nivel 
print (doblar (7))

# Esta variante incluye el objeto indicado en nuestro espacio actual, sin añadir el espacio de nombres del módulo ('mimodulo' no estaría definido 
# para acceder a otras funciones). Hay que tener en cuidado al utilizar esta forma de importar elementos, porque puede que ya exista otro objeto 
# con el mismo nombre en nuestro contexto o espacio de nombres actual. Siempre podemos asignar un alias en estos casos.

# Tenemos una versión local de la función 'triplicar'
def triplicar (x):
    """ Función triplicar local"""
    return 3 * x
# Vamos a cargar la versión del módulo, pero con un alias para que no haya conflictos de nombres
from U09_src.mimodulo import triplicar as triple

# podemos usar ambas versiones
print (triplicar(5))
print (triple(5))

# También podemos importar todos los nombres defnidos dentro de un módulo sin utilizar su namespace, auqnue sin poder asignarle un alias. 
# En lugar de la lista de elementos del módulo que queremos importar, utilizamos un asterisco (*).
from U09_src.mimodulo import *

# No obstante, esta última opción es muy desaconsejable, ya que reemplaza todas las definiciones de los nombres ya existentes.


## LOCALIZACIÓN DE LOS MÓDULOS ##

# Cuando le pedimos a Python que importe un módulo, primero tiene que encontrarlo. Para ello sigue una serie de pasos:
# - Comprueba si se trata de uno de los módulos predefinidos incluidos con el lenguaje.
# - Si no existe ningún módulo del lenguaje con ese nombre, busca el fichero con el módulo en el directorio que contiene 
#   el script de Python actual, o el directorio de ejecución de la sesión actual si estamos en modo iterativo. 
# - Si no lo encuentra en el directorio actual, consulta la variable entorno 'PYTHONPATH'. Se trata de uan variable que hay 
#   que definir a nivel de sistema operativo, y donde se puede indicar una lista de directorios donde buscar módulos y librerías instaladas.
# - Por último, busca en el directorio donde esté instalado Python.

# Podemos ver la secuencia de directorios donde buscará de la siguiente forma:
import sys
sys.path

# Cuando desarrollemso nuestros módulos, tendremos que asegurarnos qeu sean accesibles desde el directorio actual o bien añadir los directorios donde 
# se encuentren a la secuencia de búsqueda, bien mediante la variable de entorno 'PYTHONPATH' o bien modificando la variable 'sys.path' dentro del código.


## MÓDULOS EJECUTABLES ##

# Podemos ejecutar un módulo como si fuera un fichero de script normal a tarvés del terminal  

"$ python mimodulo.py"

# Si el módulo únicamente contiene definiciones de variables, funciones, clases etc, lo único que ocurrirá es que se cargarán todas ellas en un 
# nameepace y seguidamente terminará la ejecución. Cuando se lanza la ejecución de un script o un módulo, Python prepara el namespace para la 
# ejecución y le da el nombre especial '_main_'.Si queremos incluir en un módulo un código para que se ejecute solamente cuando lo lancemos como 
# script, podemos consultar cuál es el nombre del namespace actuakl utilizando la variable global '_name_'.

# %load U09_src/mimoduloexec.py
"""Ejemplo de módulo ejecutable"""
# Definición de funciones
def llama_a_la_puerta_de (persona, n_veces = 3):
    """Llama a la puerta de la persona las veces que haga falta"""
    return [ "Toc, toc, toc!" + persona + "!"  for i in range (n_veces)]
# Cuerpo principal ejecutable

# Si estamos dentro del namespace '_main_' ejecutará el código
if __name__ == "__main__":
    print ("Ejecutamos el main")
    print (llama_a_la_puerta_de ("Penny"))
