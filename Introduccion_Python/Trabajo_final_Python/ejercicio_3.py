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

# Parámetros para la generación de vectores aleatorios
min_vectores = 2
max_vectores = 6
min_longitud = 2
max_longitud = 8
min_valor = 1
max_valor = 20
# Limite para evitar combinaciones infinitas
max_combinaciones = 200     

# Generar vectores aleatorios con un control  de las combinaciones
vectores = []
combinaciones_estimadas = 1

# Regenerar hasta obtener una cantidad de vectores dentro del límite (max_combinaciones)
while True:
    num_vectores = rd.randint(min_vectores, max_vectores)
    vectores = []
    combinaciones_estimadas = 1
    
    for i in range(num_vectores):
        longitud = rd.randint(min_longitud, max_longitud)
        vector = [rd.randint(min_valor, max_valor) for i in range(longitud)]
        vectores.append(vector)
        combinaciones_estimadas *= longitud
    
    # Si las combinaciones están dentro del límite, salir del bucle
    if combinaciones_estimadas <= max_combinaciones:
        break
    # Si no, regenerar con otros valores aleatorios

print("Número de vectores generados:", len(vectores))
print("Longitudes de los vectores:", [len(v) for v in vectores])
print("Combinaciones estimadas:", combinaciones_estimadas)
print("Vectores:", vectores)
print()

def producto_cartesiano(vectores):
    """
    Calcula el producto cartesiano y muestra por pantalla el resultado.
    Recibe:
    - vectores: lista de listas (vectores de diferentes longitudes)

    Devuelve:
    - lista con todas las combinaciones posibles

    Ventaja:
    Usa un generador para ser eficiente en memoria.
    """
    if not vectores:
        print("No hay vectores guardados. Reconsidere pasos previos y ejecutelos "
              "para que este texto no aparezca.")
        return
    
    # Generador recursivo que produce combinaciones bajo demanda
    def generar_combinaciones(vecs):

        # Sin vectores
        if not vecs:
            yield ()
            return
        
        # Un solo vector
        if len(vecs) == 1:
            for elemento in vecs[0]:
                yield (elemento,)
            return
        
        # El resto: combinar (n-1) vectores con el último
        for combo in generar_combinaciones(vecs[:-1]):
            for elemento in vecs[-1]:
                yield combo + (elemento,)
    
    # Generar todas las combinaciones y convertir a lista
    combinaciones = list(generar_combinaciones(vectores))
    
    # Mostrar resultados por pantalla
    print("Total combinaciones:", len(combinaciones))
    print("Combinaciones:\n", combinaciones)
    
    return combinaciones

# Llamar a la función producto_cartesiano
resultado = producto_cartesiano(vectores)