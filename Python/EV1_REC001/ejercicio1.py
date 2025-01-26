def dibujar_rectangulo(caracter, ancho, largo):
    if ancho or largo > 0:
        for i in range(largo):
            for j in range(ancho):
                print(caracter, end='')

            print()
    else:
        print("error, el numero debe ser mayor a 0")
        


dibujar_rectangulo('*', 5, 6)