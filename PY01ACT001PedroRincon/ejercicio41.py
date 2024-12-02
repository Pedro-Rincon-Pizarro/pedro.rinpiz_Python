from ejercicio33 import es_bisiesto

anios_no_bisiestos = 0
primer_anio = int(input("Introduce el primer año a comprobar: "))

for anio in range(primer_anio + 1, primer_anio + 4):
    if not es_bisiesto(anio):
        anios_no_bisiestos += 1
    else:
        break



print(f"Desde el año {primer_anio} hasta el proximo año bisiesto faltan {anios_no_bisiestos + 1}")



anio = int(input("Introduce el primer año a comprobar: "))
contador = 1
while not es_bisiesto(anio + contador):
    contador += 1

print(f"Desde el año {anio} hasta el proximo año bisiesto faltan {contador}")