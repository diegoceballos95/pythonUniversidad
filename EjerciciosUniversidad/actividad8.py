##########################################################################
#                                 MODULOS
##########################################################################

import numpy as np

##########################################################################
#                                 CLASES
##########################################################################

class Quemador:
    
    ''' 
    ATRIBUTOS:

    * idQuem (int): identificador univoco del quemador.
    * hsTrab (int): Cantidad de horas acumuladas de trabajo.
    * ubic (char): "I"-> Lateral izquierdo. "d"-> Lateral derecho. "b"-> Bóveda.
    * proxService (int): Horas de trabajo que debe alcanzar para el próx. mantenimiento.
    * tecnico (string): Nombre de la persona que realizó el último mantenimiento.
    * estado (int): 0-> Fuera de servicio. 1-> En servicio. 2->En mantenimiento.

    '''

    # -------------------------- Constructor ---------------------------
    
    def __init__(self, idQuem, hsTrab, ubic, proxService, tecnico, estado):
        self.__idQuem = idQuem
        self.__hsTrab = hsTrab
        self.__ubic = ubic
        self.__proxService = proxService
        self.__tecnico = tecnico
        self.__estado = estado

    # ----------------------------- Getters -----------------------------

    def get__idQuem (self):
        return self.__idQuem

    def get__hsTrab (self):
        return self.__hsTrab

    def get__ubic (self):
        return self.__ubic

    def get__proxService (self):
        return self.__proxService
    
    def get__estado (self):
        return self.__estado

    # ----------------------------- Setters -----------------------------

    def set__tecnico (self, tecnico):
        self.__tecnico = tecnico

    def set__estado (self, estado):
        self.__estado = estado

    # --------------------------- Otros Metodos --------------------------

    def mostrar(self):

        print(f"- id: {self.__idQuem}")
        print(f"- Hs de trabajo acumuladas: {self.__hsTrab}")
        print(f"- Ubicacion: {self.__ubic}")
        print(f"- Proximo Service: {self.__proxService}")
        print(f"- Tecnico de ultimo mantenimiento: {self.__tecnico}")

        match(self.__estado):
            case 0: print("- Estado: Fuera de servicio")
            case 1: print("- Estado: En servicio")
            case 2: print("- Estado: En mantenimiento")


##########################################################################
#                                FUNCIONES
##########################################################################

def verificar(valor, inf, sup):

    while(valor < inf or valor > sup):

        # Entrada:
        valor = int(input(f"ERROR: Ingrese un numero valido [{inf} a {sup}]: "))

    return valor


def cargarLista(lista, N):

    for i in range(N):

        print(f"\nINGRESE DATOS DEL {i+1}° QUEMADOR:")

        id = int(input("- id: "))
        hsTrab = int(input("- Hs de trabajo acumuladas: "))
        ubicacion = (input("- Ubicacion: "))
        proxService = int(input("- Proximo Service: "))
        tecnico = input("- Tecnico: ")
        estado = int(input("- Estado: "))

        lista[i] = Quemador(id, hsTrab, ubicacion, proxService, tecnico, estado)


def mostrarLista(lista, N):

    for i in range(N):

        print(f"\n{i+1}° Quemador de la lista:\n")

        lista[i].mostrar()

    
def mostrarQuemPorID (lista, N, id):

    # Variable para guardar posicion en caso de hallar el quemador: 
    pos = -1

    for i in range(N):

        if (lista[i].get__idQuem() == id):

            pos = i

    if (pos != -1):

        lista[pos].mostrar()

    else:

        # Salida:
        print("\nNingun quemador coincide con id ingresado")


def mostrarQuemParaMantenimiento(lista, N):

    # Contador para determinar si existen o no quemadores para mantenimineto:
    contador = 0

    for i in range(N):

        if(lista[i].get__estado() == 1 and lista[i].get__hsTrab() >= lista[i].get__proxService()):

            contador += 1

            # Salidas:
            print(f"ID: {lista[i].get__idQuem()}")
            print(f"Hs de trabajo acumuladas: {lista[i].get__hsTrab()}")
            print(f"Ubicacion: {lista[i].get__ubic()}")
            
    if (contador == 0):

        # Salida:
        print("No hay quemadores que requieran mantenimiento")


