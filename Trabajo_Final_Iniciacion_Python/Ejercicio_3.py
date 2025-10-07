import random

def partida():
    victorias_jugador_1 = 0
    victorias_jugador_2 = 0

    while victorias_jugador_1 < 3 and victorias_jugador_2 < 3:

        j1_d1 = random.randint(1,6)
        j1_d2 = random.randint(1,6)
        j2_d1 = random.randint(1,6)
        j2_d2 = random.randint(1,6)

        if j1_d1 == j2_d1 or j1_d1 == j2_d2 or j1_d2 == j2_d1 or j1_d2 == j2_d2:
            victorias_jugador_1 = victorias_jugador_1 + 1
            print ("Ha ganado jugador 1")
        else:
            victorias_jugador_2 = victorias_jugador_2 + 1
            print ("Ha ganado jugador 2")
    
        print ("Jugador 1: ", j1_d1, ",", j1_d2, " | Jugador 2:", j2_d1, ",", j2_d2)

    if victorias_jugador_1 == 3:
        print ("¡Enhorabuena, Jugador 1 gana la partida!")
    else:
        print ("¡Enhorabuena, Jugador 2 gana la partida!")

respuesta = "SI"
while respuesta == "SI":
    partida()
    respuesta = input("¿Desea seguir jugando? SI/NO: ").strip()
    while respuesta not in ("SI", "NO"):
        respuesta = input("por favor, responda en mayúsculas SI o NO: ").strip()