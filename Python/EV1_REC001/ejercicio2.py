import random
def simular_tiradas(numero):
    lista = []
    if numero > 0 and numero <= 20:
        for i in range(numero):
            
            lista.append(random.randint(1,6))
            
    else:
        print("El numero debe ser mayor a 0 y menor a 20")


    for j in lista:
        print(j)


simular_tiradas(5)