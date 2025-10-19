
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

# Cierra posibles figuras previas para evitar “manchas”
plt.close('all')
# Dibuja el gráfico sobre 'ax'
sns.swarmplot(data=meteo_mes, x="mes", y="temp_c")
# Ajusta márgenes automáticamente
plt.tight_layout()
# Construye la ruta de salida dentro del workspace
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "plot.png"
# Crea la carpeta si no existe
out.parent.mkdir(parents=True, exist_ok=True)
# Guarda la figura
plt.savefig(out, dpi=150, bbox_inches="tight")
# Imprime la ruta absoluta para comprobar que se ha creado correctamente
print (f"OK -> {out.resolve()}")
# Cierra la figura actual y no 'manchamos' la siguiente
plt.close(plt.gcf())

# sns.swarmplot() crea un gráfico de dispersión evitando que se solapen los puntos.

## DESCUBRIENDO LA DISTRIBUCION DE LOS DATOS ##
# -------------------------------------------------------------------------------------------
# Una de las primeras cosas que hacemos al ponernos a trabajar con un nuevo conjunto de datos 
# es examinar distintas medidas descriptivas de la distribución, como la media, la desviación 
# típica, los mínimos y máximos, etc. a la hora de examinar gráficamente nuestros datos,
# usaremos sns.displot().
plt.close('all')
sns.displot(meteo_mes['viento_vel_kmh'], kde=True)
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "historico1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Podemos omitir el estimador de densidad con la opción 'kde = False'. También podemos añadir 
# marcadores para ver el número de observaciones de cada valor en el eje X con la opción 'rug = True'.
plt.close('all')
sns.displot(meteo_mes['viento_vel_kmh'], kde=False, rug=True)
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "historico2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Otra forma de ver la distribución de una variable es mediante un diagrama de caja o boxplot.
plt.close('all')
sns.boxplot(data=meteo_mes, y='viento_vel_kmh')
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "caja1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

## VISUALIZANDO RELACIONES ENTRE VARIABLES ##
# -------------------------------------------------------------------------------------------
# Después de examinar las variables por separado, probablemente nos interesará ver si existen 
# interacciones o dependencias entre dos variables. Cuando ambas variables son continuas, utilizamos 
# un diagrama de dispersión (o scatter plot). En Seaborn podemos generarlo con sns.jointplot().

# Vamos a cargar datos de películas
from scipy.stats import pearsonr
path = "/workspaces/First-Repository/U09_datasets/imdb_movie.csv"
movies = pd.read_csv(path, sep=None, engine="python")

# Veamos si hay interacción entre el número de "likes" en Facebook
# y los ingresos brutos de taquilla que consigue una película
plt.close('all')

# Datos log10 seguros (sin ceros/negativos)
movies_fb = movies.loc[movies['movie_facebook_likes'] > 0, ['movie_facebook_likes','gross']]
cols = ["movie_facebook_likes", "gross"]
df = movies_fb[cols].replace(0, np.nan).dropna()
df = np.log10(df)

g = sns.jointplot(
    data = movies, x='movie_facebook_likes', y='gross'
    , kind = "scatter", height=5, ratio=5, space=0)

