


# ==============================================================================================================
# --------------( Ejercicio 1)-----------------
# Ordenar una lista de PALABRAS alfabéticamente
# Crea una lista con al menos 10 PALABRAS en desorden.


lista_frutas = ["manzana", "banana", "cereza", "durazno", "uva", "kiwi", "mango", "naranja", "pera", "piña"]
print(lista_frutas)
lista_ordenada = sorted(lista_frutas)
print(lista_ordenada)
lista_reverso = sorted(lista_frutas, reverse = True)
print(lista_reverso)

# Lo que queremos hacer aquí es clasificar lso argumentos de la lista alfabéticamente.
# La función sorted nos permite ordenar cualquier lista y lo hace de la siguiente manera:
# utiliza un algoritmo llamado Timsort, que es una combinación de los algoritmos Merge Sort y Insertion Sort.
# Mira una lista y detecta tramos ya ordenados, los trata como "bloques ordenados y 
# luego lso fusiona en una cadena en el orden correcto"

# También lo que podemso hacer para saber si hay 10 elementos y se puede clasificar es utilizar un condicional 'if' 
# midiendo la longitud de la cadena (en este caso la lista) y ver si hay 10 elementos. Si no tiene, podemos imprimir un mensaje
# indicando que no se puede ordenar porque no tiene 10 elementos.

if len(lista_frutas) == 10:
    print(sorted(lista_frutas))
else:
    print("La lista no tiene 10 elementos")

## DOCUMENTACIÓN UTILIZADA:
# https://docs.python.org/3/howto/sorting.html#sorting-techniques
# https://en.wikipedia.org/wiki/Timsort 



# ==============================================================================================================
# ------( Ejercicio 2 )-------
# Invertir una CADENA de texto


palabra = "murcielago"
inverso = palabra[::-1]
# un slice está formado por tres partes: inicio:fin:paso
# en este caso, estamos diciendo que queremos toda la cadena:
# - Inicio está vacío, lo que significa que queremos empezar desde el principio de la cadena o final si el paso es negativo
# - Fin también está vacío, lo que significa que queremos llegar hasta el final de la cadena y 
# como el paso es negativo, llegamos hasta el principio.
# y además queremos que el paso sea -1, es decir, que vaya de atrás hacia adelante.
# de ahí que cuand ose imprima, nos dé la plaabra pero de forma invertida
print(inverso)

## DOCUMENTACIÓN UTILIZADA:
# https://docs.python.org/3/library/functions.html#slice
# https://stackoverflow.com/questions/5798136/python-reverse-stride-slicing 



# ==============================================================================================================
# ------------------------------( EJERCICIO 3 )------------------------------------------
# # De la comprobación si la lista tiene 10 elementos, además tengo que comprobar que las 
# palabras tengan más de 5 carácteres.


lista_frutas = ["manzana", 
                "banana", 
                "cereza", 
                "durazno", 
                "uva", 
                "kiwi", 
                "mango", 
                "naranja", 
                "pera", 
                "piña"]

# En el bucle 'for' l oque miramos es argumento por argumento la longitud de estos para ver si cumplen la 
# condicion dentro del 'if'. En este caso si las palabras tienen una longitud superior o igual a 5 letras.
# Luego imprimos el resultado para cada iteración del loop.

for fruta in lista_frutas:

    if len(fruta) >= 5:

        print("Frutas con más de 5 caracteres: ", fruta)
    else:
        print("Frutas con menos de 5 caracteres: ", fruta)

# lista por comprension:
# Basicamentes es hacer lo mismo de arriba pero en una linea. Además en este caso lo que 
# queríamos era en vez de imprimir por cada iteracion del loop 'for' el resultado 
# con el condicional 'if' que mide a traves del método len() la longitud de los argumentos 
# y agruparlos en una lista si cumplen o no el requisito del 'if'.
# La sintaxis es: -->  [expresión for elemento in iterable (lista_frutas) if condición]

lista_5 = [fruta for fruta in lista_frutas if len(fruta) >= 5]
print ("Frutas con más de 5 caracteres: ", lista_5)

lista_menos_5 = [fruta for fruta in lista_frutas if len(fruta) < 5]
print("Frutas con menos de 5 caracteres: ", lista_menos_5)

## DOCUMENTACIÓN UTILIZADA:
# https://www.geeksforgeeks.org/python/python-filter-list-of-strings-based-on-the-substring-list/ 



# ==============================================================================================================
# -------------------------------------------( EJERCICIO 4 )----------------------------------------------------
# Hacer el algoritmo por mi mismo timsort sin SORTED y sin APPEND, o sea también tendré que hacer APPEND por mi mismo. 
# Tendré que investigar ordenado de la 'pila'.

import random

def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()

# Lo primero de todo generamos una lis. En este caso, como queremos que siempre que se realice
# una clasificacion de los valores dentro de una caja queremos que sea ascendente, ponemos
# un poco de dificultad no sabiendo desde el principio cuales son los valores a ordenar.
# por eso utilizamos la librería 'random'. Una vez generados los valores, los guardamos en una variable,
# en este caso 'caja'.

tamaño = (len(caja))            # 'size' o tamaño de la lista

