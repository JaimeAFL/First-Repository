"""
===============================================================================
TOTALES DE COVID POR PAÍS (AGRUPACIÓN CON PANDAS)
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa carga un archivo CSV con datos de COVID y genera un resumen por
país, sumando los casos totales de varias métricas:
- Confirmed (confirmados)
- Deaths (muertes)
- Recovered (recuperados)
- Active (activos)

El resultado final es una tabla donde cada fila es un país y las columnas son
las sumas totales de esas métricas para ese país.

FUNCIONAMIENTO:
---------------
1) Lectura del CSV:
   - Se carga el archivo en un DataFrame con pandas.read_csv().

2) Agrupación y suma:
   - groupby("Country_Region") agrupa las filas por país.
   - [["Confirmed", "Deaths", "Recovered", "Active"]] selecciona las columnas numéricas.
   - .sum() suma esas columnas dentro de cada país.

3) Ajuste del formato:
   - .reset_index() convierte "Country_Region" en una columna normal (no en índice),
     para que el DataFrame quede más cómodo de imprimir y usar.

4) Salida:
   - Se imprime el DataFrame resumen con los totales por país.

===============================================================================
"""

import pandas as pd
import os


# Carpeta donde está este script (por ejemplo, ejercicio5_2.py)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta completa al archivo CSV dentro de la subcarpeta "datos_covid"
ruta_csv = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")

# Leer el CSV y cargarlo en un DataFrame de pandas
df = pd.read_csv(ruta_csv)

# Agrupar por país y sumar las columnas numéricas de interés
#   - groupby("Country_Region"):
#       agrupa todas las filas de un mismo país.
#   - [["Confirmed", "Deaths", "Recovered", "Active"]]:
#       nos quedamos solo con estas columnas numéricas.
#   - sum():
#       suma los valores de cada país para esas columnas (totales del mes).
#   - reset_index():
#       convierte el índice de grupo (Country_Region) en una columna normal.
resumen_paises = (df.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered", "Active"]].sum().reset_index())

# Mostrar el resultado por pantalla
print("Totales de COVID por país (enero 2021)")
print("--------------------------------------")
print(resumen_paises)
