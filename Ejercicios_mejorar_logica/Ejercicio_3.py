


# -------------------------------------------( EJERCICIO 3 )----------------------------------------------------
# De la comprobación si la lista tiene 10 elementos, además tengo que comprobar que las 
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