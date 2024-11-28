from ejercicio_35 import tirar_dado

ganador = None
ronda = 1

jugadores = {
    1 : {
        'puntos': 0,
        'pasa': False,
        'nombre': 'Diego',
        'en_juego': True,
    },
    2 : {
        'puntos': 0,
        'pasa': False,
        'nombre': 'Hector',
        'en_juego': True,
    },
    3 : {
        'puntos': 0,
        'pasa': False,
        'nombre': 'Laura',
        'en_juego': True,
    },
}


def ronda_jugador(indice, jugador):
    if not jugador['en_juego']:
        return

    if jugador['nombre'] == '':
        jugador['nombre'] = input(f"Dime el nombre del jugador nº {indice}: ")

    jugador['pasa'] = input(f'\"{jugador['nombre']}\": elige que quieres hacer (pasar o lanzar): ').lower() == 'pasar'

    if jugador['pasa']:
        return

    tirada = tirar_dado(10)
    jugador['puntos'] += tirada

    if jugador['puntos'] == 100:
        global ganador
        ganador = jugador

    jugador['en_juego'] = jugador['puntos'] < 100

    print(f"{jugador['nombre']} ha sacado {tirada} y lleva acumulado {jugador['puntos']} puntos")


def comprobar_puntos():
    global ganador
    if ganador:
        return

    indice = 0
    maximo = 0

    todos_pasan = True

    global jugadores
    for i, jugador in jugadores.items():
        if jugador['en_juego'] and jugador['puntos'] > maximo and jugador['puntos'] <= maximo:
            indice = i
            maximo = jugador['puntos']

        if not jugador['pasa']:
            todos_pasan = False

    if todos_pasan:
        ganador = indice


while not ganador:
    print(f"Ronda nº {ronda}")

    for i, jugador in jugadores.items():
        ronda_jugador(i, jugador)

    comprobar_puntos()
    ronda += 1

    print()

jugador_ganador = jugadores.get(ganador)
if jugador_ganador:
    print(f"El ganador es \"{jugador_ganador['nombre']}\" con {jugador_ganador['puntos']}")
