def formatear_fecha(fecha):
    fecha_formateada = []
    fecha_separada = str(fecha).split("-")

    # Te falta reordenar los elementos para que sean DD/MM/AAAA
    for parte in fecha_separada:
        fecha_formateada.append(str(parte))
        fecha_formateada.append("/") # Esto añade uno de más al final
    
    # Tiene que devolver la fecha formateada en string
    resultado = ''
    for parte in fecha_formateada:
        resultado += parte

    return resultado

# No era necesario pedir al usuario
fecha_sin_formatear = input("Introduce una fecha en formato AAAA-MM-DD ")
print("Fecha formateada:", formatear_fecha(fecha_sin_formatear))