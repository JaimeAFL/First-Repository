


import random

def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()
print(caja)