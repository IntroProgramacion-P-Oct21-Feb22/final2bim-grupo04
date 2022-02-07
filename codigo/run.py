def main():  # definimos la funcion principal
    bandera = True  # declaramos la variable booleana "bandera" y le asinamos el valor True
    contador = 0  # declaramos la variable contador para ir acumulando el numero de cuentas creadas
    while bandera:
        # Iniciamos un ciclo while con la condicion que se ejecute mientras que bandera sea "True"
        # A continuacion presentamos el menu de opciones, que servira para que el usuario ingrese por teclado el valor
        # de la variable "eleccion" y elija que cuenta desea crear
        eleccion = int(input("Ingrese el 1 para crear cuenta de Facebook\n"
                             "Ingrese el 2 para crear cuenta de twitter\n"
                             "Ingrese el 3 para crear cuenta de Whatsapp\n"
                             "Ingrese el 4 para crear cuenta de Telegram\n"
                             "Ingrese el 5 para crear cuenta de Signal\n"
                             "Ingrese el 6 para crear cuenta de Instagram\n"
                             "Ingrese el 7 para crear cuenta de Flickr\n"
                             "Ingrese 0 para dejar de crear cuentas\n"))
        if eleccion == 1:   # Iniciamos un condicional "si" con la condicion de que si el usuario ingreso 1 en la
                            # varible eleccion imprima la funcion "crearFacebook"
            print(crearFacebook())
        elif eleccion == 2: # De lo contrario usamos un condicional "si" con la condicion de que si el usuario
                            # ingresa 2 en la varible eleccion llame el procedimiento "CrearTwitter"
            crearTwitter()
        elif eleccion == 3: # De lo contrario usamos un condicional "si" con la condicion de que si el usuario
                            # ingresa 3 en la variable eleccion imprimir la funcion "crearWhatsapp"
            print(crearWhatsapp())
        elif eleccion == 4: # De lo contrario usamos un condicional "si" con la condicion de que si el usuario
                            # ingresa 4 en la varible eleccion llame el procedimiento "CrearTelegram"
            crearTelegram()
        elif eleccion == 5: #De lo contrario usamos un condicional "si" con la condicion de que si el usuario
                            # ingresa 5 en la variable eleccion imprimir la funcion "crearSignal"
            print(crearSignal())
        elif eleccion == 6: # De lo contraio usamos un condicional "si" con la condicion de que si el usuario
                            # ingresa 6 en la varible eleccion llame el procedimiento "CrearInstagram"
            crearInstagram()
        elif eleccion == 7: ##De lo contrario usamos un condicional "si" con la condicion de que si el usuario
                            # ingresa 7 en la variable eleccion imprimir la funcion "crearFlickr"
            print(crearFlickr())
        elif (
                eleccion == 0 or eleccion < 0 or eleccion > 7):  # De lo contraio usamos un condicioanl para que si la
                                                            # variable eleccion es < o igual a 0 o mayor a 7 el
                                                            # valor de bandera cambie a falso y termine el ciclo while
            bandera = False
            print("Proceso de creacion de cuentas finalizado")  #Además, se presenta en pantalla un mensaje expresando
                                                                # que el proceso de creación de cuentas ha finalizado

        if 1 <= eleccion <= 7: # Usamos un condicional si por fuera del anterior para que mientras la variable eleccion
                               # sea mayor o igual a 1 y menor o igual a 7 el contador sume en 1 su valor anterior
            contador = contador + 1

    #Al finalizar el ciclo y salir de el presentamos en pantalla una cadena final con un resumen de cuentas creadas, con
    # el valor de la variable contador y ademas con un mensaje que retorna de la funcion "obtenerMensaje" a la cual le
    # enviamos como parámetro el valor final del contador
    cadena = "\nNumero de cuentas creadas: %d --- %s\n" % (contador, obtenerMensaje(contador))
    print(cadena)


