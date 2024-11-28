def es_palindromo(palabra):
    palabra_invertida = ''

    for letra in palabra:
        palabra_invertida = letra + palabra_invertida

    return palabra == palabra_invertida

entrada = input("Introduzca una palabra: ")
if es_palindromo(entrada):
    print(f"{entrada} es un palíndromo.")
else:
    print(f"{entrada} no es un palíndromo.")