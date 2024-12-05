"""Escribe una función llamada imprimir_estructura que reciba un número
indeterminado de argumentos con nombre (usando **kwargs) y los imprima 
ordenados alfabéBcamente por clave mostrando en cada línea la información 
de clave-valor."""

def imprimir_estructura(**kwargs):
     diccionario = {}
     
     for clave, valor in kwargs.items():
         if isinstance(valor, list):
             diccionario[clave] = valor
        
    
     claves_ordenadas = sorted(diccionario)
     diccionario_ordenado = {}
     for clave in claves_ordenadas:
        diccionario_ordenado[clave] = diccionario[clave]
     
     return diccionario_ordenado
 
print(imprimir_estructura(sgsae = [23,"asdfd",32.4], qwesf = [23, 2, 4564], asra = ["asd", "asfa"]))