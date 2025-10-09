import random

def generar_tupla_ganadora():
    lista_tupla = []

    for _ in range (15):
        lista_tupla.append(random.randint(0,100))
    return tuple(lista_tupla)

def preguntar_numero_positivo():
    while True:
        datos = input("Introduzca un número entero positivo: ").strip()
        try:
            numeros = int(datos)
        except ValueError:
            print("El dato introducido no es número. Por favor, vuelva a intentarlo.")
            continue

        if not (1 <= n <= 100):
            print("No ha introducido un número entero positivo entre el 0 y el 100." \
            "Por favor, vuelva a intentarlo.")
            continue

        return numeros

def preguntar_si_no ():
    while True:
        pregunta = input("¿Desea seguir jugando? SI/NO: ").strip().upper()
        if pregunta == "SI": return True
        if pregunta == "NO": return False
        print("No hemos entendido su respuesta. Por favor vuelva a introducirla")

## LA RULETA DE LA SUERTE ##

ganadores = generar_tupla_ganadora()

while True:
    n = preguntar_numero_positivo()
    print("Números ganadores: ", ganadores)
    print("Mínimo ganador: ", min(ganadores), " | Máximo ganador: ", max(ganadores))

    veces = ganadores.count(n)

    if veces == 0:
        print("Lo sentimos. Su número no es el premiado")
        if preguntar_si_no():
            continue
        else:
            break
    else:
        premio = 15 + 5 * (veces - 1)
    if veces == 1:
        print(f"¡Felicidades! Su número {n} se encuentra dentro de la lista de ganadores. "
        f"Ha ganado un total de {premio} €.")
    else:
        print(f"¡Felicidades! Su número {n} se encuentra dentro de la lista de ganadores "
        f"y además se ha repetido {veces} veces. Ha ganado un total de {premio} €.")