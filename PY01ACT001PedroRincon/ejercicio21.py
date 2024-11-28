capit_inicial = int(input("Introduce la cantidad de capital inicial"))
tasa_interes = int(input("Introduce la tasa de interés"))
anios = int(input("Introduce la cantidad de años que vas a ahorrar"))

for anios in range(0, anios):
    capit_inicial = capit_inicial * (1 + (tasa_interes/100))


print(f"Dentro de {anios + 1} años tendrás {round(capit_inicial,2)}€")