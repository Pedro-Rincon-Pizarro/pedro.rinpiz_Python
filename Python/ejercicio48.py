"""Escribe un programa que barajee una las cartas de una baraja y que reparta 4 cartas a 
cada jugador sacándolas del mazo. Haz que se pueda seleccionar el número de 
jugadores, y que muestre la mano de cada jugador. 
*Usa la función crar_baraja importando ejercicio47.py para poder usar una 
baraja en el programa. """

from ejercicio47 import crear_baraja
import random

baraja = crear_baraja()

temp_lista = list(baraja)

random.shuffle(temp_lista)

baraja_mezcalda = tuple(temp_lista) 

numero_jugadores = int(input("Cuantos jugadores quieres meter "))
contador_cartas = 0

for j in range(0,numero_jugadores):
    print(f"Jugador {j+1}")
    for i in range(contador_cartas,contador_cartas+4):
        print(baraja_mezcalda[i])

    contador_cartas += 4