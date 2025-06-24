
#### TIPOS COMPUESTOS DE DATOS ####


### LISTAS ###

# Creamos una lista vacía usando un par de corchetes sin ningún elemento dentro.
lista_vacia = []

# Podemos crear una lista con números.
lista_nums = [1, 6, 2, 5, 3, 4]

# o una lista con cadenas de texto.
lista_frutas = ["pera", "manzana", "ciruela", "cereza"]

# Incluso podemos meter una lista como elemento de otra lista.
listas_anidadas = ["Aquí hay", ["listas", "anidadas"], [1 , 2]]

# Si te has fijado, la última lista tiene listas anidadas como elementos.
# ¿Cuántos elementos dirías que hay en la lista superior?
# Podemos utilizar los bucles para comprobarlo.
for elemento in listas_anidadas:
    print (elemento)


# POSICIÓN EN UNA LISTA #

# Para acceder a los elementos de una lista por su índice o posición,
# ponemos el índice entre corchetes también. El primer elemento de una lista
# (y de cualquier secuencia) tiene el índice cero. Así que si una lista
# tiene N elementos, para acceder al último tendremos que usar el índice (N - 1).

# Longitud de la lista.
len(lista_nums)
print (len(lista_nums))

# Longitud de la lista anidada: cada "sublista" interna es vista como único elemento.
len(listas_anidadas)
print (len(listas_anidadas))

# Seleccionar un elemento: el primer valor lo obtenemos con el índice 0.
print (lista_nums[0])

# El elemento para el índice 5.
print (lista_nums[5])

# El último elemento está en "len - 1".
print (lista_nums[-1])

# Devuelve el primer elemento de la lista.
print (lista_nums[-6])


# REBANADA #

# Indicamos el índice o la posición inicial desde donde empezamos la selección y la posición
# final hasta donde queremos llegar, escribiéndolos dentro de los corchetes separados por
# dos puntos ":". El elemento correspondiente al límite inicial siempre se incluye, pero
# el elemento en él limite final queda excluido.

# Seleccionamos una "rebanada" con los dos primeros elementos.
letras =  ["A", "B", "C", "D", "E", "F"]
print ("Lista entera:", letras)
print ("Dos primeros elementos:", letras[0:2])
print ("Elementos intermedios:", letras[2:5])

# Si no especificamos el segundo índice, seleccionamos hasta el final de la lista.
print ("Final de la lista:", letras[2:])

# Y si no especificamos el primer índice, seleccionamos desde el principio.
print ("Seleccionamos desde el principio:", letras[:4])

# También podemos usar la notación de índices negativos. Seleccionamos desde
# la penultima posición (incluida) hasta el final.
print("Indice negativo. De la penultima hasta el final:", letras[-2:])

# Seleccionamos desde el inicio hasta la penúltima posición (excluida).
print("Desde el inicio hasta la penúltima posición (excluida):", letras[:-2])

# Como el primer índice siempre se incluye y el segundo siempre se excluye,
# podemos reconstruir la lista.
print ("Reconstruimos la lista: letras[:2] + letras[2:]:", letras[:2] + letras[2:])

# Las listas sí son MUTABLES, es decir, sí podemos modificar
# el contenido de los elementos de una lista.
print(lista_frutas)

# Modificamos un elemento individual, en este caso el elemento "manzanas".
lista_frutas[1] = "uva"
print("Sustituimos 'manzanas' por 'uvas':", lista_frutas)

# También podemos sustituir los elementos de una rebanada
lista_frutas[2:] = ["naranja", "aguacate"]
print("Sustituimos los elementos de una rebanada:", lista_frutas)

# O eliminar valores reemplazando con la lista vacía.
lista_frutas[1:3] = []
print("Eliminamos valores con una lista vacía", lista_frutas)

# O vaciarla entera.
lista_frutas[:] = []
print("Hemos vaciado la lista:", lista_frutas)


# CONCATENAR Y REPLICAR LISTAS #

