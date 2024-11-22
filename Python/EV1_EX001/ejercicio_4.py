numeros = [3, -1, 0, 4, -5, 0, 7, -2]

def clasificar_numeros(numeros):
    positivos = int(0)
    negativos = int(0)
    ceros = int(0)
    for numero in numeros:
        if numero > 0:
            positivos += 1

        if numero < 0:
            negativos += 1
        if numero == 0:
            ceros += 1

    clasificacion = {positivos, negativos, ceros}

    return print(f"Positivos: {positivos}, Negativos: {negativos}, Ceros: {ceros}")


clasificar_numeros(numeros)

