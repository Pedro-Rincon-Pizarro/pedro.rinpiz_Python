numeros = [3, -1, 0, 4, -5, 0, 7, -2]

def clasificar_numeros(numeros):
    # Debe guardar 3 listas, no contar cuantos hay
    positivos = []
    negativos = []
    ceros = []

    for numero in numeros:
        if numero > 0:
            positivos.append(numero)
        if numero < 0:
            negativos.append(numero)
        if numero == 0:
            ceros.append(numero)

    # Tiene que devolver una tupla no imprimir un mensaje
    return (positivos, negativos, ceros)


clasificacion = clasificar_numeros(numeros)
print("Números positivos:", clasificacion[0])
print("Números negativos:", clasificacion[1])
print("Ceros:", clasificacion[2])