"""
===============================================================================
PROGRAMA: EVOLUCIÓN MUNDIAL COVID (ENERO–MARZO 2021) Y GRÁFICO DE LÍNEAS
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa lee tres archivos CSV (enero, febrero y marzo de 2021) con datos
de COVID y calcula los totales mundiales de:
- Confirmed  (casos confirmados)
- Deaths     (fallecidos)
- Recovered  (recuperados)

Después crea un DataFrame resumen por mes y genera un gráfico de líneas con
Seaborn/Matplotlib mostrando la evolución del primer trimestre de 2021.
El gráfico se guarda como PNG en la misma carpeta del script.

FUNCIONAMIENTO:
---------------
1) Localización de archivos:
   - Obtiene la carpeta del script con __file__.
   - Construye las rutas a los CSV dentro de "datos_covid".

2) Carga de datos:
   - Lee cada CSV con pandas.read_csv().

3) Cálculo de totales mundiales:
   - Suma por columnas (Confirmed, Deaths, Recovered) para cada mes.

4) Construcción del resumen mensual:
   - Crea un DataFrame con una fila por mes y columnas:
     Confirmados, Fallecidos, Recuperados.

5) Preparación para graficar:
   - Pasa el DataFrame a formato “largo” con melt() para poder usar hue.
   - Escala los valores a millones para que el eje Y sea más legible.

6) Gráfico y guardado:
   - Dibuja un lineplot con marcador por mes.
   - Ajusta título, etiquetas y márgenes.
   - Guarda el PNG junto al script.

===============================================================================
"""

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Localizar la carpeta del script y construir rutas a los CSV
script_dir = os.path.dirname(os.path.abspath(__file__))

ruta_enero = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")
ruta_febrero = os.path.join(script_dir, "datos_covid", "COVID_01-02-2021.csv")
ruta_marzo = os.path.join(script_dir, "datos_covid", "COVID_01-03-2021.csv")

# Leer los CSV en DataFrames
df_enero = pd.read_csv(ruta_enero)
df_febrero = pd.read_csv(ruta_febrero)
df_marzo = pd.read_csv(ruta_marzo)

# Calcular totales mundiales por mes (suma de columnas)
totales_enero = df_enero[["Confirmed", "Deaths", "Recovered"]].sum()
totales_febrero = df_febrero[["Confirmed", "Deaths", "Recovered"]].sum()
totales_marzo = df_marzo[["Confirmed", "Deaths", "Recovered"]].sum()

# Crear el DataFrame resumen (una fila por mes)
resumen_mensual = pd.DataFrame(
    {
        "Mes": np.array(["Enero", "Febrero", "Marzo"]),
        "Confirmados": np.array([
                totales_enero["Confirmed"],
                totales_febrero["Confirmed"],
                totales_marzo["Confirmed"],]),

        "Fallecidos": np.array([
                totales_enero["Deaths"],
                totales_febrero["Deaths"],
                totales_marzo["Deaths"],]),
                
        "Recuperados": np.array([
                totales_enero["Recovered"],
                totales_febrero["Recovered"],
                totales_marzo["Recovered"],]),
    })

# Pasar a formato largo y escalar a millones (para graficar con hue)
datos_plot = resumen_mensual.melt(
    id_vars="Mes",
    value_vars=["Confirmados", "Fallecidos", "Recuperados"],
    var_name="Tipo_caso",
    value_name="Casos",)

# Convertir a millones para que el eje Y sea más legible
datos_plot["Casos_millones"] = datos_plot["Casos"] / 1_000_000

# Crear el gráfico de líneas y guardarlo
sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 6))
ax = sns.lineplot(
    data=datos_plot,
    x="Mes",
    y="Casos_millones",
    hue="Tipo_caso",
    marker="o",)

# Ajustar leyenda para que no tape las líneas
#    - loc: posición base dentro del eje
#    - bbox_to_anchor: desplaza la leyenda fuera del área del gráfico
ax.legend(
    title="Tipo de caso",
    loc="center left",
    bbox_to_anchor=(1.02, 0.5))

# Títulos y etiquetas de los ejes
ax.set_title("Evolución COVID primer trimestre 2021")
ax.set_xlabel("Mes")
ax.set_ylabel("Número de casos (millones)")

# Ajustar el layout para que no se corte nada
plt.tight_layout()

# Guardar el gráfico en un archivo PNG en la misma carpeta del script
ruta_salida = os.path.join(script_dir, "grafico_ejercicio5_6.png")
plt.savefig(ruta_salida, dpi=150)