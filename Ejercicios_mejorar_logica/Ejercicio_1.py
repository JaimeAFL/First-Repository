


# -------------------------------------------( EJERCICIO 1 )----------------------------------------------------
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

lista_frutas = ["manzana", "banana", "cereza", "durazno", "uva", "kiwi", "mango", "naranja", "piña"]

if len(lista_frutas) == 10:
    print(sorted(lista_frutas))
else:
    print("La lista no tiene 10 elementos")

## DOCUMENTACIÓN UTILIZADA:
# https://docs.python.org/3/howto/sorting.html#sorting-techniques
# https://en.wikipedia.org/wiki/Timsort 
