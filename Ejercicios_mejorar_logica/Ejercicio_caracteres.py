lista = [1,2,3,4,5]
cuadrados = [x**2 for x in lista]
print(cuadrados)

# Crea  una  cadena  de  texto  de  mínimo  10  caracteres  
# e  indica  cuál  es  la posicion correspondiente de cada
# letra y el tamaño de la variable palabra.
palabra = "inteligencia"
print(f' el tamaño de inteligencia es: {len(palabra)}')

# Con esto basicamente lo que hacemos es primero decirle
# a la maquina que queremos buscar la posicion de la secuencia
# y que mire cada elemento de la secuencia, en este caso
# la palabra 'inteligencia'
for i, letra in enumerate(palabra):
    print(f'La letra "{letra}" está en la posición: {i}')


# Utilizando la cadena de texto anterior selecciona una 
# rebanada de cinco caracteres desde una posición en concreto
print(palabra[0:5])

# Utiliza nuevamente la cadena de texto anterior y cuenta 
# las veces que se repite un carácter en la cadena sin utilizar
# la funcion 'count'
palabra = "inteligencia"
contador = 0

for letra in palabra:
    if letra == "i":
        contador = contador + 1

print(f' La letra "i" en inteligencia está {contador} veces')

# Utilizando una nueva cadena de texto divide la cadena 
# tomando el espacio como carácter delimitador 
# sin utilizar split().

autor = "Antonio Picasso"

palabras = []
nombre = ""

for letras in autor:

    if letras != " ":
        nombre += letras

    else:
        if nombre:
            palabras = palabras + [nombre]
            nombre = ""

palabras = palabras + [nombre]

print (palabras)

# Utilizando  la  misma  cadena  de  texto  de  ejercicios  
# anteriores  divide  la cadena tomando el espacio como 
# carácter delimitador.

nombre = (palabras[0])
apellido = (palabras[1])
print(nombre, apellido)

#  Repite  el  ejercicio anterior,  pero  utilizando  
# otro carácter como  delimi-tador.

print (nombre + ", " + apellido)