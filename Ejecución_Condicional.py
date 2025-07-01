
##EJECUCIÓN CONDICIONAL##
#nos permite decidir si ejecutamos o no una operación
precio_chaqueta = 59.95
precio_abrigo = 140
dinero_disponible = 100
print ( "Tengo {} euros.".format(dinero_disponible))

#Comprobamos la condicion
if precio_abrigo <= dinero_disponible:
    #Si es cierta, ejecutamos este bloque (1) de instrucciones
    print("El abrigo cuesta menos de {} euros".format(dinero_disponible))
    #este bloque termina aquí
print("Voy a seguir mirando")

#Comprobamos otra condicion
if precio_chaqueta <= dinero_disponible:
    print("La chaqueta cuesta menos de {} euros".format(dinero_disponible))
print("Ya no miro más")

# bloque de elif

if precio_abrigo <= dinero_disponible:
    print("Mevoy a comprar el abrigo")
elif precio_chaqueta <= dinero_disponible:
    print("Me voy a comprar la chaqueta")
else:
    print("Me voy con las manos vacías")

#AHORA EMPEZAMOS BUCLES#

#BUCLE WHILE
i = 1
suma = 0
while i <= 10:
    suma += i
    i = i + 1
print("La suma de los 10 primeros números naturales vale", suma)

#BUCLES FOR
#definimos lista
lista_frutas = ["pera","manzana","ciruela","cereza"]
for fruta in lista_frutas:
    print(fruta)

#bucle FOR con función RANGE
suma = 0
for i in range (1,10):
    print(i)
    suma += i
print(suma)

#ejemplos función RANGE
#generamos una secuencia indicando solo el valor de parada
for i in range(5):
    print(str(i)*i)
#generamos una secuencia indicando que el paso debe ir
#de 2 en 2, en lugar de 1 en 1
for j in range (1,10,2):
    print(j)

#BUCLES ANIDADOS

for i in range(1,5):            #bucle exterior
    for j in range(1,i+1):      #bucle interior
        # 'end' indica el carácter a usar al final de la cadena
        print(j,end=" ")
    print()                     #sin argumentos solo imprime un salto de linea

#SENTENCIA BREAK
# sirve para interrumpir la ejecución del bucle más interno en el que se encuentra
# y devolver el flujo fuera del bucle inmmediatamente a la siguiente instrucción

#vamos a calcular qué numeros son primos entre el 10 y 19
for n in range (10,20):         #Bucle externo:iteramos de 10 a 19
    # al inicio, aún no hemos encontrado un divisor de n
    tiene_divisor = False
    #Bucle Interno: numeros entre 2 y (n-1 ¿son divisores de n?
    for d in range (2,n):
        #si d es divisor de n, el resto es cero
        print ("*d=",d)
        if n % d == 0: tiene_divisor = True     #en este caso n no es primo, tiene divisor
        #podemos pasar al siguente numero n (saltar a bucle externo)
        break
    # si no encontramos divisor en el bucle, entonces n es primo
    if not tiene_divisor:
        print("/t>",n, 'es primo')

#tanto el "/t>" como "print ("*d=",d)" se podrán quitar ya que el segundo muestra qué divisores se prueban
# y el primero si la salida de los numeros primos es correcta
