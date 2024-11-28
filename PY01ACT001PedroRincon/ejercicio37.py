from ejercicio35 import tirar_dado

acumulado_1 = 0
acumulado_2 = 0
OBJETIVO = 100

ganador = 0
acumulado_ganador = 0
seguir = True
cont = 0


    
while (seguir):
    cont += 1
    print(f"\nRonda {cont}")

    eleccion_1 = input("Jugador 1: ¿Quieres continuar?(S/si--N/No)")
    if eleccion_1 == "s":
        dado_1 = tirar_dado(10)
        acumulado_1 += dado_1
        print(f"El jugador 1 ha sacado un {dado_1} y lleva {acumulado_1}")
        if(acumulado_1 == OBJETIVO):
            ganador = 1
            acumulado_ganador = acumulado_1
            seguir = False
        elif acumulado_1 > OBJETIVO:
            ganador = 2
            acumulado_ganador = acumulado_2
            seguir = False
    
    if not seguir:
        break
    

    eleccion_2 = input("Jugador 2: ¿Quieres continuar?(S/si--N/No)")
    if eleccion_2 == "s":
        dado_2 = tirar_dado(10)
        acumulado_2 += dado_2
        print(f"El jugador 2 ha sacado un {dado_2} y lleva {acumulado_2}")
        if(acumulado_2 == OBJETIVO):
            ganador = 2
            acumulado_ganador = acumulado_2
            seguir = False
        elif acumulado_2 > OBJETIVO:
            ganador = 1
            acumulado_ganador = acumulado_1
            seguir = False
            
    if eleccion_1 != "s" and eleccion_2 != "s":
        if(acumulado_1 > acumulado_2):
            ganador = 1
            acumulado_ganador = acumulado_1
            seguir = False
        elif acumulado_2 > acumulado_1:
            ganador = 2
            acumulado_ganador = acumulado_2
            seguir = False
    
print(f"Ha ganado jugador {ganador} con {acumulado_ganador} puntos")
