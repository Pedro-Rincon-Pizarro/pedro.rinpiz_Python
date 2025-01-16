from ejercicio33 import es_bisiesto

primer_anio = int(input("Introduce el primer año a comprobar: "))
segundo_anio = int(input("Introduce el ultimo año a comprobar: "))

anios_bisiestos = 0
if primer_anio > segundo_anio:
    anio_mayor = primer_anio
    anio_menor = segundo_anio
else:
    anio_menor = primer_anio
    anio_mayor = segundo_anio



for anio in range(anio_menor, anio_mayor + 1):
    if es_bisiesto(anio):
        anios_bisiestos += 1
        
print(f"Entre {primer_anio} y {segundo_anio} hay {anios_bisiestos} años bisiestos")