# Concatenamos listas.
lista_1 = ['a', 'b', 'c']
lista_2 = ['100', '200', '300']
print("listas a concatenar: lista_1 = ['a', 'b', 'c'] y lista_2 = ['100', '200', '300']")
print("concatenación de listas:", lista_1 + lista_2)

# Replicar la lista.
print("replicar lista:", 3 * lista_1)

# Podemos extraer los elementos de una lista y asignarlos a distintas variables
# Si nos fijamos, las variables siguen el orden de los elementos de la lista
# o dicho de otro modo: el orden de la posición de los elementos se asigna al
# orden de las variables (o argumentos) de manera secuencial.
x, y, z = lista_2

print("variables y lista: x, y, z = lista_2")
print(x)
print(y)
print(z)


# CONSULTA Y MODIFICACIÓN DE LISTAS #

# Añadir un elemento al fina lde la lista.
lista_1.append('d')
print(lista_1)

#extraer el último elemento de la lista.
ultimo_valor = lista_1.pop()
print(ultimo_valor)
print(lista_1)

# Insertar un elemento dentro de una posición concreta.
# Inserta 'e' dentro de una posición concreta (al principio).

lista_1.insert(0, "e")
lista_1.insert(2, "c")
print (lista_1)

# Busca en qué posición está un elemento (si no existe dará error).
print(lista_1.index("b"))

# contar el número de veces que aparece un elemento.
print(lista_1.count("c"))

# Borrar el primer elemento de la lista que coincida con el valor dado. Dicho de otro modo,
# buscará de izquierda a derecha hasta encontrar coincidencia y eliminar la coincidencia.
lista_1.remove("c")
print(lista_1)

# Ordena los valores de la lista dependiendo del tipo: alfabéticamente, numéricamente...
lista_1.sort()
print(lista_1)

# Invierte el orden de los elementos de la lista.
lista_1.reverse()
print(lista_1)

# Borrar un elemento indicando la posición.
del lista_1[2]
print(lista_1)

# Limpiar todos los elementos de la lista.
lista_1.clear()
print(lista_1)


# VARIABLES, LISTAS Y MUTABILIDAD #

# Tienes una variable, lists1, y la inicializamos con unos valores. Más adelante, tal vez tras hacer
# varios calculos y operaciones con la primera variable, necesitas crear otra nueva variable, lista2,
# e inicializarla con la misma lista que tenga la primera en ese momento. Así que le asignas
# la primera variable a la última.

# Creamos e inicializamos la primera variable.
lista1 = [1, 2, 3]

# Y ahora necesitamos crear una nueva variable e inicializarla con la misma lista que tenta lista1.
lista2 = lista1
print(lista2)

# Obviamente, ahora tienen el mismo valor.
print(lista1 == lista2)

# Tras la asignación ambas variables tienen el mismo valor, aunque en realidad ambas variables apuntan al
# mismo contenido. Una variable de Python no deja de ser eso, un nombre o referencia a un valor o
# estructura de datos que está almacenada de algún modo en la memoria. La operación de asignación de una
# variable a otra no copia el contenido, sino que define un nuevo nombre o referencia al mismo
# contenido que la variable original. Podemos ver qu dos variables representan el mismo objeto con el operador 'is'
# Como ambas variables no son más que nombres o referencias para la misma lista en memoria,
# la primera variable mostrará también el nuevo valor.

# Comprobamos que las dos variables representan el mismo objeto.
print(lista2 is lista1)

# Modificamos lista2 sustituyendo el valor del índice 2.
# Y vemos que lista 1 nos devuelve el mismo contenido modificado.
lista2[1] = 99
print(lista1)

# No obstante, si en lugar de modificar el valor de lso elementos de la lista, asignamos una lista distinta,
# estaremos definiendo un nuevo objeto o estructura de datos. La variable usada pasará a nombrar ese nuevo objeto
# independiente; las dos variables ya no serán referencias del mismo contenido.

# Si asignamos una nueva lista a la segunda variable, dejan de referenciar al mismo contenido
lista2 = [7,8,9]
print(lista2 is lista1)

