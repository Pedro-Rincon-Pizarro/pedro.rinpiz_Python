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

# Solicitar el nombre del contacto al usuario
nombre = input("Ingrese el nombre del contacto: ").strip()

# Verificar si el contacto está en el diccionario
if nombre in contactos:
    print(f"El número de {nombre} es {contactos[nombre]}")
else:
    print(f"El contacto {nombre} no se encuentra.")
    
    # Preguntar si desea añadir un nuevo contacto
    nuevo_numero = input(f"Ingrese el número de teléfono para {nombre} (formato: XXX XXX XXX): ").strip()
    
    # Agregar el nuevo contacto al diccionario
    contactos[nombre] = nuevo_numero
    print(f"Contacto {nombre} añadido con éxito.")
    print(f"El número de {nombre} es {nuevo_numero}.")

# Mostrar todos los contactos ordenados alfabéticamente
print("\nTodos los contactos guardados (ordenados alfabéticamente):")
for nombre, telefono in sorted(contactos.items()):
    print(f"{nombre}: {telefono}")
