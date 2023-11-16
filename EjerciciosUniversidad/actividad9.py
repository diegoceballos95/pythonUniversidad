##########################################################################
#                                 MODULOS
##########################################################################

import os

##########################################################################
#                                FUNCIONES
##########################################################################


def determinarCantQuem (archivo):

    # Leemos 1° Linea:
    linea = archivo.readline()

    # Contador de Quemadores:
    contadorQuem = 0

    while (linea != ""):

        contadorQuem += 1

        # Leemos siguiente linea:
        linea = archivo.readline()

    return contadorQuem


def mostrarQuemPorID(archivo, id):

    # Leemos 1° Linea y quitamos el caracter de salto de linea:
    linea = archivo.readline()
    lineaSinSalto = linea.strip('\n')

    # Bandera para detener ciclo cuando hallamos ID:
    bandera = True

    while (lineaSinSalto != "" and bandera):

        # Separamos los datos contenidos en cada linea:
        datosQuem = lineaSinSalto.split(";")

        if (datosQuem[0] == id):

            print("\nDatos del quemador: ")
            print(f"- id: {datosQuem[0]}")
            print(f"- Hs de trabajo acumuladas: {datosQuem[1]}")
            print(f"- Ubicacion: {datosQuem[2]}")
            print(f"- Proximo Service: {datosQuem[3]}")
            print(f"- Tecnico de ultimo mantenimiento: {datosQuem[4]}")
            print(f"- Estado: {datosQuem[5]} <- (0:fuera de servicio - 1:en servicio - 2:mantenimineto)")

            bandera = False

        else: 

            # Leemos siguiente linea y quitamos el caracter de salto de linea:     
            linea = archivo.readline()
            lineaSinSalto = linea.strip('\n')


def promedioHsTrabajadasPorSector(archivo, sector):

    # Leemos 1° Linea:  
    linea = archivo.readline()

    # Contador de Hs por sector y de Cantidad de quemadores:
    contadorHsSector = 0
    contadorQuemSector = 0

    while (linea != ""):

        # Separamos los datos contenidos en cada linea:
        datosQuem = linea.split(";")

        if (datosQuem[2] == sector):

            contadorHsSector += int(datosQuem[1])
            contadorQuemSector += 1

        # Leemos siguiente linea:
        linea = archivo.readline()

    # Calculo del promedio de hs por sector:
    promedio = contadorHsSector / contadorQuemSector

    return promedio


def quemEnServiPorTecnico(archivo, tecnico):

    # Leemos 1° Linea y quitamos el caracter de salto de linea:
    linea = archivo.readline()
    lineaSinSalto = linea.strip('\n')

    while (linea != ""):

        # Separamos los datos contenidos en cada linea:
        datosQuem = lineaSinSalto.split(";")

        if (datosQuem[4] == tecnico and datosQuem[5] == "1"):

            print("\nDatos del quemador: ")
            print(f"- id: {datosQuem[0]}")
            print(f"- Hs de trabajo acumuladas: {datosQuem[1]}")
            print(f"- Ubicacion: {datosQuem[2]}")
            print(f"- Proximo Service: {datosQuem[3]}")
            print(f"- Tecnico de ultimo mantenimiento: {datosQuem[4]}")
            print(f"- Estado: {datosQuem[5]} <- (0:fuera de servicio - 1:en servicio - 2:mantenimineto)")

        # Leemos siguiente linea y quitamos el caracter de salto de linea:   
        linea = archivo.readline()
        lineaSinSalto = linea.strip('\n')


def eliminarQuemFueraDeServ(archivo):

    # Damos forma a la ruta:
    rutaDeAux = os.path.join(os.getcwd(), "auxiliar.txt")

    # Se crea un archivo txt y se abre en modo escritura:
    archivoAux = open(rutaDeAux, 'w')

    # Leemos 1° Linea y quitamos el caracter de salto de linea:   
    linea = archivo.readline()
    lineaSinSalto = linea.strip('\n')

    while (linea != ""):

        # Separamos los datos contenidos en cada linea:
        datosQuem = lineaSinSalto.split(";")

        if (datosQuem[5] != "0"):

            # Se escribe en el nuevo archivo auxiliar.txt
            archivoAux.write(linea)
            
        # Leemos siguiente linea y quitamos el caracter de salto de linea:   
        linea = archivo.readline()
        lineaSinSalto = linea.strip('\n')

    # Cierro y elimino el archivo Quemadores.txt:
    archivo.close()
    os.remove(archivo.name)
    print("- Quemadores.txt se elimino correctamente")

    # Cierro y renombro el archivo auxiliar.txt:
    archivoAux.close()
    os.rename(rutaDeAux, os.path.join(os.getcwd(), "Quemadores.txt"))
    print("- auxiliar.txt se renombro correctamente como Quemadores.txt")


