def prime_number(n):
    if n < 2:
        return f"El número {n} no es primo."

    for i in range(2, n):
        if not n % i:
            return f"El número {n} no es primo."
    
    return f"El número {n} es primo."


def requested_number():
    while True:
        data = input("Introduce un número entero positivo: ")
        try:
            number = int(data)
        except ValueError:
            print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
            continue

        if number <= 0:
            print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo.")
            continue

        return number

if __name__ == "__main__":
    num = requested_number()
    print(prime_number(num))