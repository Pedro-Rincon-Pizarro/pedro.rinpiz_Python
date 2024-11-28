import random

def jugar_ronda():
    
    opciones = ["piedra", "papel", "tijera"]
    usuario = input("Elige: piedra, papel o tijera: ").lower()
    while usuario not in opciones:
        print("Elección no válida. Por favor, elige piedra, papel o tijera.")
        usuario = input("Elige: piedra, papel o tijera: ").lower()
    
    maquina = random.choice(opciones)
    print(f"La máquina eligió: {maquina}")

    if usuario == maquina:
        print("¡Es un empate!")
        return 0
    elif (usuario == "piedra" and maquina == "tijera") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijera" and maquina == "papel"):
        print("¡Ganaste esta ronda!")
        return 1
    else:
        print("La máquina ganó esta ronda.")
        return -1

def jugar_partida():
    
    rondas_jugador = 0
    rondas_maquina = 0
    total_rondas = 0

    print("\n¡Comienza la partida al mejor de 5 rondas!")
    while rondas_jugador < 3 and rondas_maquina < 3:
        print(f"\nRonda {total_rondas + 1}")
        resultado = jugar_ronda()
        total_rondas += 1

        if resultado == 1:
            rondas_jugador += 1
        elif resultado == -1:
            rondas_maquina += 1
        
        print(f"Marcador: Jugador {rondas_jugador} - Máquina {rondas_maquina}")
    
    if rondas_jugador > rondas_maquina:
        print("\n🎉 ¡Felicidades! Ganaste la partida.")
    else:
        print("\n🤖 La máquina ganó la partida. ¡Suerte la próxima vez!")

def main():
    
    while True:
        jugar_partida()
        continuar = input("\n¿Quieres jugar otra partida? (S/si para continuar, cualquier otra tecla para salir): ").lower()
        if continuar != "s":
            print("\n¡Gracias por jugar! Hasta luego.")
            break

main()
