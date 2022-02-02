"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""

def crearFacebook():
    nombre=str(input(f"Creando Facebook\nIngrese el nombre del usuario: "))
    edad=str(input("Ingrese la edad del usuario: "))
    ciudad=str(input("Ingrese la ciudad donde reside el usuario: "))
    pais=str(input("Ingrse el pais donde reside el usuario: "))
    correo=str(input("ingrese el correo electrónico del usuario: "))

    cadena=str("")
    cadena=(f"{cadena}Resumen de cuenta creada:\nCreando Facebook\nUsuario: {nombre}\nEdad: {edad}\n"
            f"Ciudad de residencia:{ciudad}"f"\nPais de residencia: {pais}\n"
            f"Correo electrónico: {correo}")
    return cadena

def crearTwitter():
    nombreU = str(input(f"Creando Twitter\nIngrese el nombre del usuario: "))
    nombres = str(input("Ingrese sus nombres completos: "))
    apellidos = str(input("Ingrese sus apellidos completos: "))
    edad = str(input("Ingrese la edad del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    idioma = str(input("Ingrese su idioma nativo: "))
    correo = str(input("Ingrese el correo electrónico del usuario: "))

    cadena = str("")
    cadena = (f"{cadena}Resumen de cuenta creada:\nUsuario: {nombreU}\nNombres:{nombres}\nApellidos: {apellidos}"
              f" Edad: {edad}\nCiudad de residencia:{ciudad}\nPais de residencia: {pais}\nIdioma: {idioma}"
              f"Correo electrónico: {correo}\n")
    print(cadena)

def crearWhatsapp():
    nombre=str(input(f"Creando Whatsapp\nIngrese el nombre del usuario: "))
    numeroTelefono=str(input("Ingrese su numero de telefono: "))
    edad=str(input("Ingrese la edad del usuario: "))
    ciudad=str(input("Ingrese la ciudad donde reside el usuario: "))
    pais=str(input("Ingrese el pais donde reside el usuario: "))

    cadena=str("")
    cadena=(f"{cadena}Resumen de cuenta creada:\nUsuario: {nombre}\nNumero de Telefono: {numeroTelefono}\n Edad: "
            f"{edad}\nCiudad de residencia:{ciudad}\nPais de residencia: {pais}\n")
    return cadena

def crearTelegram():
    nombreU = str(input(f"Creando Telegram\nIngrese el nombre del usuario: "))
    numero = str(input("Ingrese el número de teléfono del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    hobby = str(input("Ingrese su area de interés: "))


    cadena = str("")
    cadena = (f"{cadena}Resumen de cuenta creada:\nUsuario: {nombreU}\nNúmero de teléfono: {numero}\n"
              f"Ciudad de residencia:{ciudad}\nPais de residencia: {pais}\nHobby favorito: {hobby}\n")
    print(cadena)

def crearSignal():
    nombre=str(input(f"Creando Signal\nIngrese el nombre del usuario: "))
    numeroTelefono=str(input("Ingrese su numero de telefono: "))
    ciudad=str(input("Ingrese la ciudad donde reside el usuario: "))
    pais=str(input("Ingrese el pais donde reside el usuario: "))
    hobby=str(input("Ingrese su hobby preferido: "))

    cadena=str("")
    cadena=(f"{cadena}Resumen de cuenta creada: \nUsuario: {nombre}\nNumero de Telefono: {numeroTelefono}\n"
            f"Ciudad de residencia:{ciudad}\nPais de residencia: {pais}\nHobby Principal: {hobby}\n")
    return cadena

def crearInstagram():
    nombreU = str(input(f"Creando Instagram\nIngrese el nombre del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    edad = int(input("Ingrese la edad del usuario: "))
    correo = str(input("ingrese el correo electrónico del usuario: "))

    cadena = str("")
    cadena = (f"{cadena}Resumen de cuenta creada:\nUsuario: {nombreU}\nCiudad de residencia"
              f":{ciudad}\nEdad: {edad}\nCorreo electrónico: {correo}\n")
    print(cadena)

def crearFlickr():
    nombre=str(input(f"Creando Flickr\nIngrese el nombre del usuario: "))
    correo=str(input("Ingrese su correo: "))

    cadena=str("")
    cadena=(f"{cadena}Resumen de cuenta creada:\nUsuario: {nombre}\nCorreo Electrónico: {correo}\n")
    return cadena

if __name__ == "__main__":
    bandera= True
    contador= 0
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    while (bandera):

        eleccion = int(input(f"Ingrese 1 si desea crear un cuenta de Facebook\n"
                             f"Ingrese 2 si desea crear un cuenta de Twitter\n"
                             f"Ingrese 3 si desea crear un cuenta de Whatsapp\n"
                             f"Ingrese 4 si desea crear una cuentade Telegram\n"
                             f"Ingrese 5 si desea crear una cuenta de Signal\n"
                             f"Ingrese 6 si desea crear una cuenta de Instagram\n"
                             f"Ingrese 7 si dese crear una cuenta de Flickr\n"
                             f"Ingrese 0 para salir dejar de crear cuentas\n"))

        if (eleccion == 1):
            print(crearFacebook())
        elif(eleccion == 2):
            crearTwitter()
        elif(eleccion == 3):
            print(crearWhatsapp())
        elif(eleccion == 4):
            crearTelegram()
        elif(eleccion == 5):
            print(crearSignal())
        elif(eleccion == 6):
            crearInstagram()
        elif(eleccion == 7):
            print(crearFlickr())
        elif(eleccion<0 or eleccion >7):
            bandera = False
            print("Valores introducidos fuera de rango")
        elif(eleccion == 0):
            bandera = False
            print(f"Proceso de creaccion de cuentas finalizado\nNumero de cuentas creadas: {contador}")
            if(contador >=1 and contador<=5):
                print(mensajeFinal[0])
            elif(contador >=6 and contador<=15):
                print(mensajeFinal[1])
            elif(contador >=16):
                print(mensajeFinal[2])
        contador = contador + 1

