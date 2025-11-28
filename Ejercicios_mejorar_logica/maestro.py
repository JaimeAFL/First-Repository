


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
# Hacer el algoritmo por mi mismo timsort sin SORTED y sin APPEND, o sea también tendré que hacer APPEND por mi mismo. Tendré que investigar ordenado de la 'pila'.



# EJERCICIO 5: Invertir la palabra "murcielago" de forma manual "fuck puto manu"



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