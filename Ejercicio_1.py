def primo(n):
    if n == 1:
        print("No es un número primo")
        return
    for i in range(2, n):
        if n % i == 0:
            print("No es primo")
            return
    print("Es primo")


while True:
    entrada = input("Introduce un número entero positivo: ")
    if not entrada.isdigit():
        print("El dato introducido no es número. Por favor, vuelva a intentarlo")
        continue
    try:
        numero = int(entrada)
    except ValueError:
        print("No ha introducido un número entero. Por favor, vuelva a intentarlo")
    if numero <= 0:
        print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo")
        continue
    primo(numero)
    break
    