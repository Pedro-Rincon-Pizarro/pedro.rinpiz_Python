def validar_contrasena(contrasena):
    contador = 0
    
    # Esto debe ir dentro de la función
    numero = False
    letra_minuscula = False
    letra_mayuscula = False

    for caracter in contrasena:
        caracter = str(caracter)
        contador += 1

        if caracter.isdigit(): # Esto es ina función faltaba el parentesis
            numero = True
        
        if caracter in "abcdefghijklmnñopqrstuvwxyz":
            letra_minuscula = True

        if caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            letra_mayuscula = True


    # Todo esto tiene que devolver un mensaje
    # Se puede simplificar MUCHO estas condiciones
    if contador >= 12:
        if numero == True:
            if letra_minuscula == True:
                if letra_mayuscula == True:
                    return "La contraseña es válida" # Texto diferente
                else:
                    return "La contraseña debe contener mayusculas"
            else:
                return "La contraseña debe contener minusculas"
        else:
            return "La contraseña debe contener numeros"
    else:
        return "La contraseña debe contener minimo 12 caracteres"


contrasenia = str(input("Introduce la contraseña: "))
print(validar_contrasena(contrasenia))