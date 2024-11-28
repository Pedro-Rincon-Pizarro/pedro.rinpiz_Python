from datetime import datetime


anio = int(input("Introduce un año"))
anioActual = int(datetime.now().year)  
diferencia = int(anioActual - anio)
    
if diferencia == 0:
    print("¡Son el mismo año!")
elif diferencia == 1:
    print(f"Desde el año {anio} ha pasado 1 año.")
elif diferencia > 1:
    print(f"Desde el año {anio} han pasado {diferencia} años.")
elif diferencia == -1:
    print(f"Para llegar al año {anio} falta 1 año.")
else:
    print(f"Para llegar al año {anio} faltan {abs(diferencia)} años.")