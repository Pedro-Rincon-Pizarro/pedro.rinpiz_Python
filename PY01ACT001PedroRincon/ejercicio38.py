import random

def tirar_dado(caras):
    """Simula tirar un dado con un número específico de caras."""
    return random.randint(1, caras)

def elegir_dado():
    """Permite al jugador elegir el dado que quiere usar."""
    while True:
        try:
            eleccion = int(input("Elige el dado que quieres usar (6, 10 o 20 caras): "))
            if eleccion in [6, 10, 20]:
                return eleccion
            else:
                print("Por favor, elige un dado válido (6, 10 o 20).")
        except ValueError:
            print("Entrada inválida. Introduce un número entero válido.")


acumulado_1 = 0
acumulado_2 = 0
OBJETIVO = 100
ganador = 0
acumulado_ganador = 0
seguir = True
cont = 0

while seguir:
    cont += 1
    print(f"\nRonda {cont}")
    

    eleccion_1 = input("Jugador 1: ¿Quieres continuar? (S/si--N/No): ").lower()
    if eleccion_1 == "s":
        dado_1 = elegir_dado()
        resultado_1 = tirar_dado(dado_1)
        acumulado_1 += resultado_1
        print(f"El jugador 1 ha sacado un {resultado_1} con un dado de {dado_1} caras y lleva {acumulado_1} puntos.")
        if acumulado_1 == OBJETIVO:
            ganador = 1
            acumulado_ganador = acumulado_1
            seguir = False
        elif acumulado_1 > OBJETIVO:
            ganador = 2
            acumulado_ganador = acumulado_2
            seguir = False
    
    if not seguir:
        break


    eleccion_2 = input("Jugador 2: ¿Quieres continuar? (S/si--N/No): ").lower()
    if eleccion_2 == "s":
        dado_2 = elegir_dado()
        resultado_2 = tirar_dado(dado_2)
        acumulado_2 += resultado_2
        print(f"El jugador 2 ha sacado un {resultado_2} con un dado de {dado_2} caras y lleva {acumulado_2} puntos.")
        if acumulado_2 == OBJETIVO:
            ganador = 2
            acumulado_ganador = acumulado_2
            seguir = False
        elif acumulado_2 > OBJETIVO:
            ganador = 1
            acumulado_ganador = acumulado_1
            seguir = False
            
    if eleccion_1 != "s" and eleccion_2 != "s":
        if acumulado_1 > acumulado_2:
            ganador = 1
            acumulado_ganador = acumulado_1
        elif acumulado_2 > acumulado_1:
            ganador = 2
            acumulado_ganador = acumulado_2
        seguir = False

print(f"\nHa ganado el jugador {ganador} con {acumulado_ganador} puntos.")