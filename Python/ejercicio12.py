frase = str(input("Introduce una cadena de texto"))
contador = 0
for char in frase:
    if char in "aeiou":
        contador += 1
print(f"La cantidad de vocales es: {contador}")