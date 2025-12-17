"""
===============================================================================
GRÁFICO DE CONFIRMADOS VS RECUPERADOS (FILTRANDO POR FALLECIDOS)
===============================================================================

DESCRIPCIÓN GENERAL:
--------------------
Este programa lee un CSV de COVID y genera un gráfico de barras comparando
casos Confirmed (confirmados) y Recovered (recuperados) por país, pero solo
para países con menos de 150 fallecidos (Deaths < 150).

Al final, guarda el gráfico como imagen PNG en la misma carpeta donde está
este script.

FUNCIONAMIENTO:
---------------
1) Localización del CSV:
   - Detecta la carpeta donde está el script usando __file__.
   - Construye la ruta al CSV dentro de la carpeta "datos_covid".

2) Lectura y agregación:
   - Lee el CSV con pandas.
   - Agrupa por país (Country_Region) y suma Confirmed, Deaths y Recovered.

3) Filtrado:
   - Se quedan solo los países con Deaths < 150.
   - Ordena por Confirmed (descendente) para que sea más legible.

4) Preparación para graficar:
   - Convierte los datos a formato “largo” con melt() para poder usar hue en seaborn.
   - Solo se grafican Confirmed y Recovered.

5) Gráfico y guardado:
   - Dibuja el gráfico con seaborn/matplotlib, ajusta etiquetas y márgenes.
   - Guarda la imagen PNG en la carpeta del script.

===============================================================================
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Carpeta donde está ESTE archivo .py
script_dir = os.path.dirname(os.path.abspath(__file__))

# Ruta al CSV dentro de la subcarpeta datos_covid
ruta_csv = os.path.join(script_dir, "datos_covid", "COVID_01-01-2021.csv")

# Leer el CSV
df = pd.read_csv(ruta_csv)

# Agrupar por país y sumar columnas numéricas
resumen_paises = (df.groupby("Country_Region")[["Confirmed", "Deaths", "Recovered"]].sum().reset_index())

# Filtrar países con menos de 150 fallecidos y ordenar por Confirmed
paises_filtrados = resumen_paises[resumen_paises["Deaths"] < 150]
paises_filtrados = paises_filtrados.sort_values(by="Confirmed", ascending=False)

# Pasar a formato largo para graficar Confirmed vs Recovered con hue
datos_plot = paises_filtrados.melt(
   id_vars="Country_Region",
   value_vars=["Confirmed", "Recovered"],
   var_name="Tipo_caso",
   value_name="Casos",)

# Crear el gráfico
sns.set_theme(style="whitegrid")

plt.figure(figsize=(18, 6))
ax = sns.barplot(
    data=datos_plot,
    x="Country_Region",
    y="Casos",
    hue="Tipo_caso",
)

ax.set_title(
    "Casos confirmados y recuperados\n"
    "(Países con menos de 150 fallecidos, enero 2021)")
ax.set_xlabel("País")
ax.set_ylabel("Número de casos")

# Rotar etiquetas del eje X para evitar solapes
plt.xticks(rotation=45, ha="right")

# Ajustar márgenes para que no se corte el texto
plt.tight_layout()

# Guardar el gráfico en la misma carpeta que este script
ruta_salida = os.path.join(script_dir, "grafico_ejercicio5_5.png")
plt.savefig(ruta_salida, dpi=150)