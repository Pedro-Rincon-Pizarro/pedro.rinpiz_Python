cantidad_numeros = int(input("¿Cuántos números quieres ingresar? "))
numeros = []

for i in range(cantidad_numeros):
    numero = float(input(f"Introduce el número {i + 1}: "))
    numeros.append(numero)


mayor = max(numeros)
menor = min(numeros)
media = round(sum(numeros) / len(numeros), 2)
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print(f"Media aritmética: {media}")
