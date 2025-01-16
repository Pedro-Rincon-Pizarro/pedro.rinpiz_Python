"""Crea un programa que permita al usuario gesBonar una lista con productos para
comprar. El programa pedirá un numero para ejecutar una acción al usuario hasta que
este decida salir del programa, las acciones son las siguientes:
1. Añadir un producto a la lista.
2. Eliminar un producto de la lista.
3. Mostrar todos los productos de la lista (alfabéBcamente).
4. Salir del programa.
El programa debe informar de la acción seleccionada e informar cuando no hay acción
disponible cuando indica un numero invalido"""


eleccion = 0
productos = []
while True:
    print()
    print("1. Añadir un producto a la lista.")
    print("2. Eliminar un producto de la lista.")
    print("3. Mostrar todos los productos de la lista (alfabéBcamente).")
    print("4. Salir del programa.")
    print(eleccion)
    eleccion = input("Elige una opcion: ")
    print()
    if eleccion not in "1234":
        print("Error! Introduce una opcion valida")
        print()
        
    elif eleccion in "1":
        producto = str(input("introduce el nombre del producto a añadir: "))
        productos.append(producto)
        
    elif eleccion in "2":
        producto = str(input("introduce el nombre del producto a eliminar: "))
        productos.remove(producto)
        
    elif eleccion in "3":
        print(sorted(productos))
        
    elif eleccion in "4":
        print("Saliendo del programa")
        break