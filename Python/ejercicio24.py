productos = {
    "Leche": 10,
    "Pan": 8,
    "Huevos": 20,
    "Queso": 4,
    "Mantequilla": 6
}


for producto, cantidad_disponible in productos.items():

    cantidad_deseada = int(input(f"¿Cuántas unidades de {producto} deseas comprar? "))


    if cantidad_deseada <= cantidad_disponible:

        productos[producto] -= cantidad_deseada

        if productos[producto] == 0:
            print(f"¡Atención! El producto {producto} se ha agotado.")
    else:

        print(f"No hay suficientes unidades de {producto} en inventario. Solo hay {cantidad_disponible} unidades disponibles.")


print("\nInventario final:")
for producto, cantidad in productos.items():
    print(f"{producto}: {cantidad} unidades")