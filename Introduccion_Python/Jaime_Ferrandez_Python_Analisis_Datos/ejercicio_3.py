"""
===============================================================================
PROGRAMA: PRODUCTO CARTESIANO DE VECTORES ALEATORIOS
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa genera vectores aleatorios y calcula su producto cartesiano,
es decir, todas las combinaciones posibles tomando un elemento de cada vector.

Ejemplo de producto cartesiano:
    Vectores: [[1, 2], [3, 4], [5]]
    Resultado: [(1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5)]

FUNCIONAMIENTO:
---------------
1. GENERACIÓN DE VECTORES ALEATORIOS:
   - Genera entre 2 y 6 vectores
   - Cada vector tiene entre 2 y 8 elementos
   - Los elementos tienen valores entre 1 y 20
   - CONTROL IMPORTANTE: Si el producto cartesiano excede 10,000 combinaciones,
     regenera automáticamente otros vectores para evitar explosión exponencial

2. CÁLCULO DEL PRODUCTO CARTESIANO:
   - Usa un algoritmo recursivo eficiente
   - Genera combinaciones bajo demanda (no todas a la vez en memoria)
   - Muestra el total de combinaciones y la lista completa

3. SALIDA DEL PROGRAMA:
   - Información de los vectores generados
   - Total de combinaciones
   - Lista completa de todas las combinaciones

NOTA SOBRE EFICIENCIA:
----------------------
El número de combinaciones crece exponencialmente:
    - 3 vectores de longitud 5: 5³ = 125 combinaciones
    - 5 vectores de longitud 10: 10⁵ = 100,000 combinaciones
    - 10 vectores de longitud 10: 10¹⁰ = 10 mil millones de combinaciones

Por eso el programa tiene un límite de 10,000 combinaciones para mantener
tiempos de ejecución razonables.

===============================================================================
"""

import random as rd


# Número mínimo y máximo de vectores a generar
min_vectores = 2
max_vectores = 6

# Longitud mínima y máxima de cada vector
min_longitud = 2
max_longitud = 8

# Rango de valores enteros que pueden aparecer dentro de los vectores
min_valor = 1
max_valor = 20

# Límite para el número total de combinaciones posibles del producto cartesiano.
# Si lo superamos, regeneramos los vectores para evitar un número enorme de combinaciones.
max_combinaciones = 200

# Lista que contendrá los vectores aleatorios
vectores = []

# Variable para llevar la cuenta del número estimado de combinaciones
combinaciones_estimadas = 1

# Generar vectores aleatorios controlando el número de combinaciones:
#   - Elegimos aleatoriamente cuántos vectores vamos a crear (entre min_vectores y max_vectores).
#   - Para cada vector elegimos una longitud aleatoria.
#   - Calculamos el número de combinaciones posibles como el producto de las longitudes.
#   - Si ese producto es mayor que max_combinaciones, repetimos el proceso
#     para no acabar con una explosión de combinaciones.
while True:
    # Elegir aleatoriamente cuántos vectores se van a generar
    num_vectores = rd.randint(min_vectores, max_vectores)

    # Reiniciar la lista de vectores y el contador de combinaciones
    vectores = []
    combinaciones_estimadas = 1

    # Generar cada vector
    for i in range(num_vectores):
        # Longitud aleatoria para este vector
        longitud = rd.randint(min_longitud, max_longitud)

        # Vector con valores aleatorios entre min_valor y max_valor
        vector = [rd.randint(min_valor, max_valor) for i in range(longitud)]
        vectores.append(vector)

        # Actualizar el número estimado de combinaciones:
        # producto de las longitudes de todos los vectores
        combinaciones_estimadas *= longitud

    # Si el número de combinaciones no supera el límite, salimos del bucle
    if combinaciones_estimadas <= max_combinaciones:
        break
    # Si lo supera, se vuelve al inicio del while y se generan otros vectores

# Información básica sobre los vectores generados
print("Número de vectores generados:", len(vectores))
print("Longitudes de los vectores:", [len(v) for v in vectores])
print("Combinaciones estimadas:", combinaciones_estimadas)
print("Vectores:", vectores)
print()

# Función para calcular el producto cartesiano de una lista de vectores
def producto_cartesiano(vectores):
    """
    Calcula y muestra el producto cartesiano de una lista de vectores.
    vectores : list[list[int]]
        Lista de vectores (listas) sobre los que se quiere hacer el producto cartesiano.

    Funcionamiento:
    Utiliza un generador recursivo interno para ir combinando:
      - Si no hay vectores: devuelve una tupla vacía.
      - Si hay un solo vector: genera tuplas de 1 elemento (cada valor del vector).
      - Si hay varios vectores:
          producto_cartesiano de los n-1 primeros vectores
          combinado con cada elemento del último vector.
    """
    # Si la lista de vectores está vacía, no se puede calcular el producto
    if not vectores:
        print(
            "No hay vectores guardados. Reconsidere pasos previos y ejecútelos "
            "para que este texto no aparezca."
        )
        return

    # Generador recursivo que produce combinaciones bajo demanda
    def generar_combinaciones(vecs):
        # Caso base 1: no hay vectores
        if not vecs:
            # Devolvemos una tupla vacía como punto de partida
            yield ()
            return

        # Caso base 2: solo queda un vector
        if len(vecs) == 1:
            # Cada elemento del vector genera una tupla de un solo valor
            for elemento in vecs[0]:
                yield (elemento,)
            return

        # Caso general: combinar el producto de los n-1 primeros vectores
        # con cada elemento del último vector:
        #   - generar_combinaciones(vecs[:-1]) genera todas las combinaciones
        #     posibles de los vectores excepto el último.
        #   - Para cada combinación parcial, añadimos cada elemento del último vector.
        for combo in generar_combinaciones(vecs[:-1]):
            for elemento in vecs[-1]:
                # combo es una tupla, así que sumamos una tupla de 1 elemento
                yield combo + (elemento,)

    # Generar todas las combinaciones y convertir el generador en una lista
    combinaciones = list(generar_combinaciones(vectores))

    # Mostrar resultados por pantalla
    print("Total combinaciones:", len(combinaciones))
    print("Combinaciones:\n", combinaciones)

    return combinaciones

# Llamar a la función producto_cartesiano con los vectores generados
resultado = producto_cartesiano(vectores)