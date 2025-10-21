# -*- coding: utf-8 -*-
"""
Ejemplo de módulo con definicion de funciones
y declaración de variables
"""

# Definimos funciones del módulo

def fibonacci(n):
    """Calcula el n-ésimo elemento de la serie de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def genera_multiplicador(n):
    """Esta función crea y devuelve a su vez 
    una nueva función que multiplicará cualquier valor por n"""
    return lambda x: x * n


# Declaramos variables del módulo

# Asignamos a esta variable la función multiplicadora por 2
doblar = genera_multiplicador(2)

# Asignamos a esta variable la función multiplicadora por 3
triplicar = genera_multiplicador(3)
