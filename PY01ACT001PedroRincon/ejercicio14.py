cantidad = int(input("Introduce una cantidad de segundos"))

horas = int(cantidad//3600)

minutos = int((cantidad%3600)//60)

segundos = int(cantidad%60)

print(f"{cantidad} segundos son {horas} horas, {minutos} minutos y {segundos} segundos")