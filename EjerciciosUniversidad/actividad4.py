#  Actividad N°4

from os import system

system("cls")

print("************* GENERADOR DE CORREOS Y CONTRASEÑAS *************")

# Bandera del ciclo while que finaliza o reinicia el programa:
banderaDelPrograma = 1

while banderaDelPrograma:

    # -------------------- ENTRADAS --------------------

    nombreCompleto = input("\nIngrese su nombre completo en formato 'Apellidos, Nombres': ")

    # Bandera del ciclo while para repetir el ingreso del numero si es necesario:
    banderaNumero = 1 

    while banderaNumero:
        numero = input("\nIngrese un numero de 4 digitos: ")
        if numero.isdigit() and len(numero) == 4:
            banderaNumero = 0
        else:
            print("ERROR: ingrese el numero correctamente...")

    # -------------------- PROCESAMIENTO --------------------

    # Se corrige por si la primer letra de los nombres o apellidos esta en minuscula:
    nombreCompletoCorregido = nombreCompleto.title()

    #  Se separan los apellidos y nombres en dos listas:
    listaNombresYApellido = nombreCompletoCorregido.split(",")
    listaDeApellidos = listaNombresYApellido[0].split()
    listaDeNombres = listaNombresYApellido[1].split()

    # Creamos el prototipo base para generar el correo y la contraseña
    prototipo = ""
    for i in listaDeNombres:
        prototipo += i
    for i in listaDeApellidos:
        prototipo += i

    # Se genera el correo electronico:
    correo = prototipo + numero + "@unsa.edu.ar"

    # Se genera la contraseña:
    contraseña = ""
    for letra in prototipo:
        if letra == "a" or letra == "A": contraseña += "1"
        elif letra == "e" or letra == "E": contraseña += "2"
        elif letra == "i" or letra == "I": contraseña += "3"
        elif letra == "o" or letra == "O": contraseña += "4"
        elif letra == "u" or letra == "U": contraseña += "5"
        else: contraseña += letra
    contraseña += numero
        
    # -------------------- SALIDAS --------------------

    print("\n*** Se han generado las siguientes sugerencias para usted ***")
    print(f"Correo electronico: {correo}")
    print(f"Contraseña: {contraseña}\n")

    banderaDelPrograma = int(input("INGRESE: [0] FINALIZAR | [1] REINICIAR: "))

print("\n*********************** FIN DEL PROGRAMA **********************\n")