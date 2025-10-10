# --------------------------------------------------------------
# Verificador de números primos con entrada validada por consola
# --------------------------------------------------------------
# Estructura:
# 1) requested_number(): se encarga de pedir y validar un entero positivo.
# 2) prime_number(n): evalúa si n es primo y devuelve un mensaje descriptivo.
# Mantener I/O o true false separado de la lógica facilita las pruebas y reutilización.

def prime_number(n):
    """ Indica si n es primo devolviendo un texto.
    Supone que n ya es un entero positivo validado. """
    
    # Por definición, 0 y 1 (y negativos) no son primos.
    if n < 2:
        return f"El número {n} no es primo."

    # Búsqueda de divisores: recorre 2..n-1.
    # Si encuentra un divisor exacto, termina temprano y declara no primo.
    # Si no hubo divisores, n es primo.
    for i in range(2, n):
        if n % i == 0:
            return f"El número {n} no es primo."
    return f"El número {n} es primo."

def requested_number():
    """ Solicita un entero positivo por consola.
    Repite hasta recibir un valor correcto y lo devuelve."""

    while True:
        data = input("Introduce un número entero positivo: ")

        # Intento de convertir a int. Si falla, se informa y se reintenta.
        try:
            number = int(data)
        except ValueError:
            print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
            continue

        # Validación de rango: exigimos > 0.
        if number <= 0:
            print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo.")
            continue
        return number

if __name__ == "__main__":
    # secuencia del flujo: pide número validado, evalúa el resultado y muestra salida.
    num = requested_number()
    resultado = prime_number(num)
    print(resultado)