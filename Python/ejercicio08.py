
estudiantes = (("José", 5), ("Ana", 8), ("Luis", 6), ("María", 9),("Pedro", 4))

for estudiante, nota in estudiantes:
    if nota >= 5:
        print(f"El estudiante {estudiante} ha aprobado con un {nota}.")

for est in estudiantes:
    if(estudiante[1] >=5):
        print(f"El estudiante {est} ha aprobado con un {estudiante[1]}.")
