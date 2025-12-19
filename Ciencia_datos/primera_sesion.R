# Para poner comentarios en el código se utiliza #
# El intérprete de R ignora todo aquello precedido del símbolo #
# La utilidad más sencilla de R es como calculadora
5+7
23*54
2^5
sqrt(3)
log(2)

# La estructura más sencilla de datos es un vector numérico
# Podemos crear un vector como

x <- c(1,2,5,7)
x

# o como una secuencia ordenada de números
y<-1:4
y

# O a partir de un generador de números aleatorios
z<-runif(4,0,10)
z

# Puedo redondear estos números 
z<-round(z,0)

#  Las operaciones en R son vectoriales, en el sentido de que se realizan por defecto elemento a elemento

x+y
x-y
x*y
z^x

# Veamos un ejemplo más complejo
# Generamos un vector con los números del 1 a 100
# Observemos que  como operado de asignación R utiliza <-

x<-1:100
# Mostramos un valor
x[7]
#Mostremos los 5 primeros valores de x
x[1:5]

# Generemos una variable y, relacionada linealmente con x, y con residuos aleatorios distribuidos según una distribución normal
y<- 3*x -12
# Generemos un vector con números aleatorios distribuidos normalmente con media 0 y desviacion típica 20
z<- rnorm(100,mean=0,sd=20)
# Añadimos el error aleatorio a la variable y
y<- y+z
# Representemos la variable y frente a la x en un gráfico de dispersión
plot(x,y)
# Algo más bonito
plot(x,y,pch=19,col="red",cex=0.5,main="x vs y")

# Construimos una tabla de datos (data.frame) que contenga a x e y
df <- data.frame(x,y)
# Mostremos su contenido
View(df)
# Añadimos una nueva columna al data.frame que represente una categoría a la que pertenecen las observaciones
# Hacemos un muestreo aleatorio de 100 extracciones de dos posibles bolas "a" y "b"
cat <- factor(sample(c("a","b"),100,replace = TRUE))
cat
#Añado la columna
df <- cbind(df,cat)
# Plot coloreado según la categoría de los puntos
plot(df$x,df$y,pch=19,col=df$cat,cex=0.5,main="x vs y")

# Ajustemos los puntos a modelo lineal Y=a + b*X + eps
# Los coeficientes ajustados a y b deberian corresponder con los que hemos usado en la generación de los puntos
# a=-12 ; b=3

mod <- lm(y ~ x ,data=df)
?lm
mod
summary(mod)
str(mod)

# dibujamos la recta ajustada
plot(df$x,df$y,pch=19,col="red",cex=0.5)
abline(a=mod$coefficients[1],b=mod$coefficients[2])

# Lectura de ficheros
#setwd("~/Dropbox/MasterD/CursoBigData/")
fdata <- read.table(file="Datasets/SP1_1617_red.csv",
                    sep=",",header = TRUE)
# Primeras lineas
head(fdata)
View(fdata)

# Guardar un objeto de R

save(fdata, file = "fdata.Rdata")
rm(fdata)
load("fdata.Rdata")

# Cargar paquetes

#install.packages("ggplot2")

library(ggplot2)

ggplot(fdata) + geom_boxplot(aes(HomeTeam,FTHG))

ggplot(df) + geom_point(aes(x,y,color=cat)) + geom_smooth(aes(x,y,color=cat),method="lm",se=FALSE)

ggplot(df) + geom_point(aes(x,y)) + geom_smooth(aes(x,y),method="lm") + facet_wrap(~ cat)

