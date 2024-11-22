def formatear_fecha(fecha):
    fecha_formateada = []
    fecha_separada = str(fecha).split("-")
    for parte in fecha_separada:
        fecha_formateada.append(str(parte))
        fecha_formateada.append("/")
    

    print("Fecha formateada: ")
    for parte in fecha_formateada:
        print(parte, end= "")


fecha_sin_formatear = input("Introduce una fecha en formato AAAA-MM-DD")

formatear_fecha(fecha_sin_formatear)