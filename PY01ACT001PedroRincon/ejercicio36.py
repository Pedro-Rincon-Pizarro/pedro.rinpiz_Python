from ejercicio35 import tirar_dado

numero_objetivo = int(input("introduce el numero objetivo"))
acumulado_1 = 0
acumulado_2 = 0

while acumulado_1 < numero_objetivo and acumulado_2 < numero_objetivo:
    dado_1 = tirar_dado()
    acumulado_1 += dado_1
    input(f"El jugador 1 ha sacado un {dado_1} y lleva {acumulado_1}")
    
    dado_2 =  tirar_dado()
    acumulado_2 += dado_2
    input(f"El jugador 2 ha sacado un {dado_2} y lleva {acumulado_2}")


if acumulado_1 > acumulado_2:
    input(f" El jugador 1 ha ganado con {acumulado_1}")
else:
    input(f" El jugador 2 ha ganado con {acumulado_2}")