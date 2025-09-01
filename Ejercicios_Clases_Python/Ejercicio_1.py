entrada = input ("introduzca un número entero positivo por favor")
if not entrada.isdigit():
    print ("El dato introducido no es número. Por favor, vuelva a intentarlo")
else:
    numero = int(entrada)

if numero <= 0:
    print ("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo")

def primo (n):
    if n == 1:
        print("Noes un numero primo")
        return
    for i in range (2, n):
        if n % i == 0:
            print ("No es primo")
            return
    
    print("Es primo") 