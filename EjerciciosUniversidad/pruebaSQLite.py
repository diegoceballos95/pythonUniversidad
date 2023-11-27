import sqlite3

def seleccionar(ub):

    #Conexión con la BD:
    conexion = sqlite3.connect("DBQuemadores.db")
    cursor = conexion.cursor()

    #Consuta SQL:
    sql = f"SELECT * FROM Quemador WHERE Ubic = '{ub}' "
    cursor.execute(sql)

    #Recorrido del resultado:
    lista = cursor.fetchall() #Lista de tuplas

    for registro in lista:
        print(registro)

    #Cierre de la conexión:
    conexion.close()

seleccionar("D")