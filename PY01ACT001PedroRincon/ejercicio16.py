while True:
    respuesta = input('Diga “SI” para continuar: ').strip().lower()
    if respuesta == "si":
        continue
    else:
        print('¡Hasta la vista!')
        break