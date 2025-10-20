# ---------------------------------------------------------------
# Partida de dados al mejor de 5 (gana quien llega a 3 victorias)
# ---------------------------------------------------------------
# Reglas:
# - Cada jugador lanza 2 dados (1..6).
# - Si ALGUNO de los números se repite entre las 4 tiradas de la ronda
#   (da igual quién lo saque), la ronda es para Jugador1.
# - Si los 4 números son todos distintos, la ronda es para Jugador2.
# Formato de salida por ronda:
#   Jugador1 ha obtenido: a y b
#   Jugador2 ha obtenido: c y d
#   Ganaría la ronda: Jugador1|Jugador2
# Fin de partida: mensaje de enhorabuena al ganador (3 victorias).
# Repetición: preguntar SI/NO y validar.

import random

def partida():
    """Juega rondas hasta 3 victorias y anuncia el ganador de la partida."""
    victorias_j1 = 0
    victorias_j2 = 0

    while victorias_j1 < 3 and victorias_j2 < 3:
        # Tiradas
        j1_d1 = random.randint(1, 6)
        j1_d2 = random.randint(1, 6)
        j2_d1 = random.randint(1, 6)
        j2_d2 = random.randint(1, 6)

        # Mostrar como el formato del ejercicio del PDF
        print(f"Jugador1 ha obtenido: {j1_d1} y {j1_d2}")
        print(f"Jugador2 ha obtenido: {j2_d1} y {j2_d2}")

        # Regla correcta:
        # - Gana J1 si existe CUALQUIER repetición en las 4 tiradas.
        #   Equivalente a: tamaño del conjunto < 4.
        # - Gana J2 si los 4 valores son todos distintos.
        valores = {j1_d1, j1_d2, j2_d1, j2_d2}
        if len(valores) < 4:
            victorias_j1 += 1
            print("Ganaría la ronda: Jugador1")
        else:
            victorias_j2 += 1
            print("Ganaría la ronda: Jugador2")
        
        print() # linea en blanco entre rondas para diferenciarlas 
                # y que sean más legible

    # Mensaje final de partida otorgando victoria al jugador que le toca
    if victorias_j1 == 3:
        print("¡Enhorabuena, Jugador 1 gana la partida!")
    else:
        print("¡Enhorabuena, Jugador 2 gana la partida!")

def pedir_si_no(prompt):
    """Pide SI/NO. Acepta mayúsculas o minúsculas. Repite si no se entiende."""
    while True:
        resp = input(prompt).strip().upper()
        if resp in ("SI", "NO"):
            return resp
        print("No se ha entendido correctamente su respuesta. Por favor, escriba SI o NO.")

# Bucle principal de repeticion de partidas
while True:
    partida()
    if pedir_si_no("¿Desea seguir jugando? SI/NO: ") == "NO":
        break
