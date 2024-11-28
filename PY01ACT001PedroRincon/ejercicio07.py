anio = int(input("Introduce un año"))

divisiblePor4 = (anio % 4 == 0)
divisiblePor100 =(anio % 100 == 0)
divisiblePor400 =(anio % 400 == 0)

if (divisiblePor4 and not divisiblePor100) or divisiblePor400:
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} no es bisiesto")


