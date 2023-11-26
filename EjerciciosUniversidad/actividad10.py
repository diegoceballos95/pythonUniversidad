##########################################################################
#                                 MODULOS
##########################################################################

import numpy as np

##########################################################################
#                                FUNCIONES
##########################################################################


def menu():

    print("\n*********** MENU ***********\n")
    print("[1] Consultar una bobina de la lista")
    print("[2] Modificar una bobina de la lista")
    print("[3] Eliminar una bobina de la lista")
    print("[4] Mostrar lista")
    print("[5] Salir\n")

    # Entrada de seleccion de opcion:
    opcion = int(input("Seleccione una Opcion: "))

    return opcion


def verificar(valor, inf, sup):

    while(valor < inf or valor > sup):

        # Entrada:
        valor = int(input(f"ERROR: Ingrese un numero valido [{inf} a {sup}]: "))

    return valor


def cargarLista(lista, N):

    for i in range(N):

        dicBobina = {}

        print("\n*** DATOS DE BOBINA ***")

        # Entrada de datos:
        dicBobina["id"] = int(input("- Ingrese ID de la bobina: "))
        dicBobina["metros"] = int(input("- Ingrese metros (m): "))
        dicBobina["ancho"] = int(input("- Ingrese ancho (mm): "))
        dicBobina["stock"] = int(input("- Ingrese stock: "))

        # Se agragan datos a la lista:
        lista[i] = dicBobina


def mostrarLista(lista, N):

    if(N > 0):

        print("\n--- Lista Actualmente ---")

        for i in range(N):
                
                # Salidas: 
                print("\n*** DATOS DE BOBINA ***")
                print(f"- id: {lista[i]['id']}")
                print(f"- metros(m): {lista[i]['metros']}")
                print(f"- ancho(mm): {lista[i]['ancho']}")
                print(f"- stock: {lista[i]['stock']}")

    else:

        # Salida:
        print("LISTA VACIA")


def verificarID(lista, N, id):

    i = 0

    while(i < N):

        if (lista[i]["id"] == id):

            return True

        i += 1
    
    return False


def consultar(lista, N, id):

    if(verificarID(lista, N, id)):

        for i in range(N):

            if (lista[i]["id"] == id):

                # Salidas:
                print("\n*** DATOS DE BOBINA ***")
                print(f"- id: {lista[i]['id']}")
                print(f"- metros(m): {lista[i]['metros']}")
                print(f"- ancho(mm): {lista[i]['ancho']}")
                print(f"- stock: {lista[i]['stock']}")

    else:

        # Salida:
        print("ERROR: el ID ingresado no existe en la lista")


def modificar(lista, N, id):

    if(verificarID(lista, N, id)):

        for i in range(N):

            if (lista[i]["id"] == id):
                
                print(f"\n*** INGRESE NUEVOS DATOS DE BOBINA ***")

                # Entradas para modificar datos:
                lista[i]["id"] = int(input("- ID: "))
                lista[i]["metros"] = int(input("- Metros(m): "))
                lista[i]["ancho"] = int(input("- Ancho(mm): "))
                lista[i]["stock"] = int(input("- Stock: "))

    else:

        # Salida:
        print("ERROR: el ID ingresado no existe en la lista")


def eliminar(lista, N, id, existeID):
 
    if(existeID):

        # Posicion de la bobina eliminada (se modificará en caso de hallarse el ID):
        pos = 0

        for i in range(N):

            if (lista[i]["id"] == id):

                pos = i

        # Se realiza un CORRIMIENTO ya que no puedo usar ' lista = np.delete(lista, i) ' para que la lista se modifique debido al hecho de que esto retorna una nueva lista y no se modifica la lista que paso por referencia. Ademas, en la clase de Numpy se menciono que a partir de alli, todas las actividades debian hacerse con los arrays de numpy, y es por eso que no uso listas simples:

        while(pos < N-1):

            lista[pos]["id"] = lista[pos+1]["id"]
            lista[pos]["metros"] = lista[pos+1]["metros"]
            lista[pos]["ancho"] = lista[pos+1]["ancho"]
            lista[pos]["stock"] = lista[pos+1]["stock"]
            pos += 1

        # Salida:
        print("\nBobina eliminada exitosamente")

    else: 

        # Salida:
        print("ERROR: el ID ingresado no existe en la lista")


###########################################################################
#                             PROGRAMA PRINCIPAL
###########################################################################


# -------------------------------- ENTRADAS -------------------------------


# Entradas de N bobinas:
cantBobinas = int(input("Ingrese cantidad de bobinas [MAX 100]:"))
cantBobinas = verificar(cantBobinas, 1, 100)

# Crear ls lista:
lista = np.empty(cantBobinas, dtype = dict)

# Se cargan los datos en la lista:
cargarLista(lista, cantBobinas)


# ------------------------------- PROCESAMIENTO ----------------------------


# Bandera para controlar la ejecucion del programa:
banderaDeFin = True


while (banderaDeFin):

    # Lamada a funcion de MENU DE OPCIONES:
    opcion = menu()

    # Se procesa la opcion elegida y se ejecuta el bloque de codigo correspondiente:
    match opcion:


        case 1:

            print("\n******* Consultar bobina *******\n")

            # Entrada:
            id = int(input("Ingrese ID de la bobina: "))

            # Llamada a funcion:
            consultar(lista, cantBobinas, id)


        case 2:

            print("\n******* Modificar bobina *******\n")

            # Entrada:
            id = int(input("Ingrese ID de la bobina: "))

            # Llamada a funcion:
            modificar(lista, cantBobinas, id)


        case 3:

            print("\n******* Eliminar bobina *******\n")

            # Entrada:
            id = int(input("Ingrese ID de la bobina: "))

            # Se guarda la existencia de la bobina para luego decidir si se reduce o no cantBobinas:
            existeID = verificarID(lista, cantBobinas, id)

            # Llamada a funcion:
            eliminar(lista, cantBobinas, id, existeID)

            if (existeID):

                # Se pudo eliminar, por lo que reduce en 1 la cantidad de bobinas de la lista:
                cantBobinas -= 1


        case 4:

            # Llamada a funcion:
            mostrarLista(lista, cantBobinas)


        case 5:
            
            # La bandera de control cambia para finalizar el programa:
            banderaDeFin = False

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")
            

        case _:

            # Salida:
            print("ERROR: Ingrese una opcion valida\n")