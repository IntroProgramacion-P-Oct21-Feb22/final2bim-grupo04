def main():
    bandera = True
    contador = 0
    while bandera:
        num = int(input("Ingrese el 1 para crear cuenta             de              Facebook\nIngrese el 2 para crear "
                        "cuenta de twitter\nIngrese el 3 para crear cuenta de Whatsapp\nIngrese el 4 para crear "
                        "cuenta de Telegram\nIngrese el 5 para crear cuenta de Signal\nIngrese el 6 para crear "
                        "cuenta de Instagram\nIngrese el 7 para crear cuenta de Flickr\nIngrese 0 para dejar de crear cuentas\n"))
        if num == 1:
            print(crearFacebook())
        elif num == 2:
            crearTwitter()
        elif num == 3:
            print(crearWhatsapp())
        elif num == 4:
            crearTelegram()
        elif num == 5:
            print(crearSignal())
        elif num == 6:
            crearInstagram()
        elif num == 7:
            print(crearFlickr())
        elif (num == 0 or num <0 or num >7):
            bandera= False
            print("Proceso de creacion de cuentas finalizado")
        if 1 <= num <= 7:
            contador = contador + 1

    cadena = "\nNumero de cuentas creadas: %d --- %s\n" % (contador,obtenerMensaje(contador))
    print(cadena)

def crearFacebook():
    nombre=str(input(f"Creando Facebook\nIngrese el nombre del usuario: "))
    edad=str(input("Ingrese la edad del usuario: "))
    ciudad=str(input("Ingrese la ciudad donde reside el usuario: "))
    pais=str(input("Ingrse el pais donde reside el usuario: "))
<<<<<<< HEAD
    correo=str(input("Ingrese el correo electrónico del usuario: "))

    cadena=str("")
    cadena=("%sResumen de cuenta creada:\nUsuario: %s\nEdad: %s\nCiudad de residencia:%s\n"
            "Pais de residencia: %s\nCorreo electrónico: %s\n" %(cadena,nombre, edad, ciudad, pais, correo))
=======
    correo=str(input("ingrese el correo electrónico del usuario: "))

    cadena=str("")
    cadena=(f"{cadena}Resumen de cuenta creada:\nCreando Facebook\nUsuario: {nombre}\nEdad: {edad}\n"
            f"Ciudad de residencia:{ciudad}"f"\nPais de residencia: {pais}\n"
            f"Correo electrónico: {correo}")
>>>>>>> b98d7ee591f3def92ded3160efde5e4b7ba9cad8
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
<<<<<<< HEAD
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nNombres: %s\nApellidos: %s"
              " Edad: %s\nCiudad de residencia:%s\nPais de residencia: %s\nIdioma: %s"
              "Correo electrónico: %s\n" %(cadena, nombreU, nombres, apellidos, edad, ciudad, pais, idioma,correo))
=======
    cadena = (f"{cadena}Resumen de cuenta creada:\nUsuario: {nombreU}\nNombres:{nombres}\nApellidos: {apellidos}"
              f" Edad: {edad}\nCiudad de residencia:{ciudad}\nPais de residencia: {pais}\nIdioma: {idioma}"
              f"Correo electrónico: {correo}\n")
>>>>>>> b98d7ee591f3def92ded3160efde5e4b7ba9cad8
    print(cadena)

def crearWhatsapp():
    nombre=str(input(f"Creando Whatsapp\nIngrese el nombre del usuario: "))
<<<<<<< HEAD
    numero=str(input("Ingrese su numero de telefono: "))
=======
    numeroTelefono=str(input("Ingrese su numero de telefono: "))
>>>>>>> b98d7ee591f3def92ded3160efde5e4b7ba9cad8
    edad=str(input("Ingrese la edad del usuario: "))
    ciudad=str(input("Ingrese la ciudad donde reside el usuario: "))
    pais=str(input("Ingrese el pais donde reside el usuario: "))

    cadena=str("")
<<<<<<< HEAD
    cadena=("%sResumen de cuenta creada:\nUsuario: %s\nNumero de Telefono: %s\n Edad: "
            "%s\nCiudad de residencia:%s\nPais de residencia: %s\n"%(cadena,nombre, numero,edad,ciudad,pais))
    return cadena

def crearTelegram():
    nombreU = str(input(f"Creando Telegram\nIngrese el nombre del usuario: "))
    numero = str(input("Ingrese el número de teléfono del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    hobby = str(input("Ingrese su area de interés: "))


    cadena = str("")
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nNúmero de teléfono: %s\n"
              "Ciudad de residencia:%s\nPais de residencia: %s\nHobby favorito: %s\n"
              %(cadena,nombreU,numero,ciudad,pais,hobby))
    print(cadena)

def crearSignal():
    nombre=str(input(f"Creando Signal\nIngrese el nombre del usuario: "))
    numero=str(input("Ingrese su numero de telefono: "))
    ciudad=str(input("Ingrese la ciudad donde reside el usuario: "))
    pais=str(input("Ingrese el pais donde reside el usuario: "))
    hobby=str(input("Ingrese su hobby preferido: "))

    cadena=str("")
    cadena=("%sResumen de cuenta creada: \nUsuario: %s\nNumero de Telefono: %s\n"
            "Ciudad de residencia:%s\nPais de residencia: %s\nHobby Principal: %s\n"
            %(cadena,nombre,numero, ciudad, pais, hobby))
    return cadena

def crearInstagram():
    nombreU = str(input(f"Creando Instagram\nIngrese el nombre del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    edad = str(input("Ingrese la edad del usuario: "))
    correo = str(input("ingrese el correo electrónico del usuario: "))

    cadena = str("")
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nCiudad de residencia"
              ":%s\nEdad: %s\nCorreo electrónico: %s\n"%(cadena,nombreU,ciudad,edad,correo))
=======
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
>>>>>>> b98d7ee591f3def92ded3160efde5e4b7ba9cad8
    print(cadena)

def crearFlickr():
    nombre=str(input(f"Creando Flickr\nIngrese el nombre del usuario: "))
    correo=str(input("Ingrese su correo: "))

    cadena=str("")
<<<<<<< HEAD
    cadena=("%sResumen de cuenta creada:\nUsuario: %s\nCorreo Electrónico: %s\n"%(cadena,nombre,correo))
    return cadena

def obtenerMensaje(contador):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if (contador >= 1 and contador <= 5):
        print(mensajeFinal[0])
    elif (contador >= 6 and contador <= 15):
        print(mensajeFinal[1])
    elif (contador >= 16):
        print(mensajeFinal[2])

    
def obtenerMensaje(a):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    
    if(a >=1 and a<=5):
        return (mensajeFinal[0])
    elif(a >=6 and a<=15):
        return (mensajeFinal[1])
    elif(a >=16):
        return (mensajeFinal[2])
    

if __name__ == "__main__":
    """"
    Aquí empieza el proceso cuando se ejecuta por consola
    el archivo python run.py
    """
    main()
=======
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

>>>>>>> b98d7ee591f3def92ded3160efde5e4b7ba9cad8
