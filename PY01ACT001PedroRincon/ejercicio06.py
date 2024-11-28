numeros = input("Escribe un numero")
num = 0
for digito in numeros:
    num += int(digito)
print(f"La suma de los digitos del numero {numeros} es {num}")