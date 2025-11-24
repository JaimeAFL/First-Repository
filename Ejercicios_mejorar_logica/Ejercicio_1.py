# Ejercicio 1: Ordenar una lista de PALABRAS alfabéticamente
# Crea una lista con al menos 10 PALABRAS en desorden.

lista_frutas = ["manzana", "banana", "cereza", "durazno", "uva", "kiwi", "mango", "naranja", "pera", "piña"]
print(sorted(lista_frutas))
# Lo que queremos hacer aquí es clasificar lso argumentos de la lista alfabéticamente.
# La función sorted nos permite ordenar cualquier lista y lo hace de la siguiente manera:
# utiliza un algoritmo llamado Timsort, que es una combinación de los algoritmos Merge Sort y Insertion Sort.
# Mira una lista y detecta tramos ya ordenados, los trata como "bloques ordenados y 
# luego lso fusiona en una cadena en el orden correcto"

# También lo que podemso hacer para saber si hay 10 elementos y se puede clasificar es utilizar un condicional 'if' 
# midiendo la longitud de la cadena (en este caso la lista) y ver si hay 10 elementos. Si no tiene, podemos imprimir un mensaje
# indicando que no se puede ordenar porque no tiene 10 elementos.
lista_frutas = ["manzana", "banana", "cereza", "durazno", "uva", "kiwi", "mango", "naranja", "pera"]
if len(lista_frutas) == 10:
    print(sorted(lista_frutas))
else:
    print("La lista no tiene 10 elementos")

## DOCUMENTACIÓN UTILIZADA:
# https://docs.python.org/3/howto/sorting.html#sorting-techniques
# https://en.wikipedia.org/wiki/Timsort 

# Ejercicio 2: Invertir una CADENA de texto
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

# Ejercicio 3: "Adivina la palabra"
# Crea un programa que pida al usuario que adivine una palabra secreta y que vaya imprimiendo als 
# letras que ha adivinado hasta completarla.

palabra_secreta = "python"
letras_adivinadas = ['_'] * len(palabra_secreta)

while True:

    letra = input("Adivina una letra: ").lower()

    if letra in palabra_secreta and not letras_adivinadas:
        letras_adivinadas.append(letra)
    