peso = int(input("Introduce tu peso en Kg"))
altura = float(input("Introduce tu altura"))
altura2 = altura * altura
imc = round(peso/altura2, 2)

print("Tu IMC es " + str(imc))