productos = {"Camiseta": 15,"Pantalón": 25,"Zapatos": 30,"Gorra": 10,"Cinturón": 20}
valor = float(input("Introduce un precio: "))

for producto, precio in productos.items():
    if precio <= valor:
        print(f"El {producto} cuesta {precio}€.")

print("------")

for key in productos.keys():
    precio = productos[key]
    if precio <= valor:
         print(f"El {key} cuesta {precio}€.")