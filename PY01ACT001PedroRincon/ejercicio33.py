dias_por_mes = {
    'Enero': 31,
    'Febrero': 28,
    'Marzo': 31,
    'Abril': 30,
    'Mayo': 31,
    'Junio': 30,
    'Julio': 31,
    'Agosto': 31,
    'Septiembre': 30,
    'Octubre': 31,
    'Noviembre': 30,
    'Diciembre': 31,
}

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    return False

def dias_en_mes(mes, año):
    if mes == 'Febrero' and es_bisiesto(año):
        return 29
    return dias_por_mes.get(mes, 0)

def fecha_valida(dia, mes, año):
    if mes in dias_por_mes:
        if 1 <= dia <= dias_en_mes(mes, año):
            return True
    return False

año = int(input("Introduce un año para verificar si es bisiesto: "))
print(f"El año {año} {'es bisiesto' if es_bisiesto(año) else 'no es bisiesto'}.")

mes = input("Introduce un mes (nombre completo, por ejemplo 'Enero'): ")
dias = dias_en_mes(mes, año)
print(f"{mes} tiene {dias} días.")

dia = int(input("Introduce un día: "))
mes = input("Introduce un mes (nombre completo, por ejemplo 'Enero'): ")
año = int(input("Introduce un año: "))
print(f"La fecha {dia} de {mes} de {año} {'es válida' if fecha_valida(dia, mes, año) else 'no es válida'}.")