while True:
    entrada = input("Introduce un número (o '*' para detenerse): ")
    if entrada == '*':
        print("Fin del programa.")
        break

    try:
        numero = float(entrada)
        if numero > 0:
            print("Número positivo.")
        elif numero == 0:
            print("Igual a 0.")
        else:
            print("Número negativo.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número o '*' para salir.")
