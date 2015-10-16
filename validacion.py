

def validacion(usuario):
    tam = len(usuario)
    if tam < 12:
        if tam > 5:
            if usuario.isalnum():
                print ("True")
                return True
            else:
                print("El nombre de usuario solo puede contener letras y números")
                return False
        else:
            print("El nombre de usuario debe contener al menos 6 caracteres.")
            return False
    else:
        print("El nombre de usuario no puede contener mas de 12 caracteres.")
        return False


def validacioncon(contra):
    tam = len(contra)
    minusculas = 0
    mayusculas = 0
    numeros = 0
    if tam > 7:
        for letra in range(0, tam):
            if contra[letra].islower():
                minusculas += 1
            elif contra[letra].isupper():
                mayusculas += 1
            elif contra[letra].isdigit():
                numeros += 1
            elif contra[letra].isspace():
                print("La contraseña no puede tener espacios en blanco")
                return False
        if minusculas == 0 or mayusculas == 0 or numeros == 0:
            print("La contraseña no es segura")
            return False
        else:
            print ("True")
            return True
    else:
        print("La contraseña debe contener al menos 8 caracteres.")
        return False


try:
    usuario = input("Usuario: ")
    valida = validacion(usuario)
    while valida is False:
        try:
            usuario = input("Usuario: ")
            valida = validacion(usuario)
        except (EOFError, KeyboardInterrupt):
            print("Error")

    contra = input("Contraseña: ")
    validacon = validacioncon(contra)
    while validacon is False:
        try:
            contra = input("Contraseña: ")
            validacon = validacioncon(contra)
        except (EOFError, KeyboardInterrupt):
            print("Error")


except (EOFError, KeyboardInterrupt):
    print("Error")