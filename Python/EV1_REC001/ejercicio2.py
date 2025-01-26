import random

def simular_tiradas():
    lista = []
    # Hay que inicializar todos los datos que se van a devolver
    primer_6 = False
    primer_1 = False

    # El numero de veces que se tira el dado se debe soicitar a usuario
    numero = int(input('Ingrese un número del 1 al 20: '))

    # No es necesario comprobar los datos (en este ejercicio)
    for i in range(numero):
        tirada = random.randint(1, 6)

        if primer_6 == False and tirada == 6:
            primer_6 = i

        if primer_1 == False and tirada == 1:
            primer_1 = i

        # Antes de guardarlo en la lista debemos hacer el resto de comprobaciones
        lista.append(tirada)

    return (lista, primer_6, primer_1)


print("Resultado: ", simular_tiradas())