def crearFacebook():# Iniciamos la funcion "crearFacebook" en la cual inicializamos las varibles requeridas y pedimos
                    # al usuario que ingrese los datos por  teclado en este caso sera "nombre,edad,ciudad,pais y correo"
    nombre = str(input(f"Creando Facebook\nIngrese el nombre del usuario: "))
    edad = str(input("Ingrese la edad del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    correo = str(input("Ingrese el correo electrónico del usuario: "))

    cadena = str("")    # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se retornara una
                        # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nEdad: %s\nCiudad de residencia:%s\n"
              "Pais de residencia: %s\nCorreo electrónico: %s\n" % (cadena, nombre, edad, ciudad, pais, correo))
    return cadena  # retorna la cadena


def crearTwitter():# Iniciamos la funcion "crearTwitter" en la cual inicializamos las variables requeridas y pedimos al
    # usuario que ingrese los datos por teclado en este caso sera "nombre del usuario,nombres comletos,apellidos
    # completos,edad, ciudad,pais,idioma y correo"
    nombreU = str(input(f"Creando Twitter\nIngrese el nombre del usuario: "))
    nombres = str(input("Ingrese sus nombres completos: "))
    apellidos = str(input("Ingrese sus apellidos completos: "))
    edad = str(input("Ingrese la edad del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    idioma = str(input("Ingrese su idioma nativo: "))
    correo = str(input("Ingrese el correo electrónico del usuario: "))

    cadena = str("")    # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se imprimira una
                        # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nNombres: %s\nApellidos: %s"
              " Edad: %s\nCiudad de residencia:%s\nPais de residencia: %s\nIdioma: %s"
              "Correo electrónico: %s\n" % (cadena, nombreU, nombres, apellidos, edad, ciudad, pais, idioma, correo))
    print(cadena)  # se imprime la cadena


def crearWhatsapp(): # Iniciamos la funcion "crearWhatsapp" en la cual inicializamos las varibles requeridas y pedimos
                    # al usuario que ingrese los datos por teclado en este caso sera "nombre,número,edad,ciudad y pais"
    nombre = str(input(f"Creando Whatsapp\nIngrese el nombre del usuario: "))
    numero = str(input("Ingrese su numero de telefono: "))
    edad = str(input("Ingrese la edad del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))

    cadena = str("")    # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se retornara una
                        # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nNumero de Telefono: %s\n Edad: "
              "%s\nCiudad de residencia:%s\nPais de residencia: %s\n" % (cadena, nombre, numero, edad, ciudad, pais))
    return cadena   # retorna la cadena


def crearTelegram():# Iniciamos la funcion "crearTelegram" en la cual inicializamos las variables requeridas y pedimos
    # al usuario que ingrese los datos por teclado en este caso sera "nombre del usuario,número,ciudad,pais,y hobby"
    nombreU = str(input(f"Creando Telegram\nIngrese el nombre del usuario: "))
    numero = str(input("Ingrese el número de teléfono del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    hobby = str(input("Ingrese su area de interés: "))

    cadena = str("")    # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se imprimira una
                        # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nNúmero de teléfono: %s\n"
              "Ciudad de residencia:%s\nPais de residencia: %s\nHobby favorito: %s\n"
              % (cadena, nombreU, numero, ciudad, pais, hobby))
    print(cadena) # se imprime la cadena


def crearSignal(): # Iniciamos la funcion "crearSignal" en la cual inicializamos las varibles requeridas y pedimos
                   # al usuario que ingrese los datos por teclado en este caso sera "nombre,número,ciudad,pais y hobby"
    nombre = str(input(f"Creando Signal\nIngrese el nombre del usuario: "))
    numero = str(input("Ingrese su numero de telefono: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    pais = str(input("Ingrese el pais donde reside el usuario: "))
    hobby = str(input("Ingrese su hobby preferido: "))

    cadena = str("") # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se retornara una
                     # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada: \nUsuario: %s\nNumero de Telefono: %s\n"
              "Ciudad de residencia:%s\nPais de residencia: %s\nHobby Principal: %s\n"
              % (cadena, nombre, numero, ciudad, pais, hobby))
    return cadena    # se retorna la cadena


def crearInstagram():# Iniciamos la funcion "crearInstagram" en la cual inicializamos las variables requeridas y pedimos
                    # al usuario que ingrese los datos por teclado en este caso sera "nombre del usuario,ciudad,edad,y
                    # correo"
    nombreU = str(input(f"Creando Instagram\nIngrese el nombre del usuario: "))
    ciudad = str(input("Ingrese la ciudad donde reside el usuario: "))
    edad = str(input("Ingrese la edad del usuario: "))
    correo = str(input("Ingrese el correo electrónico del usuario: "))

    cadena = str("")  # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se imprimira una
                      # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nCiudad de residencia"
              ":%s\nEdad: %s\nCorreo electrónico: %s\n" % (cadena, nombreU, ciudad, edad, correo))
    print(cadena)  # se imprime la cadena


def crearFlickr(): # Iniciamos la funcion "crearSignal" en la cual inicializamos las varibles requeridas y pedimos
                   # al usuario que ingrese los datos por teclado en este caso sera "nombre y correo"
    nombre = str(input(f"Creando Flickr\nIngrese el nombre del usuario: "))
    correo = str(input("Ingrese su correo: "))

    cadena = str("") # Iniciamos una cadena vacia en la cual se acumularan los datos y finalmente se retornara una
                     # cadena con un resumen detallado de la informacion ingresada por el usuario
    cadena = ("%sResumen de cuenta creada:\nUsuario: %s\nCorreo Electrónico: %s\n" % (cadena, nombre, correo))
    return cadena  # se retorna la cadena


def obtenerMensaje(a): # Iniciamos la funcion "obtenerMensaje" y renombramos la variable que se envió como parámetro
                        # "contador" por "a"

    # Inicializamos el arreglo unidimencional "mensajeFinal" con 3 elementos de tipo str, que seran usados para
    # retornar un mensaje con base al número total de cuentas creadas
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]

    if (a >= 1 and a <= 5):     # Iniciamos un condicional "si" con la condicion de que si la varible "a" es mayor o
                                # igual a 1 y menor o igual a 5, entonces se retorna el valor del arreglo "mensajeFinal"
                                #en la posición 0
        return (mensajeFinal[0]) #Se retorna el mensaje "Campaña con poca afluencia"

    elif (a >= 6 and a <= 15):  # De lo contrario, usamos un condicional "si" con la condicion de que si la varible "a"
                                # es mayor o igual a 6 y menor o igual a 15, entonces se retorna el valor del arreglo
                                # "mensajeFinal" en la posición 1
        return (mensajeFinal[1]) #Se retorna el mensaje "Campaña moderada siga adelante"

    elif (a >= 16):             # De lo contrario, usamos un condicional "si" con la condicion de que si la varible "a"
                                # es mayor o igual a 16 , entonces se retorna el valor del arreglo
                                # "mensajeFinal" en la posición 2
        return (mensajeFinal[2])#Se retorna el mensaje "Excelente campaña"

    elif (a <= 0):              # De lo contrario, usamos un condicional "si" con la condicion de que si la varible "a"
                                # es mmenor o igual a 0 , entonces se retorna el mensaje "No ha creado cuentas"
        return ("No ha creado cuentas")


print(main()) # Se ejecuta la fucnion princial