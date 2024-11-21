def convertir_distancia(centimetros):
    kilometros = centimetros // 100000
    metros = (centimetros % 100000) // 100
    centimetros_resto = centimetros % 100

    return kilometros, metros, centimetros_resto


distancia_cm = int(input("Introduce la distancia en centímetros: "))
kilometros, metros, centimetros = convertir_distancia(distancia_cm)
print(f"{distancia_cm} centímetros son {kilometros} km, {metros} m y {centimetros} cm.")
