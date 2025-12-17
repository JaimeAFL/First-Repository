"""
===============================================================================
TOP 10 PAÍSES CON MÁS CASOS CONFIRMADOS (PANDAS)
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa carga un CSV de COVID, calcula los totales por país y obtiene
los 10 países con más casos confirmados (“Confirmed”) para la fecha del archivo.

Qué hace exactamente:
- Agrupa los datos por país (Country_Region)
- Suma los valores de Confirmed, Deaths y Recovered dentro de cada país
- Ordena los países de mayor a menor por Confirmed
- Selecciona los 10 primeros y los imprime

FUNCIONAMIENTO:
---------------
1) Lectura del CSV:
   - Se carga el archivo en un DataFrame con pandas.read_csv().

2) Resumen por país:
   - groupby("Country_Region") agrupa filas por país.
   - [["Confirmed", "Deaths", "Recovered"]] selecciona columnas numéricas.
   - .sum() suma esas columnas para cada país.

3) Top 10 por confirmados:
   - .sort_values(by="Confirmed", ascending=False) ordena de mayor a menor.
   - .head(10) toma las 10 primeras filas (los 10 países con más confirmados).
   - .reset_index() convierte el índice (Country_Region) en columna para imprimir mejor.

4) Salida:
   - Se imprime la tabla con los 10 países con más casos confirmados.

===============================================================================
"""

import pandas as pd

# Ruta del archivo CSV (ajusta si cambia tu estructura de carpetas)
ruta_csv = ("/workspaces/First-Repository/Introduccion_Python/Trabajo_final_Python/" "datos_covid/COVID_01-01-2021.csv")

# Leer el CSV y cargarlo en un DataFrame
df = pd.read_csv(ruta_csv)

# Agrupar por país y sumar Confirmed, Deaths y Recovered
resumen_paises = (df.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum())

# Ordenar por Confirmed (descendente) y quedarnos con el Top 10
top_10 = (resumen_paises.sort_values(by="Confirmed", ascending=False).head(10).reset_index())

# Mostrar el resultado
print("=== 10 países con más casos confirmados (enero 2021) ===")
print(top_10)