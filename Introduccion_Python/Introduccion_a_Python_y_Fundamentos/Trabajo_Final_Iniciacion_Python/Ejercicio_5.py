# -----------------------
# La ruleta de la suerte:
# -----------------------
# - Genera 15 ganadores (tupla inmutable) con enteros en [0, 100].
# - Pide al usuario un entero validado "a lo ejercicio 1", pero aquí se admite 0.
# - Muestra ganadores, mínimo y máximo.
# - Si el número del usuario está en los ganadores: calcula premio y termina el programa.
# - Si no está: pregunta SI/NO para volver a intentar.

import random

# Devuelve una tupla inmutable con 15 enteros aleatorios en [0, 100].
def generar_tupla_ganadora():
    lista_tupla = []
    for _ in range(15):
        lista_tupla.append(random.randint(0, 100))
    return tuple(lista_tupla)

def preguntar_entero_no_negativo():
    """Pide un entero NO NEGATIVO en [0, 100], validado igual que en el ejercicio 1:"""
    
    while True:
        datos = input("Introduzca un número entero entre 0 y 100: ").strip()

        # 1) ¿Es número?
        try:
            x = float(datos)
        except ValueError:
            print("El dato introducido no es un número. Por favor, vuelva a intentarlo.")
            continue

        # 2) ¿Es entero?
        if not x.is_integer():
            print("El dato introducido no es un número entero. Por favor, vuelva a intentarlo.")
            continue

        n = int(x)

        # 3) ¿Está en el rango permitido [0, 100]? También permite discriminar números negativos
        if not (0 <= n <= 100):
            print("No ha introducido un entero entre 0 y 100. Por favor, vuelva a intentarlo.")
            continue

        return n

# Devuelve True si el usuario responde SI, False si responde NO. Repite en caso contrario.
def preguntar_si_no():
    while True:
        pregunta = input("¿Dispone de otro número? SI/NO: ").strip().upper()
        if pregunta == "SI": return True
        if pregunta == "NO": return False
        print("No hemos logrado entender su respuesta. Repítala, por favor.")

# Fija el conjunto de ganadores para toda la sesión.
ganadores = generar_tupla_ganadora()

# Bucle principal del juego.
while True:
    n = preguntar_entero_no_negativo()

    # Transparencia de resultados.
    print("Números ganadores:", ganadores)
    print("Mínimo ganador:", min(ganadores), "| Máximo ganador:", max(ganadores))

    # Cuenta cuántas veces aparece el número del usuario.
    veces = ganadores.count(n)

    if veces == 0:
        # Sin premio: ofrecer repetir.
        print("Lo sentimos. Su número no ha resultado premiado.")
        if preguntar_si_no():
            continue
        else:
            break
    else:
        # Con premio: 15 € por la primera aparición + 5 € por cada repetición extra.
        premio = 15 + 5 * (veces - 1)
        if veces == 1:
            print(f"¡Felicidades! Su número {n} se encuentra dentro de la lista de ganadores. "
                  f"Ha ganado un total de {premio} €")
        else:
            print(f"¡Felicidades! Su número {n} se encuentra dentro de la lista de ganadores "
                  f"y además se ha repetido {veces} veces. Ha ganado un total de {premio} €")
        break  # Terminar inmediatamente cuando el número está premiado
