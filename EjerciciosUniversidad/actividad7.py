###################################################################
#                             MODULOS
###################################################################

import numpy as np

###################################################################
#                            FUNCIONES
###################################################################

def verificar(valor, inf, sup):

    while(valor < inf or valor > sup):

        # Entrada:
        valor = int(input(f"ERROR: Ingrese un numero valido [{inf} a {sup}]: "))

    return valor


def cargarMatriz(matriz, fil, col):

    for i in range(fil):

        print(f"--- Producto {i+1} ---")

        for j in range(col):

            # Entrada:
            matriz[i][j] = int(input(f"Mes {j+1}: "))

        print()


def mostrarMatriz(matriz, fil, col):

    print("\n----- MATRIZ -----")

    for i in range(fil):

        for j in range(col):

            # Salida:
            print(f"{matriz[i][j]:10}", end="")

        print()


def mostrarMatrizConTotalDeVentas(matriz, fil, col):

    print("\n----- MATRIZ CON TOTAL DE VENTAS INCLUIDO-----")

    for i in range(fil):

        for j in range(col):

            # Salida:
            print(f"{matriz[i][j]:10}", end="")

        print()


def mesDeMasVentaDeUnPorducto(matriz, fil, col):
    
    # Entrada:
    filaDelProducto = int(input(f"Ingrese fila del producto: "))
    filaDelProducto = verificar(filaDelProducto, 1, fil) - 1

    return matriz[filaDelProducto, :col].argmax() + 1


def productoMenosVendidoDelMes(matriz, fil, col):

    # Entrada:
    mes = int(input(f"Ingrese el mes a consultar: "))
    mes = verificar(mes, 1, col) - 1

    return matriz[:fil, mes].argmin() + 1


def agregarColumnaVentaTotal(matriz, fil, col):

    for i in range(fil):

        matriz[i][col] = matriz[i][:col].sum()

    # Salida:
    print("Columna agregada EXITOSAMENTE")


###################################################################
#                        PROGRAMA PRINCIPAL
###################################################################


# ------------------------- ENTRADAS -------------------------


# Creamos la matriz:
matriz = np.empty((100,13), dtype="int") 
# Hemos fijado arbitrariamente un maximo de 100 productos
# 12 columanas para los meses + columna extra para cantidades vendidadas.


# Entradas de filas:
filas = int(input("Ingrese cantidad de productos a registrar [MAX: 100]: "))
filas = verificar(filas, 1, 100)


# Entradas de columnas:
columnas = int(input("Ingrese cantidad de meses a registrar [MAX: 12]: "))
columnas = verificar(columnas, 1, 12)


# ----------------------- PROCESAMIENTO -----------------------


#Llamada a funciones:
cargarMatriz(matriz, filas, columnas)
mostrarMatriz(matriz, filas, columnas)


# Bandera para controlar la ejecucion del programa:
banderaDeFin = True

# Bandera para controlar ingreso de columna de ventas totales:
banderaDeMatrizTotalIncluido = False


while (banderaDeFin):

    print("\n*********** MENU ***********\n")
    print("[1] Mostrar matriz")
    print("[2] Mostrar mes de mayor venta de un producto")
    print("[3] Mostrar producto menos vendido de un determinado mes")
    print("[4] Agregar columna con venta total por producto")
    print("[5] Salir\n")

    # Entrada de seleccion de opcion:
    opcion = int(input("Seleccione una Opcion: "))


    # Se procesa la opcion elegida y se ejecuta el bloque de codigo correspondiente:
    match opcion:


        case 1:

            print("\n******* Visualizacion de Matriz *******\n")

            print("¿Que matriz desea visualizar?:")
            print("[1] Matriz Ventas")
            print("[2] Matriz Ventas: con Total de ventas incluido")

            # Entrada  de seleccion de opcion:
            op = int(input("Ingrese una opcion [1 o 2]: "))

            match (op):

                case 1:
                    # Llamada a funcion:
                    mostrarMatriz(matriz, filas, columnas)

                case 2:
                    if(banderaDeMatrizTotalIncluido):
                    # Llamada a funcion:
                        mostrarMatrizConTotalDeVentas(matriz, filas, columnas + 1) 
                    else:
                        #Salida:
                        print("\nERROR: La columna de ventas totales aun NO FUE AGREGADA")
                
                case _:
                    # Salida:
                    print("\nERROR: Ingrese una opcion valida\n")


        case 2:

            print("\n******* Mes de mayor venta de un producto *******\n")

            # Llamada a funcion:
            numeroDeMes = mesDeMasVentaDeUnPorducto(matriz, filas, columnas)

            # Salida:
            print(f"La mayor venta del producto ingresado fue en el MES N°{numeroDeMes}")


        case 3:

            print("\n******* Producto menos vendido de un mes *******\n")

            # Llamada a funcion:
            productoMenosVendido = productoMenosVendidoDelMes(matriz, filas, columnas)  

            # Salida:
            print(f"El producto menos vendido del mes ingresado es el PRODUCTO N°{productoMenosVendido}")


        case 4:

            print("\n******* Agregar columna de ventas totales *******\n")

            if (banderaDeMatrizTotalIncluido == False):

                # Llamada a funcion:
                agregarColumnaVentaTotal(matriz, filas, columnas)
                mostrarMatrizConTotalDeVentas(matriz, filas, columnas + 1)

                # La bandera de matriz total cambia:
                banderaDeMatrizTotalIncluido = True
            
            else:
                # Salida:
                print("La columna de ventas totales YA FUE AGREGADA")


        case 5:
            
            # La bandera de control cambia para finalizar el programa:
            banderaDeFin = False

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")


        case _:

            # Salida:
            print("ERROR: Ingrese una opcion valida\n")