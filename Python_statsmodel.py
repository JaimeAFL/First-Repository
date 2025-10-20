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


## MODELO LINEAL SIMPLE ##

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

# Para este primer ejemplo, intentamos explicar las ventas a partir del gasto en publicidad en TV.
# Vamos a definir el modelo y realizar el ajuste de coeficientes por mínimos cuadrados con Statsmodels.

import statsmodels.api as sm
# Definimos un modelo y ~ b0 + b1*X + e
# Vector respuesta
y = ads['Sales']

# Matriz de variables explicativas del modelo
X = ads['TV']

# Añadimos un término constante a la matriz del modelo (b0)
X = sm.add_constant(X, prepend=False)

# Construimos el objeto modelo
# usamos un modelo lineal tipo OLS
# (Ordinary Least Squares)
model = sm.OLS(y, X)

# Ajustamos los parámetro
mfitted = model.fit()

# Veamos el resumen del modelo ajustado
print(mfitted.summary())

#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                  Sales   R-squared:                       0.612
# Model:                            OLS   Adj. R-squared:                  0.610
# Method:                 Least Squares   F-statistic:                     312.1
# Date:                Mon, 20 Oct 2025   Prob (F-statistic):           1.47e-42
# Time:                        09:42:33   Log-Likelihood:                -519.05
# No. Observations:                 200   AIC:                             1042.
# Df Residuals:                     198   BIC:                             1049.
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# TV             0.0475      0.003     17.668      0.000       0.042       0.053
# const          7.0326      0.458     15.360      0.000       6.130       7.935
# ==============================================================================
# Omnibus:                        0.531   Durbin-Watson:                   1.935
# Prob(Omnibus):                  0.767   Jarque-Bera (JB):                0.669
# Skew:                          -0.089   Prob(JB):                        0.716
# Kurtosis:                       2.779   Cond. No.                         338.
# ==============================================================================
# Notes: [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


## MODELO LINEAL MULTIPLE ##

# Al explicarte cómo preparar la matriz de diseño del modelo ya te hemos adelantado 
# que podemos incluir todas las variables explicativas que deseemos. No va a existir 
# ninguna diferencia a nivel de las operaciones a realizar.

# Para demostrarlo, ajustemos un modelo para las ventas utilizando como predictores 
# el gasto de publicidad en cada medio:

# Sales = b0 + b1TV + b2Radio + b3Newspaper + e

# Vector respuesta
y = ads['Sales']

# Matriz de variables explicativas del modelo
X = ads[['TV','Radio','Newspaper']]

# Añadimos un término constante a la matriz del modelo (b0)
X = sm.add_constant(X, prepend=False)

# Construimos el objeto modelo
# usamos un modelo lineal tipo OLS
# (Ordinary Least Squares)
model_mlin = sm.OLS(y, X)

# Ajustamos los parámetros del modelo
mlin_fitted = model_mlin.fit()

# Veamos el resumen del modelo ajustado
print(mlin_fitted.summary())

# 	                      OLS Regression Results                      
# 	=================================================================
# 	Dep. Variable:            Sales   R-squared:                0.897
# 	Model:                      OLS   Adj. R-squared:           0.896
# 	Method:           Least Squares   F-statistic:              570.3
# 	Date:          Tue, 28 Nov 2017   Prob (F-statistic):    1.58e-96
# 	Time:                  12:33:31   Log-Likelihood:        -386.18
# 	No. Observations:           200   AIC:                     780.4
# 	Df Residuals:               196   BIC:                     793.6
# 	Df Model:                     3                                
# 	Covariance Type:      nonrobust                              
# 	=================================================================
# 	             coef  std err     t    P>|t|      [0.025      0.975]
# 	TV         0.0458    0.001   32.809   0.000     0.043       0.049
# 	Radio      0.1885    0.009   21.893   0.000     0.172       0.206
# 	Newspaper -0.0010    0.006   -0.177   0.860    -0.013       0.011
# 	const      2.9389    0.312    9.422   0.000     2.324       3.554
# 	=================================================================
# 	Omnibus:                   60.414   Durbin-Watson:          2.084
# 	Prob(Omnibus):              0.000   Jarque-Bera (JB):     151.241
# 	Skew:                      -1.327   Prob(JB):            1.44e-33
# 	Kurtosis:                   6.332   Cond. No.                454.
# 	=================================================================
# 	Notes: [1] Standard Errors assume that the covariance matrix of the errors is correctly specified