def enviarQuemAMantenimineto(lista, N, id, tecnico):

    # Variable para guardar posicion en caso de hallar el quemador 
    pos = -1

    for i in range(N):

        if (lista[i].get__idQuem() == id and lista[i].get__estado() != 2):

            pos = i

    if (pos != -1):
        
        lista[pos].set__tecnico(tecnico)
        lista[pos].set__estado(2)

        # Salida:
        print("\nEl quemador se envio exitosamente a mantenimineto:\n")

        # Llamada a funcion:
        mostrarQuemPorID(lista, N, id)

    else:

        # Salida:
        print("Ningun quemador coincide con los datos ingresados\n")


def QuemProxService(lista, N, hs):

    # Contador para determinar si existen o no quemadores proximos a service:
    contador = 0

    for i in range(N):

        if((lista[i].get__proxService() - lista[i].get__hsTrab() <= hs) and (lista[i].get__estado() == 1)):

            contador += 1

            # Llamada a funcion:
            lista[i].mostrar()

            print("")

    if (contador == 0):

        # Salida:
        print("No hay quemadores que requieran un service")
        

###################################################################
#                        PROGRAMA PRINCIPAL
###################################################################


# ---------------------------- ENTRADAS ----------------------------


# Entradas de N quemadores:
cantQuemadores = int(input("Ingrese cantidad de quemadores a registrar [MAX: 28]: "))
cantQuemadores = verificar(cantQuemadores, 1, 28)


# Creamos la lista:
lista = np.empty(cantQuemadores, dtype = Quemador) 


# -------------------------- PROCESAMIENTO --------------------------


#Llamada a funciones:
cargarLista(lista, cantQuemadores)


# Bandera para controlar la ejecucion del programa:
banderaDeFin = True


while (banderaDeFin):

    print("\n*********** MENU ***********\n")
    print("[1] Mostrar lista")
    print("[2] Mostrar quemador por id")
    print("[3] Mostrar quemadores en servicio que requieren mantenimiento")
    print("[4] Enviar quemador a mantenimiento")
    print("[5] Mostrar quemadores que pronto requeriran un service")
    print("[6] Salir\n")

    # Entrada de seleccion de opcion:
    opcion = int(input("Seleccione una Opcion: "))


    # Se procesa la opcion elegida y se ejecuta el bloque de codigo correspondiente:
    match opcion:


        case 1:

            print("\n******* Visualizacion de lista *******")

            # Llamada a funcion:
            mostrarLista(lista, cantQuemadores)


        case 2:

            print("\n******* Mostrar quemador por ID *******\n")

            # Entrada:
            id = int(input("Ingresar id: "))

            # Llamada a funcion:
            mostrarQuemPorID(lista, cantQuemadores, id)


        case 3:

            print("\n******* Quemadores en servicio que requieren mantenimiento *******\n")

            # Llamada a funcion:
            mostrarQuemParaMantenimiento(lista, cantQuemadores)  


        case 4:

            print("\n******* Enviar quemador a mantenimiento *******\n")

            # Entradas:
            id = int(input("Ingresar id: "))
            tecnico = input("Ingresar tecnico: ")

            # Llamada a funcion:
            enviarQuemAMantenimineto(lista, cantQuemadores, id, tecnico)

    
        case 5:
            
            print("\n******* Quemadores que pronto requeriran un service *******\n")

            # Entrada:
            hs = int(input("Ingrese cant. de hs: "))

            # Llamada a funcion:
            QuemProxService(lista, cantQuemadores, hs)


        case 6:
            
            # La bandera de control cambia para finalizar el programa:
            banderaDeFin = False

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")


        case _:

            # Salida:
            print("ERROR: Ingrese una opcion valida\n")