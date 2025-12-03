

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







# tengo que cambiar lo que hay dentro de la caja, buscar su posicion
# y truco, utilizar 'str' para volver los valores en strings

lista_caja1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]

auxiliar1 = str(lista_caja1)


def cambio_posicion (lista, a, b):
    
    memoria = lista [a]
    lista [a] = lista [b]
    lista [b] = lista [c]
    lista [c] = memoria
    return lista


for a in lista_caja1:

    for b in lista_caja1:
        a = a > b

        for c in lista_caja1:
            b = b > c



g = 10
y = 20

if g > y:
    print("Es mayor") 
else:
    print("No es mayor")