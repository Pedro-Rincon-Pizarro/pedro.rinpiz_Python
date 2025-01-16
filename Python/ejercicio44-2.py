"""Escribe una función llamada validar_requeridos que reciba un número
indeterminado de argumentos con nombre (usando **kwargs) y valide si ciertos
campos obligatorios están presentes. La función debe devolver una lista con los fallos
de validación en el siguiente formato: Falta el campo: <obligatorio>"""

def validar_requeridos(**kwargs):

    obligatorios = ["nombre", "email", "telefono"]

    for campo in kwargs.keys():
        if campo in obligatorios:
            obligatorios.remove(campo)

    if len(obligatorios) == 0 :
        return "Campos correctos"
    else:
        print(f"Campos obligatorios {obligatorios}")

print(validar_requeridos(nombre = "cualquiera", email = "gmail" ))