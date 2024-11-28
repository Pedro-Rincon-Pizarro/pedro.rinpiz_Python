
palabras = input("Introduce una frase: ").split(" ")

resultados = {}

for palabra in palabras:
    if(palabra not in resultados):
        resultados[palabra] = 1
    else:
        resultados[palabra] += 1
        
        
print(f"Rescuencia de las palabras: {resultados}")