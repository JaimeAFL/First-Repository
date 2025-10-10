# ---------------------------------------------------------------
# Partida de dados al mejor de 5 (gana quien llega a 3 victorias)
# ---------------------------------------------------------------
# Regla de la ronda:
# - Cada jugador tira 2 dados (1 - 6).
# - Si ALGUNO de los dados del Jugador 1 coincide con ALGUNO del Jugador 2,
#   gana la ronda el Jugador 1. En caso contrario gana el Jugador 2.
# Estructura:
# - partida(): ejecuta una partida completa hasta 3 victorias.
# - Bucle principal: pregunta si seguir jugando y valida la respuesta.

import random

def partida():
    """Juega rondas hasta que un jugador alcance 3 victorias y muestra el ganador."""
    victorias_jugador_1 = 0
    victorias_jugador_2 = 0

    # Repetir rondas mientras ninguno haya llegado a 3
    while victorias_jugador_1 < 3 and victorias_jugador_2 < 3:
        # Tiradas independientes de 2 dados por jugador
        j1_d1 = random.randint(1, 6)
        j1_d2 = random.randint(1, 6)
        j2_d1 = random.randint(1, 6)
        j2_d2 = random.randint(1, 6)

        # Condición de victoria de la ronda:
        # Jugador 1 gana si hay cualquier coincidencia entre sus dados y los del Jugador 2
        if j1_d1 == j2_d1 or j1_d1 == j2_d2 or j1_d2 == j2_d1 or j1_d2 == j2_d2:
            victorias_jugador_1 += 1
            print("Ha ganado jugador 1")
        else:
            victorias_jugador_2 += 1
            print("Ha ganado jugador 2")
    
        # Mostrar tiradas de la ronda para trazabilidad
        print("Jugador 1:", j1_d1, ",", j1_d2, "| Jugador 2:", j2_d1, ",", j2_d2)

    # Fin de partida: anunciar quién alcanzó 3 primero
    if victorias_jugador_1 == 3:
        print("¡Enhorabuena, Jugador 1 gana la partida!")
    else:
        print("¡Enhorabuena, Jugador 2 gana la partida!")

# Bucle de repetición de partidas con validación de entrada
respuesta = "SI"
while respuesta == "SI":
    partida()
    # strip() limpia espacios; se espera SI/NO en mayúsculas
    respuesta = input("¿Desea seguir jugando? SI/NO: ").strip()
    # Validación estricta: solo aceptar "SI" o "NO"
    while respuesta not in ("SI", "NO"):
        respuesta = input("Por favor, responda en mayúsculas SI o NO: ").strip()
