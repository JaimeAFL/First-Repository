
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
out = BASE / "graficos_seaborn" / "caja1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

## VISUALIZANDO RELACIONES ENTRE VARIABLES ##
# -------------------------------------------------------------------------------------------
# Después de examinar las variables por separado, probablemente nos interesará ver si existen 
# interacciones o dependencias entre dos variables. Cuando ambas variables son continuas, utilizamos 
# un diagrama de dispersión (o scatter plot). En Seaborn podemos generarlo con sns.jointplot().

# Vamos a cargar datos de películas
path = "/workspaces/First-Repository/U09_datasets/imdb_movie.csv"
movies = pd.read_csv(path, sep=None, engine="python")

# Veamos si hay interacción entre el número de "likes" en Facebook
# y los ingresos brutos de taquilla que consigue una película
sns.jointplot(data = movies, x='movie_facebook_likes', y='gross')
BASE = Path(__file__).parent
out = BASE / "graficos_seaborn" / "dispersion1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Este tipo de gráficos nos muestra la distribución conjunta del par de variables, junto con las distribuciones 
# o histogramas marginales de cada variable independiente. Además, nos indica cuál es el coeficiente de Pearson 
# para la correlación lineal entre las variables.

# vamos a quedarnos con las películas que tienen datos de "likes"
movies_fb = movies.loc[movies['movie_facebook_likes'] > 0, ['movie_facebook_likes','gross']]
# aplicamos `log10` a las variables antes de pintar
sns.jointplot(data = np.log10(movies_fb), x = 'movie_facebook_likes', y = 'gross', )

BASE = Path(__file__).parent
out = BASE / "graficos_seaborn" / "mapa1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Si lo preferimos, podemos mostrar densidades de probabilidad estimadas en lugar 
# de las observaciones e histogramas.

sns.jointplot(data = np.log10(movies_fb), x = 'movie_facebook_likes', y = 'gross', kind="kde")
out = BASE / "graficos_seaborn" / "mapa2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Una vez que hemos identificado una posible interacción entre variables, 
# podemos estimar y pintar un modelo ajustado a las observaciones.
# Con sns.regplot(), además de mostrar los puntos para cada observación, 
# también se ajusta un modelo de regresión lineal para y ~ x
# y pinta la recta correspondiente al ajuste con el intervalo de confianza al 95%. 
# Si preferimos omitir este ajuste lineal, basta con incluir la opción 'fit_reg=False'.

# aplicamos `log10` a las variables antes de pintar
sns.regplot(data = np.log10(movies_fb), x = 'movie_facebook_likes', y = 'gross')
out = BASE / "graficos_seaborn" / "regresion_y_dispersion1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# -- IMPORTANTE --

# Ahora parece que tenemos una relación algo más evidente entre ambas variables.
# Cuando queremos ajustar modelos entre dos variables también podemos usar la función sns.lmplot().
# En realidad, sns.regplot() es una versión reducida de ésta. Con sns.lmplot() podemos controlar 
# distintos parámetros del ajuste, tipo de modelo, emplear regresión robusta, etc.


## COMPARANDO NIVELES O CATEGORIAS ##
# -------------------------------------------------------------------------------------------
# ¿Y qué ocurre si trabajamos también con variables categóricas? En estos casos queremos ver cómo varía 
# la respuesta (variable dependiente) en función del nivel o categoría.

# Por ejemplo, veamos cómo varían las temperaturas medias mensuales en función de la ciudad.
sns.swarmplot(data=meteo_mes, x='mes', y='temp_c', hue='ciudad')
out = BASE / "graficos_seaborn" / "plot2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Hemos indicado que coloree los puntos en función de la ciudad (hue='ciudad')

# Igual que utilizamos un boxplot para ver la distribución de una variable, 
# podemos ver la distribución por niveles o categorías.
sns.boxplot(data=meteo_mes, x='mes', y='temp_c')
out = BASE / "graficos_seaborn" / "caja2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# También podemos dividir por otra variable categórica usando 'hue' de nuevo.
sns.boxplot(data=meteo_mes, x='mes', y='temp_c', hue='año')
out = BASE / "graficos_seaborn" / "caja3.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")


# Otra forma de ver la distribución de una variable dependiendo de distintos factores 
# o categorías es mediante un gráfico de violín. se estiman la densidad de los datos

sns.violinplot(data=meteo_mes, x='mes', y='temp_c', hue='año')
out = BASE / "graficos_seaborn" / "violin1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Y podemos partir cada violin y que cada mitad se aplique a un nivel, utilizando el argumento 'split=True'
sns.violinplot(data=meteo_mes, x='mes', y='temp_c', hue='año', split=True)
out = BASE / "graficos_seaborn" / "violin2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Por último, otra forma de comparar valores entre categorías es utilizando gráficos de barras. 
# Para ello tenemos la función sns.barplot(), que muestra un indicador agregado estadístico 
# de las observaciones para cada categoría (por defecto calcula la media)ç
sns.barplot(data=meteo_mes, x='mes', y='temp_c', hue='año')
out = BASE / "graficos_seaborn" / "barras1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")


## FACETS ##
# -----------------------------------------------------------------------------------------------------
# Cuando tenemos que analizar y visualizar datos con varias dimensiones, suele ser muy útil representar 
# simultáneamente múltiples vistas de diferentes subconjuntos de datos y dimensiones. Para ello utilizamos 
# gráficos múltiples organizados en cuadrículas o rejillas (FACETS). esta organización de gráficos se consigue 
# mediante un objeto sns.FacetGrid.

# Vamos a seleccionar datos de unas pocas ciudades
meteo_bvz = meteo_mes[--meteo_mes['ciudad'].isin(['Bilbao','Valencia','Zaragoza'])]
# Pintar una rejilla con tantas filas como años
# y tantas columnas como ciudades;
# en cada panel incluir un gráfico de puntos 
# de temperatura por mes
sns.FacetGrid(data=meteo_bvz, row='año', col='ciudad').map(sns.pointplot, "mes", "temp_c")
out = BASE / "graficos_seaborn" / "facets1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")

# Con sns.FacetGrid hemos definido una rejilla con tantas filas como años y tantas columnas como ciudades. 
# Sobre cada celda del grid construido, aplicamos (con map) la función gráfica que queremos representar; 
# en este caso un gráfico de puntos (sns.pointplot) de temperatura por cada mes.

# Podemos utilizar el color (o la forma de los puntos) para representar dimensiones adicionales de los datos.

# Usamos `pd.melt` para pasar de datos en modo 'ancho'
	# a modo 'largo' o apilado.
meteo_bvz_long = pd.melt(meteo_bvz, 
	                         id_vars=['año','mes','ciudad'], 
	                         value_vars=['temp_c','viento_vel_kmh'], 
	                         var_name='variable', value_name='valor')

	# Ahora en cada fila de la rejilla representamos una variable meteo
	# y con el color representamos el año
sns.FacetGrid(meteo_bvz_long, row='variable', col='ciudad', hue='año').map(sns.pointplot, 'mes', 'valor')
out = BASE / "graficos_seaborn" / "facets2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")