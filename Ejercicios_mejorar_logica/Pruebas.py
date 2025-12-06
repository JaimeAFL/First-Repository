import random

def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()

caja = [1,4,3,6,7,8,2]


tamaño = (len(caja))            # 'size' o tamaño de la lista
posicion_c = len(caja) - 1      # 'posicion' de un elemento en una lista
ultimo_caja = caja [ -1 ]       # Da el ultimo 'valor' de la ultima 'posicion' de la lista o el array


caja_2 = [ ]

while caja:

    for elemento in caja:
        cambio_elemento = caja.pop()
    

