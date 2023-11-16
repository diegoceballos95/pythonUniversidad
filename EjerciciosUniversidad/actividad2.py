#Actividad obligatoria N°2

from os import system

operar = 1   #Para controlar el ciclo while - 1:True / 0:False
while operar:
    system("cls")

    #Ingreso de datos:
    print("***** INGRESE LAS MEDICIONES REGISTRADAS *****\n")
    m1 = float(input(f"Medicion N°1: "))
    m2 = float(input(f"Medicion N°2: "))
    m3 = float(input(f"Medicion N°3: "))
    m4 = float(input(f"Medicion N°4: "))
    m5 = float(input(f"Medicion N°5: "))
    gan = float(input("\nIngrese la ganancia obtenida por el laboratorio:"))

    #Claculo del promedio de las mediciones:
    prom = (m1+m2+m3+m4+m5)/5

    #Determinar la multa:
    if prom <= 220:
        multa = 0
    elif prom > 200 and prom <= 450:
        multa = 0.05 * gan
    elif prom > 450 and prom <= 675:
        multa = 0.10 * gan
    elif prom > 675 and prom <= 1120:
        multa = 0.25 * gan
    elif prom > 1120 and prom <= 1695:
        multa = 0.50 * gan
    else:
        multa = 0.75 * gan
    print(f"\nLa multa a pagar despues de ser sometido a un control es de ${multa}")

    #Continuar o finalizar programa:
    operar = int(input("\nINGRESE: [0] FINALIZAR / [1] NUEVA OPERACION: "))

print("\n***** FIN DEL PROGRAMA *****\n")