# Calculamos el coeficiente de Pearson y el p-valor asociado
r, p = pearsonr(df["movie_facebook_likes"], df["gross"])
g.ax_joint.text(
    0.5, 0.95, f"pearsonr = {r:.2f}; p = {p:.1e}",
    transform=g.ax_joint.transAxes, ha="center", va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "dispersion1.png"
out.parent.mkdir(parents=True, exist_ok=True)
g.figure.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Este tipo de gráficos nos muestra la distribución conjunta del par de variables, junto con las distribuciones 
# o histogramas marginales de cada variable independiente. Además, nos indica cuál es el coeficiente de Pearson 
# para la correlación lineal entre las variables.

# vamos a quedarnos con las películas que tienen datos de "likes"
movies_fb = movies.loc[movies['movie_facebook_likes'] > 0, ['movie_facebook_likes','gross']]
# aplicamos `log10` a las variables antes de pintar

plt.close('all')
g = sns.jointplot(data = np.log10(movies_fb), x = 'movie_facebook_likes', y = 'gross', )

r, p = pearsonr(df["movie_facebook_likes"], df["gross"])
g.ax_joint.text(
    0.5, 0.95, f"pearsonr = {r:.2f}; p = {p:.1e}",
    transform=g.ax_joint.transAxes, ha="center", va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "mapa1.png"
out.parent.mkdir(parents=True, exist_ok=True)
g.figure.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Si lo preferimos, podemos mostrar densidades de probabilidad estimadas en lugar 
# de las observaciones e histogramas.

plt.close('all')
g = sns.jointplot(
    data=df, x="movie_facebook_likes", y="gross",
    kind="kde", fill=True, height=5, ratio=5, space=0)

r, p = pearsonr(df["movie_facebook_likes"], df["gross"])
g.ax_joint.text(
    0.5, 0.95, f"pearsonr = {r:.2f}; p = {p:.1e}",
    transform=g.ax_joint.transAxes, ha="center", va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "mapa2.png"
out.parent.mkdir(parents=True, exist_ok=True)
g.figure.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Una vez que hemos identificado una posible interacción entre variables, 
# podemos estimar y pintar un modelo ajustado a las observaciones.
# Con sns.regplot(), además de mostrar los puntos para cada observación, 
# también se ajusta un modelo de regresión lineal para y ~ x
# y pinta la recta correspondiente al ajuste con el intervalo de confianza al 95%. 
# Si preferimos omitir este ajuste lineal, basta con incluir la opción 'fit_reg=False'.

# aplicamos `log10` a las variables antes de pintar
plt.close('all')
g = sns.regplot(data = np.log10(movies_fb), x = 'movie_facebook_likes', y = 'gross')
ax = plt.gca()

r, p = pearsonr(df["movie_facebook_likes"], df["gross"])
ax.text(
    0.5, 0.95, f"pearsonr = {r:.2f}; p = {p:.1e}",
    transform= ax.transAxes, ha="center", va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "regresion_y_dispersion1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

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
plt.close('all')
sns.swarmplot(data=meteo_mes, x='mes', y='temp_c', hue='ciudad')
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "plot2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Hemos indicado que coloree los puntos en función de la ciudad (hue='ciudad')

# Igual que utilizamos un boxplot para ver la distribución de una variable, 
# podemos ver la distribución por niveles o categorías.
plt.close('all')
g = sns.boxplot(data=meteo_mes, x='mes', y='temp_c')
ax = plt.gca()

r, p = pearsonr(df["movie_facebook_likes"], df["gross"])
ax.text(
    0.5, 0.95, f"pearsonr = {r:.2f}; p = {p:.1e}",
    transform= ax.transAxes, ha="center", va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8))

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "caja2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# También podemos dividir por otra variable categórica usando 'hue' de nuevo.
plt.close('all')
sns.set_theme(style="whitegrid")
pal = sns.color_palette("deep", 2)

sns.boxplot(data=meteo_mes, x='mes', y='temp_c', hue='año')

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "caja3.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Otra forma de ver la distribución de una variable dependiendo de distintos factores 
# o categorías es mediante un gráfico de violín. se estiman la densidad de los datos
plt.close('all')
sns.set_theme(style="whitegrid")
pal = sns.color_palette("deep", 2)

sns.violinplot(data=meteo_mes, x='mes', y='temp_c', hue='año')


pal = sns.color_palette("deep", 2)
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "violin1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Y podemos partir cada violin y que cada mitad se aplique a un nivel, utilizando el argumento 'split=True'
plt.close('all')
sns.set_theme(style="whitegrid")
pal = sns.color_palette("deep", 2)

sns.violinplot(data=meteo_mes, x='mes', y='temp_c', hue='año', split=True)

BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "violin2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Por último, otra forma de comparar valores entre categorías es utilizando gráficos de barras. 
# Para ello tenemos la función sns.barplot(), que muestra un indicador agregado estadístico 
# de las observaciones para cada categoría (por defecto calcula la media)
plt.close('all')
sns.barplot(data=meteo_mes, x='mes', y='temp_c', hue="año")
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "barras1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

## FACETS ##
# -----------------------------------------------------------------------------------------------------
# Cuando tenemos que analizar y visualizar datos con varias dimensiones, suele ser muy útil representar 
# simultáneamente múltiples vistas de diferentes subconjuntos de datos y dimensiones. Para ello utilizamos 
# gráficos múltiples organizados en cuadrículas o rejillas (FACETS). esta organización de gráficos se consigue 
# mediante un objeto sns.FacetGrid.

# Vamos a seleccionar datos de unas pocas ciudades
meteo_bvz = meteo_mes[--meteo_mes['ciudad'].isin(['Bilbao','Valencia','Zaragoza'])]

# Pintar una rejilla con tantas filas como años y tantas columnas como ciudades;
# en cada panel incluir un gráfico de puntos de temperatura por mes.
plt.close('all')
sns.FacetGrid(data=meteo_bvz, row='año', col='ciudad').map(sns.pointplot, "mes", "temp_c")
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "facets1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

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
plt.close('all')
sns.FacetGrid(meteo_bvz_long, row='variable', col='ciudad', hue='año').map(sns.pointplot, 'mes', 'valor')
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "facets2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())



# --( 2 )-- AJUSRANDO LOS GRÁFICOS DE SEABORN
# ------------------------------------------------------------------------------------------
# Seaborn permite ajustar muchos aspectos de los gráficos generados, tanto a nivel global como a nivel particular 
# de cada gráfico. Los objetos gráficos que devuelven las funciones de Seaborn constan a su vez de dos partes, 
# un objeto que representa los ejes (axes) y otro objeto que representa la figura (figure). Podremos modificar 
# propiedades del gráfico a través de estos objetos.

## ESTILOS Y TEMAS ##
# -------------------------------------------------------------------------------------------
# Seaborn incluye cinco temas gráficos predefinidos con distintas configuraciones de estilos para usar directamente con nuestras figuras.

# | Tema gráfico |
# | ------------ |
# | darkgrid     |
# | whitegrid    |
# | dark         |
# | white        |
# | ticks        |

# Para especificar qué tema queremos aplicar, empleamos la función sns.set_style()
plt.close('all')
sns.set_style('darkgrid')
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes)
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "tema1.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())

# Sobre un tema podemos introducir nuestros propios ajustes. La función sns.set_style() 
# admite que le pasemos un diccionario con nuestras configuraciones de elementos particulares del gráfico.

plt.close('all')
sns.set_style('darkgrid', rc = {'axes.grid': False})
sns.swarmplot(x='mes', y='temp_c', data=meteo_mes)
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "tema2.png"
out.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())