# Incluso aunque usemos la primera variable en la expresión para definir
# la segunda, las estructuras de datos que referencian son distintas
lista2 = 2 * lista1
print(lista2 is lista1)

# A la hora de trabajar con estructuras de datos mutables (como son las listas), deberás tener
# to-do esto en cuenta para evitar modificar accidentalmente el contenido de una variable al manipular una segunda.
# Si necesitas una copia idéntica, pero independiente de una lista, puedes usar el méto-do copy()
lista1 = [1, 2, 3]

# Con copy() creas una nueva lista, copia exacta de la original, pero independiente
lista2 = lista1.copy()

# Los valores de las listas son iguales
print(lista2 == lista1)

#Peor en el fondo, ya no son lo mismo
print(lista2 is lista1)


### TUPLAS ###

# Las tuplas son una secuencia de elementos ordenados, similares a las listas. Las diferencias principales son dos:
# - Desde un punto de vista sintáctico, se definen usando paréntesis en vez de corchetes como en las listas.
# - Desde el punto de vista semántico, las tuplas SON INMUTABLES.
# Una vez que has creado una tupla definiendo sus elementos, ya no puedes modificar los valores que contiene.

# Construimos las tuplas poniendo sus elementos separados por comas entre paréntesis
palos_baraja = ("corazones", "diamantes", "tréboles", "picas")
valores_baraja = ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
as_de_picas = (valores_baraja[0], palos_baraja[3])
reina_de_corazones = (valores_baraja[11], palos_baraja[0])

# Podemos usar tuplas como elementos anidados dentro de otra tupla
mano = (as_de_picas, reina_de_corazones)
print(mano)
print(mano[0])
print(mano[1])

# También podemos utilizar listas como elementos, cualquier objeto en realidad
jugador = ("jugador_1", [as_de_picas, reina_de_corazones])
print(jugador)

# Si tratas de modificar la tupla, obtendrás un error

# todo mano[0] = ('J', "corazones"):

# todo Traceback (most recent call last):
  # todo File "C:\Users\ujcr3a\PycharmProjects\PythonProject\Listas_tuplas.py", line 258, in <module>
    # todo mano[0] = ('J', "corazones")
    # todo ~~~~^^^
# todo TypeError: 'tuple' object does not support item assignment

# En realidad Python nos permite definir una tupla sin usar paréntesis al crearla,
# poniendo simplemente elementos separados por comas

#tupla definida por enumeración, sin usar paréntesis
otra_tupla = 'uno', 'dos', 3
print(otra_tupla)

# Te recomendamos siempre utilizar paréntesis. Cuando uses tuplas anidados o expresiones
# más complejas para definir elementos, vas a necesitar incluir los paréntesis obligatoriamente.
# Hay dos casos especiales de creación de tuplas
# - tupla vacía
# - tupla de un solo elemento

# Las tuplas vacías créan con una pareja de paréntesis vacía, sin ningún elemento dentro
# Para crear una tupla de un único elemento es necesario añadir una coma justo detrás del elemento
# y antes del cierre de paréntesis. Parece raro, pero como los paréntesis también sirven para 'encapsular'
# una expresión "3*4", Python necesita una pista para distinguir si queremos construir
# una tupla con un solo valor o no.

# Creamos la tupla vacía con una pareja de paréntesis vacía, sin ningún elemento
tupla_vacia = ()
print(tupla_vacia)

# Creamos una tupla con un solo elemento
tupla_un_elemento = (1,)
print(tupla_un_elemento)


## CONJUNTOS ##

# Ya has aprendido que en Python tenemos los tipos tupla, lista y cadena de texto que son tipos
# secuenciales, es decir son colecciones ordenadas de elementos. El tipo no ordenado más básico
# es el conjunto o set en Python. Un conjunto es una colección no ordenada de elementos y donde
# además no puede haber elementos repetidos. Un conjunto sí es modificable. Podemos eliminar o
# añadir nuevos elementos siempre que no estén ya incluidos en el conjunto. La utilidad de este
# tipo viene justamente cuando necesitamos controlar elementos duplicados o saber si un elemento
# ha sido incluido (pertenece) a un conjunto, sin importarnos la posición.

