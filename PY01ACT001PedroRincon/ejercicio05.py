peso = int(input("Introduce tu peso en Kg"))
altura = float(input("Introduce tu altura"))
altura2 = altura ** 2
imc = round(peso/altura2, 2)

print("Tu IMC es " + str(imc))

if(imc >= 40):
    print("Obesidad tipo III")
elif(imc >= 35):
    print("Obesidad tipo II")
elif(imc >= 30):
    print("Obesidad tipo I")
elif(imc >= 25):
    print("Sobrepeso")
elif(imc >= 18,5):
    print("Peso normal")
else:
    print("Peso bajo")