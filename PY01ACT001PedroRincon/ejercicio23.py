productos = {
"payaso": 112,
"muñeca": 75,
"robot": 250,
"peluche": 180,
"puzzle": 400
}

for producto in productos:
    print(producto)
    
    
producto = input("Introduce el nombre de un producto de la lista")

if producto in productos:
    print(producto)