# Para crear un conjunto escribimos los elementos entre un par de llaves y separados por comas.
# Si queremos crear un conjunto vacío utilizaremos la función set() y no un par de llaves vacías
# ({}) un par de llaves vacías créan un diccionario vacío.

# Vamos a controlar qué objetos añadimos en nuestra mochila para una excursión
# Creamos un conjunto vacío (solo por probar, para este ejemplo no nos haría falta)
# todo en_mochila = set()

# 'inicializamos': incluimos varios objetos
en_mochila = {"bocadillo", "agua","linterna", "agua", "cuerda"}

# Si imprimimos, veremos que el "agua" no aparece duplicada - ya sabemos que tenemos agua
print(en_mochila)

# Anotamos que metemos un cuchillo
en_mochila.add("cuchillo")
print(en_mochila)

# para comprobar si un elemento está en el conjunto usamos 'in'.
print("bocadillo" in en_mochila)
print("cerillas" not in en_mochila)

# También podemos quitar un elemento del conjunto
en_mochila.discard("cuerda")
print(en_mochila)


# OPERADORES EN CONJUNTOS #

# También disponemos de las operaciones habituales entre conjuntos: unión, diferencia, intersección...
# Unión de a y b
a = {1, 2, 3, 5, 8}
b = {1, 2, 4, 8, 16}
print(a.union(b))

# También podemos hacerlo así: elementos que están en a o en b
print(a | b )

# Intersección de a y b
print(a.intersection(b))

# También podemos hacerlo así: elementos que están en a y en b
print(a & b)

# Diferencia entre a y b
print(a.difference(b))

# También podemos hacerlo así: elementos que están en 'a' pero no en 'b'
print(a - b)

#diferencia simétrica o excluyente entre a y b
print(a.symmetric_difference(b))

# También podemos hacerlo así: elementos que están exclusivamente bien en la 'a'
# o bien en 'b' (pero no en ambos)
print(a ^ b)

# ¿'s' es un subconjunto de 'a'?
s = {1, 2}
print(s.issubset(a))

# ¿Todos los elementos de 's' están en'a'?
print(s <=a)

# ¿'a' es un superconjunto de 's'?
print(a.issuperset(s))

# ¿'a' incluye todos los elementos que están en 's'?
print(a >= s)


## DICCIONARIOS ##

# Los diccionarios son otro de lso tipos de datos compuestos más útiles que Python proporciona
# de forma nativa. La principal característica de lso diccionarios es que almacenan parejas de
# elementos formadas por una clave o elemento identificador y el valor que queremos asociarle.
# Los diccionarios no son un tipo ordenado de datos (o no tienen por qué serlo). Lo importante
# en un diccionario es poder añadir una clave y su valor asociado, para que luego buscar por la
# clave para obtener su valor sea una operación rápida y eficiente. Python gestiona y organiza
# internamente las claves para optimizar el funcionamiento.

# Las claves no tienen por qué estar en el orden que tú pensarías después de añadir datos nuevos.
# Deben ser únicas, no puede haber claves repetidas. Además, una clave tiene que estar formada
# por un elemento 'inmutable', no puede cambiar una vez que se ha añadido junto con su valor al
# diccionario. Por ejemplo, una cadena mde texto, un número o un tupla pueden usarse como claves.
# Pero una lista no, porque es posible modificar los elementos de la lista a posteriori.

# Para crear un diccionario inicialmente vacío utilizamos una pareja de claves '{}'. Si quieres
# añadir elementos en la propia inicialización, solo tienes que poner parejas 'clave : valor'
# separadas por comas dentro de las llaves. Fíjate que separamos la clave de su valor utilizando
# dos puntos (:). Para acceder a un valor, utilizamos los corchetes como haríamos en una lista o
# una tupla, solo que en este caso indicamos la clave y no un índice de posición.