# -------------------------------------------------------------------------------------------------------
# --( 2 )-- DEFINIENDO MODELOS CON FORMULAS --
# -------------------------------------------------------------------------------------------------------

# Definir un modelo mediante una matriz de diseño con las variables explicativas no es especialmente complicado. 
# Sobre todo, en Statsmodels, que admite que usemos las columnas de un DataFrame de Pandas directamente.

# Sin embargo, trabajar con matrices de modelo cuando quieres probar distintas variantes (quitando o añadiendo variables, 
# considerando interacciones o transformaciones de variables) puede resultar más engorroso; tendremos que andar preparando 
# una nueva matriz para cada alternativa a explorar.
# Statsmodels ha incluido desde hace algún tiempo la capacidad de definir un modelo mediante fórmulas.

# Cargamos la API con soporte a formulas
import statsmodels.formula.api as smf

# Definimos el modelo usando una formula como en R
model_f = smf.ols(formula = 'Sales ~ TV + Radio + Newspaper', data=ads)

# Ajustamos el modelo
mf_fitted = model_f.fit()

# Resumen
print(mf_fitted.summary())

# 	                      OLS Regression Results                      
# 	=================================================================
# 	Dep. Variable:            Sales   R-squared:                0.897
# 	Model:                      OLS   Adj. R-squared:           0.896
# 	Method:           Least Squares   F-statistic:              570.3
# 	Date:          Tue, 28 Nov 2017   Prob (F-statistic):    1.58e-96
# 	Time:                  12:33:31   Log-Likelihood:        -386.18
# 	No. Observations:           200   AIC:                     780.4
# 	Df Residuals:               196   BIC:                     793.6
# 	Df Model:                     3                                
# 	Covariance Type:      nonrobust                              
# 	=================================================================
# 	             coef  std err     t    P>|t|      [0.025      0.975]
# 	TV         0.0458    0.001   32.809   0.000     0.043       0.049
# 	Radio      0.1885    0.009   21.893   0.000     0.172       0.206
# 	Newspaper -0.0010    0.006   -0.177   0.860    -0.013       0.011
# 	const      2.9389    0.312    9.422   0.000     2.324       3.554
# 	=================================================================
# 	Omnibus:                   60.414   Durbin-Watson:          2.084
# 	Prob(Omnibus):              0.000   Jarque-Bera (JB):     151.241
# 	Skew:                      -1.327   Prob(JB):            1.44e-33
# 	Kurtosis:                   6.332   Cond. No.                454.
# 	=================================================================

# Como cabía esperar, los resultados del ajuste son los mismos. En realidad, el modelo subyacente no cambia, 
# sólo el mecanismo que hemos usado para definirlo. Aparte de la sencillez de uso, tener la definición del modelo 
# de forma textual aporta legibilidad. Es más fácil y rápido interpretar un modelo mediante su formulación 
# que revisando la matriz de diseño.

# IMPORTANTE:
# Si has revisado con atención el modelo y los resultados, tal vez ya te hayas dado cuenta de un cambio sutil al usar 
# una fórmula. No hemos tenido que añadir un término constante explícito como ocurre con las matrices. La API para fórmulas 
# lo hace por nosotros de forma automática (en línea con el funcionamiento en R).


