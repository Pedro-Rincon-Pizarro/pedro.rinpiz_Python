anchura = int(input("Introduce la anchura del rectángulo: "))
altura = int(input("Introduce la altura del rectángulo: "))

for i in range(altura):
    if i == 0 or i == altura - 1:
        print("*" * anchura)
    else:
        print("*" + " " * (anchura - 2) + "*")
