import random
def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()
caja_2 = []

while caja:
    pila_1 = caja.pop()

    while caja_2 and caja_2 [-1] > pila_1:
        pila_2 = caja_2.pop()
        caja = caja + [pila_2]
    caja_2 = caja_2 + [pila_1]
    
print(caja_2)