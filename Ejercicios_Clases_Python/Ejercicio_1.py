def primo (n):
    if n == 1:
        print("Noes un numero primo")
        return
    for i in range (2, n):
        if n % i == 0:
            print ("No es primo")
            return
    
    print("Es primo") 

while True:
    entrada = input("Introduce un número entero positivo: ")

    if not any(c.isdigit() for c in entrada):
        print("El dato introducido no es número. Por favor, vuelva a intentarlo")
        continue

    if not (entrada.isdigit() or (entrada.startswith('-') and entrada[1:].isdigit())):
        print("No ha introducido un número entero. Por favor, vuelva a intentarlo")
        continue

    numero = int(entrada)
    if numero <= 0:
        print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo")
        continue

    primo(numero)
    break