# Si queremos crear un diccionario vacío, usamos una pareja de llaves
libreta_telefonos1 = {}

# También podemos incluir elementos en la inicialización poniendo pares 'clave : valor'
libreta_telefonos = {"Carlos": 5556045, "Luis": 5556048, "Javier": 5556051}

# Para acceder a un valor, utilizamos la clave entre corchetes
print(libreta_telefonos["Luis"])

# Podemos añadir una nueva clave y asignarle un valor
libreta_telefonos["Daniel"] = 5556056

# Además si asignamos un valor a una clave existente, reemplazaremos el valor antiguo
libreta_telefonos["Carlos"] = 5556033
print(libreta_telefonos)

# Podemos comprobar si una clave está en el diccionario
print("Luis" in libreta_telefonos)

# Y podemos eliminar una pareja "clave valor" indicando la clave
del libreta_telefonos["Luis"]
print(libreta_telefonos)

# Tenemos distintas formas de iterar un diccionario. Podemos iterar sobre las claves del
# diccionario de forma directa. También podemos iterar sobre las parejas (clave, valor).

# Podemos iterar directamente sobre las claves de un diccionario así
for nombre in libreta_telefonos:
    print(nombre, "=", libreta_telefonos[nombre])

# O podemos iterar sobre las parejas 'clave, valor'
# todo for nombre, telefono in libreta_telefonos:
    # todo print(nombre, "=", telefono)

# Y si lo que queremos es iterar solo los valores, podemos hacerlo de la siguiente manera:
for telefono in libreta_telefonos.values():
    print(telefono)


## DEFINICIONES POR COMPRENSIÓN ##

# Las definiciones por comprensión son una forma muy concisa y simple de generar colecciones
# de datos de forma automática. Se utilizan sobre to-do con listas, pero son aplicables a todos
# los tipos compuestos haciendo los debidos ajustes. En inglés aparecen como 'list comprehensions'
# y en español listas de comprensión o también comprensión de listas. Son expresiones que permiten
# construir una nueva colección definiéndoles a partir de otra colección de partida, una expresión
# generadora de los nuevos elementos a incluir y un predicado o condición.

# Imagina que queremos guardar en una lista la tabla de multiplicar del 7. Una forma de hacerlo,
# con lo que hemos aprendido hasta ahora, es mediante un bucle.

# Preparamos una lista vacía para ir poniendo los resultados
tabla_7 = []

# Iteramos los números del 0 al 9 y añadimos el valor de la tabla de multiplicar del 7.
for x in range(0, 10):
    tabla_7.append(7 * x)
print(tabla_7)

# Hemos tenido que crear una variable con una lista vacía al principio y después utilizar
# el bucle 'for' para iterar por lso valores de 0 a 9 e ir modificando en cada paso la lista
# para añadir cada valor de la tabla de multiplicar.

# No es que sea un código muy complicado ni largo. Pero Python nos permite hacer esto
# de forma más sencilla y breve.
tabla_7 = [7 * x for x in range(0, 10)]
print(tabla_7)

# Para empezar, la expresión está entre corchetes. Esto indica que vamos a construir una lista,
# rellenándola con los elementos que genere la expresión. Enseguida te contamos como hacer
# para crear un conjunto, tupla o un diccionario.

# La primera parte (7 * x) es la expresión que genera los nuevos elementos a partir de los valores
# que tome 'x' mientras que la expresión 'for' nos dice cuál es el dominio de valores de entrada
# que va a tomar 'x' (En este caso una secuencia de 0 hasta 9). Podemos ampliar la definición
# incorporando una o más condiciones con una cláusula 'if'. Supongamos que queremos guardar los valores
# de la tabla de multiplicar del 7 solo cuando el factor multiplicador es un número par.

# Usamos un 'if' para comprobar x es par (utilizando el o módulo o resto)
tabla_7_pares = [7 * x for x in range (0, 10) if x % 2 == 0]
print(tabla_7_pares)

