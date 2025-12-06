

# -------------------------------------------( EJERCICIO 4 )----------------------------------------------------
# Hacer el algoritmo por mi mismo timsort sin SORTED y sin APPEND, o sea 
# también tendré que hacer APPEND por mi mismo. Tendré que investigar ordenado de la 'pila'.
import random

def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()
print(caja)

def cambio_colocacion(caja):
    print(caja)
    auxiliar = caja(0)
    for i in range(len(caja)):
        if i > caja:






<<<<<<< HEAD
import random

def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()
tamaño = (len(caja))            # 'size' o tamaño de la lista
posición_c = len(caja) - 1      # 'posicion' de un elemento en una lista
ultimo_caja = caja [ -1 ]       #  Da el ultimo 'valor' de la ultima 'posicion' de la lista o el array


caja_2 = [ ]
tamaño_c2 = len(caja_2)
posición_c2 = len(caja_2) - 1   
ultimo_caja2 = caja_2 [ -1 ]


while caja:

    for elemento in caja:
        cambio_elemento = caja.pop()
        caja_2 = caja_2 + [cambio_elemento]

        for elemento_c2 in range (tamaño_c2):
            if elemento_c2 > posición_c2:
                caja_2 = caja_2 + [elemento_c2]

print(caja_2)







def cambio_colocacion(caja):
    print(caja)
    auxiliar = caja(0)
    for i in range(len(caja)):
        if i > caja:
            break



caja = [10, 3, 50, 56, 42, 24, 4, 112, 69, 54, 12, 30, 79, 80]
=======
>>>>>>> refs/remotes/origin/main



# tengo que cambiar lo que hay dentro de la caja, buscar su posicion
# y truco, utilizar 'str' para volver los valores en strings

lista_caja1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]

auxiliar1 = str(lista_caja1)


def cambio_posicion (lista, a, b, c):
    
    memoria = lista [a]
    lista [a] = lista [b]
    lista [b] = lista [c]
    lista [c] = memoria
    return lista


for a in lista_caja1:

    for a in caja:

<<<<<<< HEAD
        for b in caja:
            a = a > b

            for c in caja:
                b = b > c
=======
    for b in caja:
        a = a > b

        for c in caja:
            b = b > c
>>>>>>> refs/remotes/origin/main



g = 10
y = 20

if g > y:
    print("Es mayor") 
else:
    print("No es mayor")