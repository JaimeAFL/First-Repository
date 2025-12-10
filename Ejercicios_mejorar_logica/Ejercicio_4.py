import random
def generar_caja ():
    lista_caja = random.sample(range(0, 10),7)
    return lista_caja

caja = generar_caja()
print(caja)
caja_2 = []

while caja:
    pila_1 = caja.pop()

    while caja_2 and caja_2 [-1] > pila_1:
        pila_2 = caja_2.pop()
        caja = caja + [pila_2]
    caja_2 = caja_2 + [pila_1]

print(caja_2)


# =================================================(EJERCICIO NUEVO)================================================
# Rehacer este ejercicio pero con palabras y de orden alfabetico:
# - no puedo usar ninguna función relacionada con listas ni variable = [-1], ni accesos rápidos a la última posición.

# MUST:
# - Todo por posición. 
# - Una sentencia por línea.
# - TO-DO en 'for' y no utilizar los 'whiles'
# - MIRAR SUBSTRING en documentación Python
# - TENGO que utulizar si o si 'for' numérico

# ===============================================(EJERCICIO NUEVO 2)================================================
# Una palabra reordenando sus letras en orden alfabético