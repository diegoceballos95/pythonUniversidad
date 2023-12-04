import sqlite3

def crearBD():
    # Se conecta a la base de datos (o se crea si no existe):
    conexion = sqlite3.connect("streamers.db")
    # Garantiza que cualq. cambio realizado en la BD se almacene de forma permanente:
    conexion.commit() 
    # Cierro la conexion a la BD, liberando recursos:
    conexion.close()


def crearTabla():
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()

    # Creamos el comando SQL en un DocStrinf (comillas triples):
    cursor.execute(
        """CREATE TABLE streamers(
            name text,
            followers integer,
            subs integer
        )"""
    )

    conexion.commit()
    conexion.close()


def consultarFila(name):
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()

    # Consulto los datos, los almaceno en una lista y los muestro:
    instruccion = f"SELECT * FROM streamers WHERE name = '{name}'"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)

    conexion.commit()
    conexion.close()


def consultarOrdenado(field):
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()

    # Consulto los datos, los almaceno en una lista y los muestro:
    instruccion = f"SELECT * FROM streamers ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)

    conexion.commit()
    conexion.close()


def consultarBD():
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()

    # Consulto los datos, los almaceno en una lista y los muestro:
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    print(datos)

    conexion.commit()
    conexion.close()


def insertarFila(name, followers, subs):
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{name}', {followers}, {subs})"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()


def insertarFilas(streamerList):
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?,?,?)"
    cursor.executemany(instruccion, streamerList)
    conexion.commit()
    conexion.close()


def actualizarCampos():
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()

    # Actualizo el campo subs, donde el campo name sea igual a diego:
    instruccion = f"UPDATE streamers SET subs=10000000 WHERE name='diego' "
    cursor.execute(instruccion)

    conexion.commit()
    conexion.close()


def eliminarFila():
    conexion = sqlite3.connect("streamers.db")
    cursor = conexion.cursor()

    # Se elimina la fila 
    instruccion = f"DELETE FROM streamers WHERE name='ibai' "
    cursor.execute(instruccion)

    conexion.commit()
    conexion.close()


if __name__ == "__main__":

    #crearBD()
    #crearTabla()
    #insertarFila("ibai", 7000000, 15000000)
    #insertarFila("elMariana", 3_000_000, 700000)

    # streamers = [
    #     ("diego", 31700, 0),
    #     ("elRubius", 41_000_000, 37_000_000),
    #     ("xoxas", 5000000, 3250000),
    # ]

    #insertarFilas(streamers)
    #consultarFila("elMariana")
    #consultarBD()
    #consultarOrdenado('name')
    #actualizarCampos()
    #eliminarFila() # -> Se eliminó el registro de ibai

    print("FIN")