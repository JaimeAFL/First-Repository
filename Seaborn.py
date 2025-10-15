
# --------
# SEABORN
# --------


# --( 1 )-- VISUALIZACION DE DATOS: SEABORN
# ------------------------------------------------------------------------------------------
# Ya sabemos cómo manipular y trabajar con nuestros datos en Python. Ahora necesitamos poder 
# visualizarlos gráficamente. Python dispone de un buen número de librerías para construir gráficos. 
# Algunas de las principales son:

# - Matplotlib: la librería de visualización de datos más extendida, se integra con NumPy y las Series de Pandas.
# - Seaborn: librería construida sobre Matplotlib con soporte a funcionalidades más avanzadas y 
#   mejor integración con Pandas.
# - ggplot: librería de visualización inspirada en el paquete ggplot2 de R y su gramática de gráficos. 
#   También se basa en Matplotlib y se integra con Pandas.
# - Bokeh: librería especializada en crear gráficos interactivos para integrar en la web.
# - Plot.ly: librería para construir y compartir gráficos interactivos online.

# Seaborn es una biblioteca de visualización de datos en Python basada en Matplotlib.
# Proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos y
# fáciles de interpretar. Seaborn está diseñado para trabajar bien con estructuras de datos
# como DataFrames de pandas, lo que facilita la visualización de datos complejos.
# Seaborn ofrece una variedad de gráficos predefinidos, como gráficos de dispersión,
# gráficos de barras, gráficos de líneas, gráficos de violín, mapas de calor, entre otros.
# Además, Seaborn incluye funciones para realizar análisis estadísticos y ajustar modelos
# a los datos, lo que permite explorar relaciones y patrones de manera más profunda.
# Seaborn también proporciona opciones de personalización para ajustar la apariencia de los gráficos,
# como paletas de colores, estilos de línea y temas.

# ANTES DE CONTINUAR: 
# Si estás trabajando con Jupyter o con un terminal de IPython (en Spyder la consola interactiva también 
# funciona sobre IPython), antes de empezar a probar los ejemplos y tus propios gráficos deberás ejecutar 
# el siguiente comando:

# %matplotlib inline

# Esto hará que los gráficos se muestren directamente en la celda de Jupyter o en la consola de IPython, 
# en lugar de abrirse en una ventana aparte.

## UN PRIMER GRÁFICO ##
# -----------------------------------------------------------------------------------------------------
# Vamos a cargar otra vez nuestros datos meteorológicos y pintemos las temperaturas observadas por mes.

# Cargamos las librerías NumPy y Pandas
# Cargamos Matplotlib y Seaborn
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl; mpl.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# Cargamos nuestros datos meteorológicos
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")

# Vamos a ver ahora las temperaturas por mes
sns.swarmplot(data=meteo_mes, x="mes", y="temp_c")
plt.tight_layout()

BASE = Path(__file__).parent
out = BASE / "graficos_seaborn" / "plot.png"
out.parent.mkdir(parents=True, exist_ok=True)

plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
# sns.swarmplot() crea un gráfico de dispersión evitando que se solapen los puntos.

## DESCUBRIENDO LA DISTRIBUCION DE LOS DATOS ##
# -------------------------------------------------------------------------------------------
# Una de las primeras cosas que hacemos al ponernos a trabajar con un nuevo conjunto de datos 
# es examinar distintas medidas descriptivas de la distribución, como la media, la desviación 
# típica, los mínimos y máximos, etc. a la hora de examinar gráficamente nuestros datos,
# usaremos sns.displot().

sns.displot(meteo_mes['viento_vel_kmh'], kde=True)
BASE = Path(__file__).parent
out = BASE / "graficos_seaborn" / "historico1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Podemos omitir el estimador de densidad con la opción 'kde = False'. También podemos añadir 
# marcadores para ver el número de observaciones de cada valor en el eje X con la opción 'rug = True'.

sns.displot(meteo_mes['viento_vel_kmh'], kde=False, rug=True)
BASE = Path(__file__).parent
out = BASE / "graficos_seaborn" / "historico2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Otra forma de ver la distribución de una variable es mediante un diagrama de caja o boxplot.
sns.boxplot(data=meteo_mes, y='viento_vel_kmh')
BASE = Path(__file__).parent
out = BASE / "graficos_seaborn" / "historico2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

## VISUALIZANDO RELACIONES ENTRE VARIABLES ##
# -------------------------------------------------------------------------------------------
# Después de examinar las variables por separado, probablemente nos interesará ver si existen 
# interacciones o dependencias entre dos variables. Cuando ambas variables son continuas, utilizamos 
# un diagrama de dispersión (o scatter plot). En Seaborn podemos generarlo con sns.jointplot().

# Vamos a cargar datos de películas


# Veamos si hay interacción entre el número de "likes" en Facebook
# y los ingresos brutos de taquilla que consigue una película
