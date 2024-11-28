palabra = input("Por favor, introduce una palabra: ")

for letra in palabra:
    if letra.lower() == 'h':
        print("Se encontró una 'h'. Deteniendo el programa.")
        break
    print(letra)