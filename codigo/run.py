"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""
contador=int(0)
bandera=True
mensajeFinal=["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
while (bandera):

    eleccion = int(input("Ingrese 1 si desea crear un cuenta de Facebook\nIngrese 2 si desea crear un cuenta de "
                         "Twitter\nIngrese 3 si desea crear un cuenta de Whatsapp\nIngrese 4 si desea crear una cuenta"
                         "de Telegram\nIngrese 5 si desea crear una cuenta de Signal\nIngrese 6 si desea crear una "
                         "cuenta de Instagram\nInfrese 7 si dese crear una cuenta de Flickr\n"
                         "Ingrese -111 para dejar de crear cuentas\n"))



    def crearFacebook():
        print("Datos necesarios para la creación de una cuenta en Facebook")
        nombre=str(input("Ingrese el nombre del usuario"))
        edad=int(input("Ingrese la edad del usuario"))
        ciudad=str(input("Ingrese la ciudad donde reside el usuario"))
        pais=str(input("Ingrse el pais donde reside el usuario"))
        correo=str(input("ingrese el correo electrónico del usuario"))

        cadena=str("Resumen de datos:\n------------------------------\n")
        cadena=(f"{cadena}Usuario: {nombre}\nEdad: {edad}\nCiudad de residencia:{ciudad}\nPais de residencia: {pais}\n"
                f"Correo electrónico: {correo}")
        return cadena


    def crearTwitter():
        print("Datos necesarios para la creación de una cuenta en Twitter")
        nombreU = str(input("Ingrese el nombre del usuario: "))
        nombres = str(input("Ingrese sus nombres completos: "))
        apellidos = str(input("Ingrese sus apellidos completos: "))
        edad = int(input("Ingrese la edad del usuario: "))
        ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
        pais = str(input("Ingrse el pais donde reside el usuario: "))
        idioma = str(input("Ingrese su idioma nativo: "))
        correo = str(input("ingrese el correo electrónico del usuario: "))

        cadena = str("Resumen de datos:\n------------------------------\n")
        cadena = (
            f"{cadena}Usuario: {nombreU}\nNombres:{nombres}\nApellidos: {apellidos} Edad: {edad}\nCiudad de residencia"
            f":{ciudad}\nPais de residencia: {pais}\nIdioma: {idioma}"
            f"Correo electrónico: {correo}")
        print(cadena)


    def crearWhatsapp():
        print("Datos necesarios para la creación de una cuenta en Whatsapp")
        nombre = str(input("Ingrese el nombre del usuario: "))
        numeroTelefono = str(input("Ingrese su numero de telefono: "))
        edad = int(input("Ingrese la edad del usuario: "))
        ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
        pais = str(input("Ingrese el pais donde reside el usuario: "))

        cadena = str("Resumen de datos:\n------------------------------\n")
        cadena = (
            f"{cadena}Usuario: {nombre}\nNumero de Telefono: {numeroTelefono}\n Edad: {edad}\nCiudad de residencia:"
            f"{ciudad}\nPais de residencia: {pais}\n"
            )
        return cadena

    def crearTelegram():
        print("Datos necesarios para la creación de una cuenta en Telegram")
        nombreU = str(input("Ingrese el nombre del usuario: "))
        numero = int(input("Ingrese el número de teléfono del usuario: "))
        ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
        pais = str(input("Ingrse el pais donde reside el usuario: "))
        hobby = str(input("Ingrese el hobby faborito del usuario: "))


        cadena = str("Resumen de datos:\n------------------------------\n")
        cadena = (
            f"{cadena}Usuario: {nombreU}\nNúemro de teléfono: {numero}\nCiudad de residencia"
            f":{ciudad}\nPais de residencia: {pais}\nHobby favorito: {hobby}")
        print(cadena)


    def crearSignal():
        print("Datos necesarios para la creación de una cuenta en Signal")
        nombre = str(input("Ingrese el nombre del usuario: "))
        numeroTelefono = str(input("Ingrese su numero de telefono: "))
        ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
        pais = str(input("Ingrese el pais donde reside el usuario: "))
        hobby = str(input("Ingrese su hobby preferido: "))

        cadena = str("Resumen de datos:\n------------------------------\n")
        cadena = (
            f"{cadena}Usuario: {nombre}\nNumero de Telefono: {numeroTelefono}\nCiudad de residencia:{ciudad}\n"
            f"Pais de residencia: {pais}\nHobby Principal: {hobby}\n")
        return cadena


    def crearInstagram():
        print("Datos necesarios para la creación de una cuenta en Instagram")
        nombreU = str(input("Ingrese el nombre del usuario: "))
        ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
        edad = int(input("Ingrese la edad del usuario: "))
        correo = str(input("ingrese el correo electrónico del usuario: "))

        cadena = str("Resumen de datos:\n------------------------------\n")
        cadena = (
            f"{cadena}Usuario: {nombreU}\nCiudad de residencia"
            f":{ciudad}\nEdad: {edad}\nCorreo electrónico: {correo}")
        print(cadena)

    def crearFlickr():
        print("Datos necesarios para la creación de una cuenta en Flickr")
        nombre = str(input("Ingrese el nombre del usuario: "))
        correo = str(input("Ingrese su correo: "))

        cadena = str("Resumen de datos:\n------------------------------\n")
        cadena = (f"{cadena}Usuario: {nombre}\nCorreo Electrónico: {correo}\n")
        return cadena

    if (eleccion == 1):
        print(crearFacebook())
    elif(eleccion==2):
        crearTwitter()
    elif(eleccion == 3):
        print(crearWhatsapp())
    elif(eleccion==4):
        crearTelegram()
    elif (eleccion == 5):
        print(crearSignal())
    elif (eleccion == 6):
        crearInstagram()
    elif (eleccion == 7):
        print(crearFlickr())
    elif (eleccion == -111):
        bandera = False
        if (contador >= 1 and contador <= 5):
            print(mensajeFinal[0])
        elif (contador >= 6 and contador <= 15):
            print(mensajeFinal[1])
        elif (contador >= 16):
            print(mensajeFinal[2])
        print(f"Proceso de creaccion de cuentas finalizado\nNumero de cuentas creadas: {contador}")
    contador = contador + 1


# agregar los métodos faltantes

# Aquí empieza el proceso cuando se ejecuta por consola
# el archivo
# python run.py
#"if __name__ == "__main__":
#	"""
#	Leer las indicaciones para que el proceso cumpla
#	lo solicitado.
#	"""

#   """print("proceso inicial")
#   crearFacebook()
#    cuenta_twitter = crearTwitter()
#    print(cuenta_twitter)
