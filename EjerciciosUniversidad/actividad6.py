# ACTIVIDAD OBLIGATORIA N°5

# -------------------- FUNCIONES --------------------

def cargarMatriz (tabla):

    # Validar que la tabla no se haya cargado anteriormente:
    if len(tabla) == 0:

        # Entrada de filas y columnas:
        m = int(input("\nIngrese la cantidad de equipos: "))
        n = int(input("Ingrese la cantidad de meses: "))

        for i in range(m):

            filaEquipos = []

            print(f"\n--- Ingrese datos del {i+1}° equipo ---\n")

            for j in range(n):

                # Entrada de cada uno de los datos de cada fila:
                x = int(input(f"Mes {j+1}: "))

                filaEquipos.append(x) #Agrega x en la fila.

            tabla.append(filaEquipos) #Agrega fila en la tabla.

        # Salida:
        print("\nLa tabla se cargo exitosamente")

    else:
        # Salida:
        print("La tabla ya se encuentra cargada")


def mostrarProduccionPorMes (tabla):

    # Validar que haya datos para mostrar:
    if len(tabla) != 0:

        # Entrada del mes a mostrar:
        mes = int(input("Ingrese el numero de mes que desea visualizar: "))

        # Validar que el mes corresponda con un indice de las columnas:
        if mes-1 < len(tabla[0]):

            for i in range(len(tabla)):
                
                # Salida:
                print(f"* Produccion del Equipo {i+1} en el Mes {mes}: {tabla[i][mes-1]} L.")
        else:

            # Salida:
            print("El mes ingresado no existe en la tabla\n")

    else:

        # Salida:
        print("Tabla vacia: No hay nada para visualizar\n")


def mostrarProduccionPorEquipo (tabla):

    # Validar que haya datos para mostrar:
    if len(tabla) != 0:

        # Entrada del equipo a mostrar:
        equipo = int(input("Ingrese el numero de equipo que desea visualizar: "))

        # Validar que el equipo corresponda con un indice de las filas:
        if equipo-1 < len(tabla):

            for i in range(len(tabla[0])):

                # Salida:
                print(f"* Produccion del Equipo {equipo} en el Mes {i+1}: {tabla[equipo-1][i]} L.")
        else:

            # Salida:
            print("El equipo ingresado no existe en la tabla\n")

    else:

        # Salida:
        print("Tabla vacia: No hay nada para visualizar\n")


def agregarMesDeProduccion (tabla):

    # Validar que haya minimo un equipo registrado en la tabla:
    if len(tabla) != 0:

        for i in range(len(tabla)):

            # Entrada de dato de produccion por cada equipo de la tabla:
            datoPorEquipo = int(input(f"Ingrese produccion del equipo {i+1}: "))

            # Agrega los datos al equipo correspondiente:
            tabla[i].append(datoPorEquipo) 

        # Salida:
        print("Los datos se agregaron exitosamente\n")
    else:

        # Salida:
        print("Tabla vacia: No hay equipos registrados\n")


def eliminarInformacionDeEquipo (tabla):

    # Validar que haya minimo un equipo registrado en la tabla:
    if len(tabla) != 0:

        # Entrada del equipo que se desea borrar:
        equipoAEliminar = int(input(f"Ingrese el numero del equipo que desea eliminar: ")) 

        # Validar que el equipo ingresado corresponde a algun indice de las filas:
        if equipoAEliminar-1 < len(tabla):

            del tabla[equipoAEliminar-1]

            # Salida:
            print(f"El equipo {equipoAEliminar} se elimino correctamente")
            print("La numeracion de los equipos mayores al eliminado, disminuyó en 1 (visualizar la tabla)")
        
        else:
            # Salida:
            print("El equipo ingresado no existe")

    else:
        # Salida:
        print("La tabla esta vacia\n")


def mostrarTabla (tabla):

    # Validar que haya datos para mostrar:
    if len(tabla) != 0:

        # Se recorren las filas:
        for i in range(len(tabla)):

            print(f"\nEquipo {i+1} -> ", end="")

            # Se recorren las columnas:
            for j in range(len(tabla[0])):

                # Salida:
                print(f"Mes {j+1}: {tabla[i][j]} L. | ", end="",)

        print("")

    else:
        # Salida:
        print("Tabla vacia: No hay nada para visualizar\n")

# -------------------- ENTRADAS --------------------

# Se inicializa la tabla principal:
tablaDeProduccion = []

# Bandera para controlar la ejecucion del programa:
banderaDeFin = 1

# -------------------- PROCESAMIENTO --------------------

while (banderaDeFin):

    print("\n*********** MENU ***********\n")
    print("[1] Cargar tabla de produccion")
    print("[2] Mostrar produccion por mes")
    print("[3] Mostrar produccion por equipo")
    print("[4] Agregar nuevo mes de produccion")
    print("[5] Eliminar informacion de un equipo")
    print("[6] Mostrar tabla de produccion")
    print("[7] Salir\n")

    # Entrada de seleccion de opcion:
    opcion = int(input("Seleccione una Opcion: "))

    # Se procesa la opcion elegida y se ejecuta el bloque de codigo correspondiente:
    match opcion:

        case 1:

            print("\n******* Carga de tabla de prodccion *******\n")

            # Llamada a funcion:
            cargarMatriz(tablaDeProduccion)
        
       
        case 2:

            print("\n******* Visualizacion de prodccion por mes *******\n")

            # Llamada a funcion:
            mostrarProduccionPorMes(tablaDeProduccion)

      
        case 3:

            print("\n******* Visualizacion de prodccion por equipo *******\n")

            # Llamada a funcion:
            mostrarProduccionPorEquipo(tablaDeProduccion)

     
        case 4:

            print("\n******* Agregar nuevo mes de produccion *******\n")

            # Llamada a funcion:
            agregarMesDeProduccion(tablaDeProduccion)

       
        case 5:

            print("\n******* Eliminar informacion de equipo *******\n")

            # Llamada a funcion:
            eliminarInformacionDeEquipo(tablaDeProduccion)

     
        case 6:

            print("\n******* Visualizacion de tabla de prodccion *******")

            # Llamada a funcion:
            mostrarTabla(tablaDeProduccion)

     
        case 7:
            # La bandera de control cambia para finalizar el programa:
            banderaDeFin = 0

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")

      
        case _:           

            # Salida:
            print("Ingrese una opcion valida\n")