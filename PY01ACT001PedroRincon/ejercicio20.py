# Definir el diccionario de contactos
contactos = {
    "Ana": "612 345 678",
    "Luis": "622 987 654",
    "Marta": "635 555 555",
    "Pedro": "645 678 901",
    "Lucía": "655 432 123",
    "Carlos": "699 876 543",
    "Laura": "677 321 890",
    "Javier": "689 234 567"
}


telefono = input("Ingrese el número de teléfono (formato: XXX XXX XXX): ").strip()


contacto_encontrado = False
for nombre, num in contactos.items():
    if num == telefono:
        contacto_encontrado = nombre
        break


if contacto_encontrado:
    print(f"El número {telefono} pertenece a {contacto_encontrado}.")
else:
    print(f"El número {telefono} no está registrado.")