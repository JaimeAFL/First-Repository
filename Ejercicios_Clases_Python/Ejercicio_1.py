def es_primo(n):
    if n < 2:
        return f"El número {n} no es primo."

    for i in range(2, n):
        if not n % i:   # resto 0 significa que es divisible
            return f"El número {n} no es primo."
    
    return f"El número {n} es primo."


def solicitar_numero():
    while True:
        dato = input("Introduce un número entero positivo: ")
        try:
            numero = int(dato)
        except ValueError:
            print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
            continue

        if numero <= 0:
            print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo.")
            continue

        return numero


if __name__ == "__main__":
    num = solicitar_numero()
    print(es_primo(num))