

# -------------------------------------------( EJERCICIO 4 )----------------------------------------------------
# Hacer el algoritmo por mi mismo timsort sin SORTED y sin APPEND, o sea 
# también tendré que hacer APPEND por mi mismo. Tendré que investigar ordenado de la 'pila'.

caja = [10, 3, 50, 56, 42, 24, 4, 112, 69, 54, 12, 30, 79, 80]

# tengo que cambiar lo que hay dentro de la caja, buscar su posicion
# y truco, utilizar 'str' para volver los valores en strings

auxiliar = str(caja [::1])
print(auxiliar)

def cambio_posicion (lista, a, b, c):
    
    memoria = lista [a]
    lista [a] = lista [b]
    lista [b] = lista [c]
    lista [c] = memoria
    return lista



for a in caja:

    for b in caja:
        a = a > b

        for c in caja:
            b = b > c



