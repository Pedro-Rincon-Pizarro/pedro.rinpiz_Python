num_multiplos = 0

while True:
    numero = int(input("Introduce un número múltiplo de 5: "))
    
    if numero % 5 == 0:
        num_multiplos += 1
    else:
        print("El número no es múltiplo de 5. Inténtalo de nuevo.")
        continue

    continuar = input("¿Quieres introducir otro número? (escribe NO o N para salir): ").strip().lower()
    
    if continuar == "no" or continuar == "n":
        break

print(f"Has escrito {num_multiplos} números múltiplos de 5.")