## INTERACCION ENTRE VARIABLES ##
# ------------------------------------------------------------------------
# Si el fenómeno que estamos modelando cumple que cuando todas las variables explicativas valen cero, entonces 
# la respuesta es cero, podemos eliminar del ajuste el término constante o intercept. Eliminar un término se consigue 
# simplemente restando en la fórmula. En nuestro ejemplo, la fórmula pasaría a ser.

# Sales ~ TV + Radio + Newspaper - 1

# Las interacciones entre variables se incluyen en las fórmulas igual que en R.

# ---------------------------------------------------------------
# | Fórmula | Descripción                                       |
# |---------|---------------------------------------------------|
# | Y ~ X*Z | Añadir la interacción entre las vars. X y Z       |
# |         |  Equivalente a Y = β0 + β1X + β2Z + β3(X*Z)       |
# |---------|---------------------------------------------------|
# | Y ~ X:Z | Incluir solo la interacción entre las vars. X y Z |
# |         | Y = β0 + β3(X*Z)                                  |
# |         | Equivalente a Y = β0 + β3(X*Z)                    |
# ---------------------------------------------------------------

## VARIABLES CATEGÓRICAS ##
# ---------------------------------------------------------------------------------------------------------------------------------
# Statsmodels también soporta el uso de variables categóricas en las fórmulas. La librería se encarga de hacer las transformaciones 
# automáticas para añadir las variables dummy necesarias por cada nivel. Además, si tenemos una variable entera que queremos tratar 
# como una variable categórica, basta con utilizar el operador C() con dicha variable en la fórmula.

# Creamos una variable categórica 
	# ¿el gasto en TV es bajo, medio o alto?
ads['TV_budget'] = pd.qcut(ads['TV'], [0, 0.15, 0.85, 1], labels=['LOW','MID','HIGH'])

# Creamos una variable entera
# 0 si hay más gasto en TV que en el resto
# 1 en caso contrario
ads['More_Radio_Or_News'] = ads.apply(lambda x: int(x['TV'] < x['Radio'] + x['Newspaper']), axis="columns")

# Definimos un modelo usando variables categóricas
model_c = smf.ols(formula = 'Sales ~ TV_budget + C(More_Radio_Or_News)', data=ads)
mc_fitted = model_c.fit()
print(mc_fitted.summary())

#                             OLS Regression Results                            
# ==============================================================================================
# Dep. Variable:                  Sales   R-squared:                       0.447
# Model:                            OLS   Adj. R-squared:                  0.438
# Method:                 Least Squares   F-statistic:                     52.79
# Date:                Mon, 20 Oct 2025   Prob (F-statistic):           4.69e-25
# Time:                        10:26:58   Log-Likelihood:                -554.46
# No. Observations:                 200   AIC:                             1117.
# Df Residuals:                     196   BIC:                             1130.
# Df Model:                           3                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================================
#                                  coef    std err          t      P>|t|      [0.025      0.975]
# ----------------------------------------------------------------------------------------------
# Intercept                      8.6897      1.123      7.735      0.000       6.474      10.905
# TV_budget[T.MID]               5.7760      1.104      5.232      0.000       3.599       7.953
# TV_budget[T.HIGH]             10.9270      1.331      8.210      0.000       8.302      13.552
# C(More_Radio_Or_News)[T.1]    -1.7919      1.001     -1.790      0.075      -3.766       0.182
# ==============================================================================================
# Omnibus:                        7.827   Durbin-Watson:                   2.003
# Prob(Omnibus):                  0.020   Jarque-Bera (JB):                7.389
# Skew:                           0.415   Prob(JB):                       0.0249
# Kurtosis:                       2.556   Cond. No.                         9.67
# ==============================================================================================
# Notes: [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


