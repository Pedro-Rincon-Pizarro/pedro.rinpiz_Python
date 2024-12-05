"""Escribe una función llamada crar_baraja que devuelva una tupla con las 52 cartas de 
la baraja francesa sin comodines. Cada carta debe de ser un diccionario con esta 
estructura: """
"""Los puntos son según las reglas del blackjack o el vein uno simplificadas, por lo que 
cada carta ene los puntos de su valor a excepción de las figuras que valen todas 10 y 
los ases que valen 11. """

def crear_baraja():
    baraja = []
    palos = ["treboles", "diamantes", "picas", "corazones"]
    valores = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10,"J", "Q", "K"]
    for palo in palos:
        for valor in valores:
            if valor in ['J', 'Q', 'K']:
                puntos = 10
            elif valor == 'As':
                puntos = 11
            else:
                puntos = int(valor)
            
            carta = {"palo" : palo,
                     "valor" : valor,
                     "puntos" : puntos}
            baraja.append(carta)
    
    return tuple(baraja)


print(crear_baraja())