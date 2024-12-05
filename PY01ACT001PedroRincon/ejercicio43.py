"""Escribe una función llamada obtener_datos_tipo que reciba un número
indeterminado de valores y devuelva un diccionario las siguientes claves: números,
cadenas, listas y tuplas. No deberá mostrar elementos que no encajen con los Bpos de
las claves"""

def obtener_datos_tipo(*args):
    diccionario = {
        "numeros" : [],
        "cadenas" : [],
        "listas" : [],
        "tuplas" : []
    }
    
    for n in args:
        if isinstance(n, (int, float)):
            diccionario["numeros"].append(n)
            
        if isinstance(n, str):
            diccionario["cadenas"].append(n)
            
        if isinstance(n, list):
            diccionario["listas"].append(n)
            
        if isinstance(n, tuple):
            diccionario["tuplas"].append(n)
            
    return diccionario

print(obtener_datos_tipo(12,18,-8,0,"asda", "asdad", 2.23, ["sdafas", 23, 345.5], (2323, "asddfa" , 23.5)))