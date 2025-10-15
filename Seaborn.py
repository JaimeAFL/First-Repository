
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

# Vamos a cargar otra vez nuestros datos meteorológicos y pintemos las temperaturas observadas por mes.

# Cargamos las librerías NumPy y Pandas
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Cargamos Matplotlib y Seaborn
import matplotlib as mpl
mpl.use("Agg")  
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Cargamos nuestros datos meteorológicos
meteo_mes = pd.read_csv("./U09_datasets/meteo_mes_agg.csv", sep = ";")

# Vamos a ver ahora las temperaturas por mes
sns.swarmplot(data=meteo_mes, x='mes', y='temp_c')
plt.tight_layout()
plt.show()
plt.savefig("plot.png", dpi=150)
print("OK -> plot.png")

# sns.swarmplot() crea un gráfico de dispersión evitando que se solapen los puntos.