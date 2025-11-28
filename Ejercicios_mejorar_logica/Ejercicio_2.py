


# -------------------------------------------( EJERCICIO 2 )----------------------------------------------------
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