###################################################################
#                        PROGRAMA PRINCIPAL
###################################################################


# ---------------------------- ENTRADAS ----------------------------


# Bandera para controlar la ejecucion del programa:
banderaMenu = False

# Bandera para controlar la ejecucion del programa:
banderaTryExcept = True

while (banderaTryExcept):

    try:

        # Entrada del archivo:
        nombreDeArchivo = input("\nIngrese nombre del archivo: ")

        # Damos forma a la ruta:
        ruta = os.path.join(os.getcwd(), nombreDeArchivo)

        # Creamos y abrimos en modo lectura un objeto file:
        archivoQuem = open(ruta, "r")

        # Salida:
        print(f"\nArchivo cargado exitosamente")

        # La bandera cambia para dar acceso al Menu de opciones:
        banderaMenu = True
        # La bandera cambia para salir del bucle Try Except:
        banderaTryExcept = False

    except:

        # Entrada (Incluye msj de error):
        op = input("\nERROR: EL ARCHIVO NO EXISTE\nIngrese:\n[1] Reintentar\n[Otra tecla] Salir:\n\nSu eleccion: ")

        if (op == '1'):
            
            # Salida:
            print("\n*********** REINTENTO ***********")         

        else:

            # La bandera cambia para salir del bucle Try Except y finalizarprograma:
            banderaTryExcept = False

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")
            

# -------------------------- PROCESAMIENTO --------------------------


while (banderaMenu):

    print("\n*********** MENU ***********\n")
    print("[1] Mostrar cantidad de quemadores")
    print("[2] Mostrar quemador por id")
    print("[3] Mostrar promedio de horas de trabajo por sector")
    print("[4] Mostrar quemadores en servicio reparados por tecnico")
    print("[5] Eliminar quemadores fuera de servicio")
    print("[6] Salir\n")

    # Entrada de seleccion de opcion:
    opcion = int(input("Seleccione una Opcion: "))

    # El puntero retorna al inicio del archivo:
    archivoQuem.seek(0,0)

    # Se procesa la opcion elegida y se ejecuta el bloque de codigo correspondiente:
    match opcion:


        case 1:

            print("\n******* Cantidad de quemadores *******\n")

            # Llamada a funcion:
            cantQuem = determinarCantQuem(archivoQuem)

            # Salida:
            print(f"Cantidad de Quemadores: {cantQuem}")


        case 2:

            print("\n******* Informacion de quemador por ID *******\n")

            # Entrada:
            id = (input("Ingresar id: "))

            # Llamada a funcion:
            mostrarQuemPorID(archivoQuem, id)


        case 3:

            print("\n******* Promedio de hs de trabajo por sector *******\n")

            # Entrada:
            sector = (input("Ingrese sector -> [I] izquiero - [D] derecho - [B] boveda: "))

            # Llamada a funcion:
            promHs = promedioHsTrabajadasPorSector(archivoQuem, sector.upper())

            # Salida:
            print(f"\nPromedio de hs en el sector {sector.upper()}: {promHs} hs")


        case 4:
            
            print("\n******* Quemadores en servicio reparados por tecnico *******\n")

            # Entrada:
            tecnico = (input("Ingrese nombre del tecnico: "))

            # Llamada a funcion:
            quemEnServiPorTecnico(archivoQuem, tecnico.title())


        case 5:
            
            print("\n******* Eliminar quemadores fuera de servicio *******\n")

            # Llamada a funcion:
            eliminarQuemFueraDeServ(archivoQuem)

            # El archivo original no existe, pero ahora existe otro con el mismo nombre en la misma ubicacion, por lo cual la variable de "ruta" que usamos al inicio, sigue siendo valida, tomando ahora el nuevo archivo.txt:
            archivoQuem = open(ruta, 'r')

        case 6:
            
            # La bandera de control cambia para finalizar el programa:
            banderaMenu = False

            # Se cierra el objeto file:
            archivoQuem.close()

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")


        case _:

            # Salida:
            print("ERROR: Ingrese una opcion valida\n")