## TRANSFORMACIONES. FUNCIONES Y FORMULAS  ##
# ------------------------------------------------------------------------------------------------------------------------------
# Cuando observemos que existen relaciones no lineales entre variables, podemos embeber funciones para transformar las variables 
# predictoras involucradas en nuestras fórmulas. El intérprete de fórmulas se encargará internamente de aplicar dichas funciones. 
# Los únicos requisitos son que se trate de funciones vectorizadas, preparadas para operar sobre objetos tipo arrays o Series 
# (como las funciones de NumPy); y además que las funciones sean accesibles en el contexto o espacio de nombres actual.

# Definimos un modelo usando la raíz cuadrada del gasto en TV como predictor
model_fn = smf.ols(formula = 'Sales ~ np.sqrt(TV)', data=ads)
mfn_fitted = model_fn.fit()
print(mfn_fitted.summary())

#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                  Sales   R-squared:                       0.623
# Model:                            OLS   Adj. R-squared:                  0.621
# Method:                 Least Squares   F-statistic:                     327.1
# Date:                Mon, 20 Oct 2025   Prob (F-statistic):           8.39e-44
# Time:                        10:35:47   Log-Likelihood:                -516.16
# No. Observations:                 200   AIC:                             1036.
# Df Residuals:                     198   BIC:                             1043.
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ===============================================================================
#                   coef    std err          t      P>|t|      [0.025      0.975]
# -------------------------------------------------------------------------------
# Intercept       2.6724      0.667      4.004      0.000       1.356       3.989
# np.sqrt(TV)     0.9954      0.055     18.085      0.000       0.887       1.104
# ==============================================================================
# Omnibus:                        0.759   Durbin-Watson:                   2.021
# Prob(Omnibus):                  0.684   Jarque-Bera (JB):                0.863
# Skew:                           0.076   Prob(JB):                        0.649
# Kurtosis:                       2.717   Cond. No.                         35.8
# ==============================================================================
# Notes: [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.


# -------------------------------------------------------------------------------------------------------
# --( 3 )-- CLASIFICACION. REGRESION LOGISTICA --
# -------------------------------------------------------------------------------------------------------
# Otro tipo de problema típico a resolver con modelos estadísticos es el de clasificación. El problema 
# aquí consiste en estimar la categoría más probable a la que pertenece un elemento en función de una serie 
# de características observadas, que utilizamos como variables explicativas del modelo.

# Existen varias técnicas de clasificación estadística. Pero ahora vamos a centrarnos en la regresión logística. 
# Statsmodels incluye métodos y utilizades específicas para regresión logística. La interfaz principal es sm.Logit(). 
# Como vas a ver, su uso no puede ser más sencillo.

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
body = pd.read_csv("/workspaces/First-Repository/U09_datasets/body_measures_subset.csv", delimiter=";")
# Los datos contienen varias medidas antropométricas
# `Gender` es una variable categórica
#  - 0 : mujer
#  - 1 : hombre
print(body.head())

# | Position | Gender | Ankle_min_girth | Wrist_min_girth | Height | Weight | Chest_depth | Biacromial_diameter |
# |----------|--------|-----------------|-----------------|--------|--------|-------------|---------------------|
# |        0 |      1 |           23.5  |           16.5  |  174.0 |   65.6 |        17.7 |                42.9 |
# |        1 |      1 |           24.5  |           17.0  |  175.3 |   71.8 |        16.9 |                43.7 |
# |        2 |      1 |           21.9  |           16.9  |  193.5 |   80.7 |        20.9 |                40.1 |
# |        3 |      1 |           23.0  |           16.6  |  186.5 |   72.6 |        18.4 |                44.3 |
# |        4 |      1 |           24.4  |           18.0  |  187.2 |   78.8 |        21.5 |                42.5 |

# Variable respuesta
y = body['Gender']

# Las variables predictoras son todas las demás
X = body.iloc[:,1:]

# Añadimos el término constante
X = sm.add_constant(X, prepend=False)

# Construimos el modelo logístico
model = sm.Logit(y, X)

# Y ajustamos
mfitted = model.fit()

