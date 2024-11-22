contador = 0
numero = False
letra_minuscula = False
letra_mayuscula = False

def validar_contrasena(contrasena):
    contador = 0
    for caracter in contrasena:
        caracter = str(caracter)
        contador += int(1)
        if(caracter.isdigit):
            numero = True
        
        if caracter in "abcdefghijklmnñopqrstuvwxyz":
            letra_minuscula = True

        if caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            letra_mayuscula = True


    if contador >= 12:
        if numero == True:
            if letra_minuscula == True:
                if letra_mayuscula == True:
                    print("La contraseña se ha validado correctamente")
                else:
                    print("La contraseña debe contener mayusculas")
            else:
                print("La contraseña debe contener minusculas")
        else:
            print("La contraseña debe contener numeros")
    else:
        print("La contraseña debe contener minimo 12 caracteres")
    

contrasenia = str(input("Introduce la contraseña"))
validar_contrasena(contrasenia)