# La 'posicion' no es un valor dentro de la secuencia, 
# si no donde está ese valor dentro del índice que tiene la secuencia o lista.
# En este ejemplo, veremos cual es la última posición de la secuencia.
# No nos dará el valor dentro de la posicion, si no la última posición en sí.

ultima_posicion_caja = len(caja) - 1      # 'posicion' de un elemento en una lista

# Si de forma espefícica necesitamos el valor que se encuentra dentro de la ultima posicion, 
# entonces si que lo buscaremos de forma específica, dando el último valor 
# de la secuencia y no la ultima posicion.

ultimo_caja = caja [-1]       # Da el ultimo 'valor' de la ultima 'posicion' de la lista o el array

# En este ejercicio, necesitamos entender el concepto de 'pila'. La pila en programación se llama LIFO
# (Last-in, last-out) por lo que siempre jugaremos con la última posición o valor de la secuencia.
# Para ello, crearemos una lista vacía para poder rellenarla de los valores de la primera lista,
# en este caso se llama 'caja', y poder ordenarlos de forma ascendente: 1, 2, 3, 4, 5... n
caja_2 = [ ]

# El primer 'while' mira una condición que es fundamental para que podamos clasificar los valores dentro de la secuencia.
# Mira que la lista 'caja' no esté vacía. Solo se realizará si hay elementos dentro de la lista. Cuando no haya ninguno, el bucle 
# parará y podremos ver si la clasificación se ha hecho de forma correcta.
# La función que necesitamos utilizar es pop. Elimina el elemento en la posición dada en la lista y lo devuelve. 
# Si no se especifica ningún índice, lista.pop() elimina y devuelve el último elemento de la lista. 
# Genera un IndexError si la lista está vacía o el índice está fuera del rango de la lista.
# La utilización de esta función es crucial para el uso de la pila. Necesitamos jugar con la última posicion para poder ordenar.
while caja:
    pila_1 = caja.pop()

# Una vez dentro del primer bucle, luego entraremos en un bucle interno 'while' que nos ayudará a ver:
# Si 'caja_2' no está vacía y el último valor de la 'caja_2' es mayor que el valor que está dentro dentro de la 'pila_1',
# podremos añadir el valor que habiamos sacado de 'caja' y lo habíamos guardado en 'pila_1' dentro de la 'caja_2'.
# Es importante tener el cuenta el valor y no la posición porque no queremos cambiar solo las posiciones de los elementos, 
# si no compararlos para poder ordenarlos de forma ascendente.

    while caja_2 and caja_2 [-1] > pila_1:

# Lo curioso de este bucle es que la condicion en la primera vuelta no se cumple ya que no hay nada en 'caja_2', 
# nos da 'False'. Al acabar el bucle interno lo que si que ocurre es que a 'caja_2' se le añade el valor 
# que estaba en la 'pila_1'. Ahora el bucle interno si que puede funcionar. Sacamos la ultima posicion de 'caja' y lo 
# guardamos en 'pila_1'. entramos en el bucle interno. Miramos si el valor del ultimo elemento de 'caja_2' es mayor que 
# el valor de 'pila_1'. Si se cumple, se quita el último elemento de 'caja_2', se añade a 'caja'.
# Al acabarse el bucle interno, añadimos el elemento guardado en 'pila_1' a 'caja_2'. ¿qué ha ocurrido en verdad?
# se han comparado dos valores: el que estaba en caja_2 y el que estaba en pila_1. Como el valor de caja_2 era mayor 
# que el de pila_1, se quita, se añade a caja y se añade el elemento de pila_1 ya que era más pequeño que el elemento 
# que hemos quitado de caja_2. El elemento que hemos puesto al final de caja será el siguiente 
# en filtrarse gracias al método LIFO. Por lo tanto, los elementos que entren en caja_2 se compararán uno a uno 
# con el valor guardado en pila_1 extraido de caja, hasta ordenarse de forma ascendete y dejando vacio caja.

        pila_2 = caja_2.pop()
        caja = caja + [pila_2]

    caja_2 = caja_2 + [pila_1]

# Al final, cuando los dos bucles acaben, imprimaremos la lista ordenada

print(caja_2)

## DOCUMENTACIÓN UTILIZADA:
# https://stackoverflow.com/questions/930397/how-do-i-get-the-last-element-of-a-list
# https://www.geeksforgeeks.org/python/stack-in-python/



# ==============================================================================================================
# -------------------------------------------( EJERCICIO 5 )----------------------------------------------------
# Invertir la palabra "murcielago" de forma manual "fuck puto manu"



# Ejercicio extra: Un programa que lanza hechizos y que haga la combinacion de 2 palabras



# Ejercicio 6: "Adivina la palabra"
# Crea un programa que pida al usuario que adivine una palabra secreta y que vaya imprimiendo als 
# letras que ha adivinado hasta completarla.
# la condicion en vez que sea TRUE tiene que mirar 'while' si las palabras adivinadas son todas las que coninciden con la palabra secreta
# T0DO LO QUE SEA 'if' o bucles lo separo por lineas y nada de anidaciones.

palabra_secreta = "python"
letras_adivinadas = ['_'] * len(palabra_secreta)

while True:

    letra = input("Adivina una letra: ").lower()

    if letra in palabra_secreta:
        if letra not in letras_adivinadas:
            letras_adivinadas.append(letra)

    print(letras_adivinadas)