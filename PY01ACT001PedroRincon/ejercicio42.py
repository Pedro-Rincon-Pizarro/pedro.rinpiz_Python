
"""Escribe una función llamada calcular_promedio_positivo que reciba un número
indeterminado de valores y devuelva su promedio. Para el promedio solo se tendrán en
cuenta números y que sean posiBvos"""

def calcular_promedio_positivo(*args):
    positivos = []
    
    for n in args:
        if str(n).isdigit() and n > 0:
            positivos.append(n)

    promedio = sum(positivos) / len(positivos)
    print(f"el promedio de los numeros positivos introducidos es {promedio}")



calcular_promedio_positivo(10,20,-34,"df",30,10,30,-40)


