# ACTIVIDAD OBLIGATORIA N°5

# -------------------- ENTRADAS --------------------

# Creacion de listas:
listaCodigo = []
listaNombre = []
listaStock = []
listaCantidadVendida = []
listaPrecio = []
listaProductos = [listaCodigo, listaNombre, listaStock, listaCantidadVendida, listaPrecio]

# Bandera para controlar la ejecucion del programa:
banderaDeFin = 1

# -------------------- PROCESAMIENTO --------------------

while (banderaDeFin):

    print("*********** MENU ***********\n")
    print("[1] Registrar un producto nuevo")
    print("[2] Borrar un producto")
    print("[3] Mostrar productos")
    print("[4] Hacer una venta")
    print("[5] Salir\n")

    # Entrada de seleccion de opcion:
    opcion = int(input("Seleccione una Opcion: "))

    # Se procesa la opcion elegida y se ejecuta el bloque de codigo correspondiente:
    match opcion:

        case 1:
            print("\n--- INGRESE NUEVO PRODUCTO ---\n")

            # Entrada de codigo de producto:
            codigo = (int(input("Codigo: ")))

            # Se busca el codigo en la lista de codigos:
            if codigo not in listaProductos[0]:

                # Se agregan los datos a sus respectivas listas:
                listaProductos[0].append(codigo)
                listaProductos[1].append(input("Nombre: "))
                listaProductos[2].append(int(input("Stock: ")))
                listaProductos[3].append(0)
                listaProductos[4].append(float(input("Precio: ")))

                # Salida:
                print("\nProducto registrado con exito\n")
            else:
                # Salida:
                print("El producto ya esta registrado\n")


        case 2:
            print("\n--- ELIMINAR PRODUCTO ---\n")

            # Entrada de codigo de producto:
            codigo = (int(input("Ingrese codigo del producto a eliminar: ")))

            # Se busca el codigo en la lista de codigos:
            if codigo in listaProductos[0]:

                # Se obtiene la posicion del codigo, para buscar los datos en las otras listas, en dicha posicion:
                posicion = listaProductos[0].index(codigo)

                # Se eliminan los datos del producto:
                del listaProductos[0][posicion]
                del listaProductos[1][posicion]
                del listaProductos[2][posicion]
                del listaProductos[3][posicion]
                del listaProductos[4][posicion]

                # Salida:
                print("El producto se borro exitosamente\n")
            else: 
                # Salida:
                print("El producto no existe en los registros\n")


        case 3:
            print("\n--- LISTA DE PRODUCTOS ---\n")

            # Para recorrer sublistas (codigos, nombres, etc...):
            for i in range(len(listaProductos[0])):
                print("--- INFORMACION DE PRODUCTO ---")

                # Para recorrer lista principal (contiene a las sublistas):
                for j in range(len(listaProductos)):
                    match j:
                        # Salidas:
                        case 0: print(f"Codigo: {listaProductos[j][i]}")
                        case 1: print(f"Nombre: {listaProductos[j][i]}")
                        case 2: print(f"Stock: {listaProductos[j][i]}")
                        case 3: print(f"Cantidad Vendida: {listaProductos[j][i]}")
                        case 4: print(f"Precio: {listaProductos[j][i]}")
            print("")
       

        case 4:
            print("\n--- VENTAS ---\n")

            # Entrada de codigo de producto:
            codigo = (int(input("Ingrese codigo del producto a vender: ")))

            # Se busca el codigo en la lista de codigos:
            if codigo in listaProductos[0]:

                # Se obtiene la posicion del codigo, para buscar los datos en las otras listas, en dicha posicion:
                posicion = listaProductos[0].index(codigo)

                # Se verifica el stock:
                if listaProductos[2][posicion] > 0:

                    # Entrada de cantidad a vender:
                    cantidad = int(input("Cantidad que se va a vender?: "))

                    # Se verifica que el stock cubra la demanda de cantidad:
                    if cantidad <= listaProductos[2][posicion]:

                        costoDeVenta= listaProductos[4][posicion] * cantidad

                        # Salida
                        print(f"Venta realizada con exito por ${costoDeVenta}\n")

                        # Se actualizan los valores de stock y cantidad de ventas:
                        listaProductos[2][posicion] -= cantidad
                        listaProductos[3][posicion] += cantidad
                    else:
                        # Salida:
                        print("El stock es insuficiente para la venta solicitada\n")
                else:
                    # Salida:
                    print("Sin Stock\n")
            else:
                # Salida:
                print("El producto no existe en los registros\n")
        

        case 5:
            # La bandera de control cambia para finalizar el programa:
            banderaDeFin = 0

            # Salida:
            print("\n*********** FIN DEL PROGRAMA ***********\n")
        

        case _:  
            # Salida:
            print("Ingrese una opcion valida\n")
