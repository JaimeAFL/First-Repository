# -----------------------
# La ruleta de la suerte: 
# -----------------------
# generar 15 ganadores y comprobar aciertos
# Validación usa la variable convertida y rango [1, 100].

import random

# Devuelve una tupla inmutable con 15 enteros aleatorios en [0, 100].
# Usar tupla bloquea modificaciones accidentales del conjunto ganador.
def generar_tupla_ganadora():
    lista_tupla = []
    # Genera 15 números al azar.
    for _ in range(15):
        lista_tupla.append(random.randint(0, 100))
    return tuple(lista_tupla)

# Pide un entero válido en [1, 100].
# Reintenta hasta que la entrada sea correcta.
def preguntar_numero_positivo():
    while True:
        datos = input("Introduzca un número entero entre 1 y 100: ").strip()
        try:
            numero = int(datos)
        except ValueError:
            # Entrada no numérica: informar y repetir.
            print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
            continue

        # Validación de rango no excluyente.
        if not (1 <= numero <= 100):
            print("No ha introducido un entero entre 1 y 100. Por favor, vuelva a intentarlo.")
            continue

        # Valor válido listo para usar.
        return numero

# Devuelve True si el usuario responde SI, False si responde NO.
# Cualquier otra respuesta vuelve a preguntar.
def preguntar_si_no():
    while True:
        pregunta = input("¿Desea seguir jugando? SI/NO: ").strip().upper()
        if pregunta == "SI":
            return True
        if pregunta == "NO":
            return False
        print("No hemos entendido su respuesta. Por favor, vuelva a introducirla.")

# Fija el conjunto de ganadores para toda la sesión.
ganadores = generar_tupla_ganadora()

# Bucle principal del juego.
# Pide número, muestra ganadores y mínimo/máximo, evalúa premio y decide continuidad.
while True:
    n = preguntar_numero_positivo()

    # Transparencia de resultados.
    print("Números ganadores: ", ganadores)
    print("Mínimo ganador: ", min(ganadores), " | Máximo ganador: ", max(ganadores))

    # Cuenta cuántas veces aparece el número del usuario.
    veces = ganadores.count(n)

    # Rama sin premio: ofrecer seguir o salir.
    if veces == 0:
        print("Lo sentimos. Su número no es el premiado.")
        if preguntar_si_no():
            continue
        else:
            break
    else:
        # Cálculo del premio: 15 € por la primera aparición + 5 € por cada repetición extra.
        premio = 15 + 5 * (veces - 1)

    # Mensaje según apariciones.
    if veces == 1:
        print(f"¡Felicidades! Su número {n} está en la lista de ganadores. "
            f"Ha ganado un total de {premio} €.")
    else:
        print (f"¡Felicidades! Su número {n} está en la lista de ganadores "
            f"y se ha repetido {veces} veces. Ha ganado un total de {premio} €.")