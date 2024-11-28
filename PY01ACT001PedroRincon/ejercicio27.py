numero = int(input("Introduce un número entero mayor que cero: "))

if numero <= 0:
    print("El número debe ser mayor que cero.")
else:
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    print(f"Los divisores de {numero} son: {divisores}")
