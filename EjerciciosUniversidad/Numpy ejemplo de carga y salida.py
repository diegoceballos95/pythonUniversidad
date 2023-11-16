#########################################################################
#                        MODULOS                                        #
#########################################################################
import numpy as np    

#########################################################################
#                       DECLARACION DE FUNCIONES                        #
#########################################################################

#FUNCION PARA VERIFICAR ENTRADA.
def Verificar(valor, inf, sup):
    while(valor<inf or valor>sup):
        valor=int(input(f"ERROR. Ingrese otra vez [{inf}a{sup}]: "))
    return valor

#FUNCION PARA CARGAR LA MATRIZ.
def Cargar_Matriz(mat, m, n):
    for i in range(m):
        print("Fila ",i)
        for j in range(n):
            mat[i][j] = int(input(f"Mat[{i}][{j}]: "))
        print()

#FUNCION PARA MOSTRAR LA MATRIZ
def Mostrar_Matriz(mat, m, n):
    print("MATRIZ")
    for i in range(m):
        for j in range(n):
            print(f"{mat[i][j]:8}",end="")
        print()

        
#########################################################################
#                       PROGRAMA PRINCIPAL                              #
#########################################################################

#Declaración de la matriz de enteros, Máx.50x12
matriz = np.empty((50,12), dtype="int")

#Entrada de datos.
fil = int(input("Cantidad de productos [Máx.50]: "))
fil = Verificar(fil, 1, 50)
col = int(input("Cantidad de meses [Máx.12]: "))
col = Verificar(col, 1, 12)

#Procesamiento.
print()
Cargar_Matriz(matriz, fil, col)
print()
Mostrar_Matriz(matriz, fil, col)