cantidad_numeros = int(input("¿Cuántos números quieres sumar? "))
suma_total = 0

for i in range(cantidad_numeros):
    numero = float(input(f"Introduce el número {i + 1}: "))
    suma_total += numero  


print(f"La suma total es: {suma_total}")