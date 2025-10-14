# --------------------------------------------------------------
# Verificador de números primos con entrada validada por consola
# --------------------------------------------------------------
# Estructura:
# 1) numero_preguntado(): pide y valida un entero positivo diferenciando:
#    - no número
#    - número no entero
#    - número no positivo
# 2) numero_primo(n): evalúa si n es primo y devuelve un mensaje.

def numero_primo(n):
    """Indica si n es primo devolviendo un texto.
    Supone que n ya es un entero positivo validado."""
    # Por definición, 0 y 1 (y negativos) no son primos.
    if n < 2:
        return f"El número {n} no es primo."
    # Búsqueda de divisores: recorre 2..n-1 y corta al encontrar divisor.
    for i in range(2, n):
        if n % i == 0:
            return f"El número {n} no es primo."
    return f"El número {n} es primo."

def numero_preguntado():
    """Solicita un entero positivo por consola.
    Repite hasta recibir un valor correcto y lo devuelve."""
    while True:
        dato = input("Introduce un número entero positivo: ")

        # 1) ¿Es número? Intento convertir a float.
        try:
            x = float(dato)
        except ValueError:
            print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
            continue

        # 2) ¿Es entero? Comprobación con 'is_integer'.
        if not x.is_integer():
            print("El dato introducido no es un número entero. Por favor, vuelva a intentarlo.")
            continue

        n = int(x)

        # 3) ¿Es positivo? Exigimos > 0.
        if n <= 0:
            print("No ha introducido un número entero positivo. Por favor, vuelva a intentarlo.")
            continue

        return n

if __name__ == "__main__":
    # Flujo principal: pedir número válido, evaluar primalidad y mostrar salida.
    num = numero_preguntado()
    resultado = numero_primo(num)
    print(resultado)
