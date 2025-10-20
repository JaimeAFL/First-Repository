# -----------------------------------------
### MODELSO ESTADISTICOS: STATS-MODELS ###
# -----------------------------------------


# -------------------------------------------------------------------------------------------------------
# --( 1 )-- MODELOS ESTADÍSTICOS: STATSMODELS --
# -------------------------------------------------------------------------------------------------------

## MODELOS LINEALES SIMPLES Y MÚLTIPLES ##
# -------------------------------------------------------------------------
# Statsmodels es una librería para Python especializada en la exploración, estimación y evaluación de modelos, 
# ajuste de parámetros y realización de tests estadísticos sobre conjuntos de datos y distribuciones.
# Statsmodels está construido sobre la base de NumPy, y se integra con las estructuras de datos de Pandas. 
# Además, incluye la posibilidad de definir modelos siguiendo la sintaxis de fórmulas de R, 
# lo que facilita la transición para los usuarios de este lenguaje.

# Cargamos las librerías NumPy y Pandas
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pathlib import Path
# Cargamos Matplotlib y Seaborn
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
# Cargamos los datos de gasto en publicidad

ads = pd.read_csv("/workspaces/First-Repository/U09_datasets/advertising.csv", sep = ";")

# La regresión lineal es dibujar la “mejor línea” que pasa por un montón de puntos para predecir algo.
# - Tienes una variable que quieres predecir: 𝑌 (por ejemplo, notas).
# - Tienes una variable que crees que explica Y: 𝑋 (por ejemplo, horas de estudio).

# Buscas una línea: Y = b0 + b1X
# - b0 es la intersección con el eje Y (cuando X = 0). por dónde corta la línea el eje vertical.
# - b1 es la pendiente de la línea (el cambio en Y por cada unidad de cambio en X). 
#   cuánto sube o baja Y si aumentas X en 1.

# Cómo se elige la “mejor línea”
# - Calcula los errores (residuos): diferencia entre lo observado y lo que dice la línea.
# - El método de mínimos cuadrados elige la línea que hace pequeña la suma de errores al cuadrado.

# Qué te dice el resultado
# Pendiente b1: : efecto por unidad de X. Positiva sube, negativa baja.
# Intersección b0: valor de Y cuando X = 0. (a veces no tiene sentido práctico, no pasa nada).
# R**2: de 0 a 1. Qué porcentaje de la variación de Y explica la línea.
# Valores p: si son bajos (< 0.05), hay evidencia de relación.

# Cuándo funciona bien
# Relación más o menos recta entre X y Y.
# Errores sin patrón raro y de tamaño parecido.
# Sin puntos extremos que lo destrocen.

# Ahora revisamos gráficamente la estructura de los datos.
# Nos preparamos los datos de forma que sea más fácil pintarlos
ads_m = ads.melt(id_vars='Sales', value_vars=['TV','Radio','Newspaper'], var_name='Media', value_name='Spend')

# Representamos en una rejilla las ventas según gasto en cada medio
g = sns.FacetGrid(ads_m, col='Media', col_order=['TV','Radio','Newspaper'],
                  sharex=False, height=2.2, aspect=1.4)
g.map(sns.regplot, 'Spend', 'Sales', fit_reg=False, scatter_kws={'s':20})
g.set_axis_labels('Spend', 'Sales')
g.set_titles('Media = {col_name}')
BASE = Path.cwd()
out = BASE / "graficos_seaborn" / "grafico_ventas_model.png"
out.parent.mkdir(parents=True, exist_ok=True)
g.figure.savefig(out, dpi=150, bbox_inches="tight")
print (f"OK -> {out.resolve()}")
plt.close(plt.gcf())
