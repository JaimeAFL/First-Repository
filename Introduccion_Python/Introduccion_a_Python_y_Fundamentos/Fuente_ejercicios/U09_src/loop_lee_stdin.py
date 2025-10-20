# -*- coding: utf-8 -*-
"""
Ejemplo de lectura de datos de la entrada estándar,
capturada desde teclado al lanzar el script por linea de comandos
"""

import sys

# Escribimos un mensaje inicial para el usuario en STDOUT
sys.stdout.write("Prueba a escribir (una línea vacía sirve para salir) ...\n")

while True:
  
    # Leemos de STDIN
    x = sys.stdin.readline()
    
    # Comprobamos si no es una línea vacía
    if (len(x) > 0) and (x != '') and (x != '\n'):
        mensaje = "He leído {}".format(x)
        sys.stdout.write(mensaje)
    else:
        # Es una línea vacía, salimos
        sys.stderr.write("No hay más datos\n")
        break