# Examinamos los resultados del ajuste
print(mfitted.summary())

# Optimization terminated successfully.
#          Current function value: 0.154336
#          Iterations 9
#                            Logit Regression Results                           
# ==============================================================================
# Dep. Variable:                 Gender   No. Observations:                  507
# Model:                          Logit   Df Residuals:                      500
# Method:                           MLE   Df Model:                            6
# Date:                Mon, 20 Oct 2025   Pseudo R-squ.:                  0.7772
# Time:                        10:46:17   Log-Likelihood:                -78.248
# converged:                       True   LL-Null:                       -351.26
# Covariance Type:            nonrobust   LLR p-value:                1.018e-114
# =======================================================================================
#                           coef    std err          z      P>|z|      [0.025      0.975]
# ---------------------------------------------------------------------------------------
# Ankle_min_girth        -0.4816      0.235     -2.050      0.040      -0.942      -0.021
# Wrist_min_girth         2.6984      0.444      6.075      0.000       1.828       3.569
# Height                  0.1668      0.040      4.153      0.000       0.088       0.246
# Weight                 -0.1417      0.043     -3.328      0.001      -0.225      -0.058
# Chest_depth             0.5113      0.156      3.271      0.001       0.205       0.818
# Biacromial_diameter     0.6985      0.134      5.194      0.000       0.435       0.962
# const                 -88.4009     10.527     -8.398      0.000    -109.033     -67.769
# =======================================================================================

# Podemos ver la matriz de confusión del ajuste con el método pred_table(). Las filas corresponden 
# a las observaciones (0 y 1) de la variable respuesta, mientras que las columnas corresponden 
# a los valores estimados por el modelo ajustado sobre los datos de entrenamiento. 
# La diagonal recoge los casos correctos.

print(mfitted.pred_table())
# [[246.  14.]
#  [ 16. 231.]]

# Pero naturalmente, lo importante son los resultados sobre datos distintos de los usados para entrenar. 
# Vamos a dividir los datos originales en dos, un conjunto de entrenamiento y otro de test, y procedamos de nuevo.

# Creamos el conjunto de entrenamiento
# tomando aleatoriamente el 80% de filas
body_train = body.copy().sample(frac=0.8)

# El conjunto de test es el formado
# por el resto de filas
body_test = body.copy().drop(body_train.index)

# Variable respuesta
y_train = body_train['Gender']
y_test = body_test['Gender']

# Las variables predictoras son todas las demás
X_train = body_train.iloc[:,1:]
X_test = body_test.iloc[:,1:]

# Añadimos el término constante
X_train = sm.add_constant(X_train, prepend=False)
X_test = sm.add_constant(X_test, prepend=False)

# Construimos el modelo logístico
model = sm.Logit(y_train, X_train)

# Y ajustamos
mfitted = model.fit()

# Optimization terminated successfully.
#         Current function value: 0.144507
#         Iterations 9

# Ahora realizamos la predicción sobre el conjunto de test.

pred = mfitted.predict(X_test)
print(pred.head())

# 0     0.974587
# 2     0.996022
# 3     0.998152
# 14    0.984199
# 17    0.995932
# dtype: float64

# Los valores de la predicción para cada individuo están en el rango [0, 1]. Interpretando 
# los resultados como Prob(y = 1), tomamos que valores (p >= 0.5) corresponden a la categoría 1. 
# Calculemos la tabla de confusión.

pred_0_1 = [ 1 if p >= 0.5 else 0 for p in pred ]
print (pd.crosstab(index=y_test, columns=pd.Categorical(pred_0_1), rownames=['Obs'], colnames=['Pred']))

# Pred   0   1
# Obs         
# 0     48   2
# 1      5  46

# Y, por último, calculemos el acierto global.

acierto_total = np.mean(y_test == pred_0_1)
print ('acierto_total = {0}%'.format(np.round(acierto_total*100, 2))  )
# acierto_total = 92.08%