# Como ves en el ejemplo, simplemente hemos añadido la cláusula 'if x % 2 == 0' al final
# de la construcción. Para cada valor de 'x' en el rango específicado (de 0 a 9), se comprueba
# si se cumple la condición ('x % 2 == 0', es decir, el resto de dividir 'x' por 2 sea 0
# luego que 'x' sea par). Si se cumple el predicado, entonces se genera un nuevo valor (7 * x)
# para la lista; y si no ese valor de 'x' se descarta.

# El dominio de valores de entrada puede ser cualquier objeto o expresión iterable.
lista_frutas = ["pera", "manzana", "ciruela", "cereza"]
resultado = [fruta.upper() for fruta in lista_frutas if fruta.startswith("c")]
print(resultado)

# Podemos combinar dos o más cláusulas 'for' con sus dominios de entrada para construir la colección.
[print(x * y) for x in (1, 2, 3) for y in (4, 5, 6)]

# Esta expresión se evalúa para todas las combinaciones de valores de 'x' e 'y'. Si lo piensas, es
# como si tuvieras dos bucles 'f' anidados. Vamos a incluir en cada elemento generado los valores
# 'x' e 'y' así quedará más claro.
[print (x, y, x * y) for x in (1, 2, 3) for y in (4, 5, 6)]

# En este caso hemos hecho que la expresión generadora devuelva una tupla con lso valores de
# 'x', 'y' y de 'x * y'. Puede utilizarse cualquier expresión, to-do lo compleja que se
# necesite, siempre que devuelva un elemento válido. Si en lugar de generar una lista
# queremos construir un conjunto, solamente tenemos que reemplazar los corchetes por la
# función set () y paréntesis.
print (set((x for x in range(10) if x % 2 != 0)))

# Si queremos un tupla, no será suficiente con utilizar paréntesis.
# Tendremos que utilizar el constructo 'tuple()'.
print (tuple(x for x in range (5)))

# Y para construir un diccionario utilizando el mecanismo de comprensión, además de utilizar
# llaves en lugar de corchetes, la expresión generadora deberá tener forma de 'clave : valor'.

# Aquí la clave es el factor multiplicador, y el valor es el resultado de la multiplicación
dict_tabla_7 = {num : 7 * num for num in range (0, 10)}
print (dict_tabla_7[3])


## GENERADORES ##

# Un generador es un objeto que se encarga de hacer cálculos para generar los valores
# resultantes uno a uno conforme los necesitemos y los vayamos pidiendo, iterando sobre
# la colección de entrada, en lugar de construir la secuencia entera de golpe. La utilidad
# de este mecanismo es que así se ahorra espacio de memoria (no tenemos que almacenar todos
# los resultados) y resulta más eficiente en los casos en los casos en los que no necesitamos
# la secuencia completa de una vez, por si queremos iterar los valores en un bucle.

# Construimos un generador para la tabla de multiplicar del 7
gen_tabla_7 = ( 7 * x for x in range (0, 10))
print(gen_tabla_7)

# No veremos una secuencia, sino un mensaje indicando que es un objeto de tipo 'generado'.

# Vamos a usarlo en un bucle. El generador va devolviendo un nuevo valor cada vez
# que se le pide hasta que agota todos los valores de su dominio de entrada.
for v in gen_tabla_7:
    print(v)

# Si tenemos un generador y queremos extraer sus valores a una lista
# podemos utilizar el constructo 'list'.

gen_tabla_3 = ( 3 * x for x in range (0, 10))
lista_tabla_3 = list(gen_tabla_3)
print(lista_tabla_3)

# Fíjate que si intentas volver a utilizar el generador después de haber iterado todos
# los elementos (en un bucle o al extraerlos a una lista), no obtendrás nada, excepto
# posiblemente un error. El generador ha quedado vacío, está agotado y no tiene
# valores para devolver.

otra_lista_tabla_3 = list(gen_tabla_3)
print(otra_lista_tabla_3)
