eleccion = 0
temperatura = 0.0
while True:
    print()
    print("1. Celsius a Fahrenheit.")
    print("2. Fahrenheit a Celsius.")
    print("3. Celsius a Kelvin.")
    print("4. Kelvin a Celsius.")
    print("5. Fahrenheit a Kelvin.")
    print("6. Kelvin a Fahrenheit.")
    print("7. Salir")
    print(eleccion)
    eleccion = input("Elige una opcion: ")
    print()
    if eleccion not in "1234":
        print("Error! Introduce una opcion valida")
        print()
        
    elif eleccion in "1":
        temperatura = float(input("Introduce la temperatura en Celsius: "))
        temperatura_final = (temperatura * 1.8) + 32
        print(f"La temperatura introducida en Celsius equivale a {round(temperatura_final, 2)} grados Fahrenheit")
        
    elif eleccion in "2":
        temperatura = float(input("Introduce la temperatura en Fahrenheit: "))
        temperatura_final = (temperatura - 32) / 1.8
        print(f"La temperatura introducida en Fahrenheit equivale a {round(temperatura_final, 2)} grados Celsius")
        
    elif eleccion in "3":
        temperatura = float(input("Introduce la temperatura en Celsius: "))
        temperatura_final = temperatura + 273.15
        print(f"La temperatura introducida en Celsius equivale a {round(temperatura_final, 2)} grados Kelvin")
        
    elif eleccion in "4":
        temperatura = float(input("Introduce la temperatura en Kelvin: "))
        temperatura_final = temperatura - 273.15
        print(f"La temperatura introducida en Kelvin equivale a {round(temperatura_final, 2)} grados Celsius")
        
    elif eleccion in "5":
        temperatura = float(input("Introduce la temperatura en Fahrenheit: "))
        temperatura_final = (temperatura - 32) / 1.8 + 273.15
        print(f"La temperatura introducida en Fahrenheit equivale a {round(temperatura_final, 2)} grados Kelvin")
        
    elif eleccion in "6":
        temperatura = float(input("Introduce la temperatura en Kelvin: "))
        temperatura_final = (temperatura - 273.15) * 1.8 + 32
        print(f"La temperatura introducida en Kelvin equivale a {round(temperatura_final, 2)} grados Fahrenheit")
        
    elif eleccion in "7":
        print("Saliendo del programa")
        break