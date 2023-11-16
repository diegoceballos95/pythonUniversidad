# ACTIVIDAD OBLIGATORIA N°3

print('\n******************** BIENVENIDO ********************\n')

# -------------------- ENTRADA --------------------

precioUnitario = float(input('Ingrese el precio unitario del "Vaso de Yogurt 190gr": '))
banderaDeParada = True
contadorVasos = 0   # Cantidad de vasos total
contadorVasos15 = 0 # Cantidad de vasos con 15% de descuento
contadorVasos18 = 0 # Cantidad de vasos con 18% de descuento

# -------------------- PROCESAMIENTO --------------------

while banderaDeParada:

    # Nueva entrada:
    codigoDeBarra = int(input('\nIngrese el codigo de barras de 13 digitos: '))

    if codigoDeBarra >= 1000000000000:

        contadorVasos += 1
        
        # El modulo elimina el codigo A y B, luego el cociente elimina el codigo D, dejanto solo el codigo C:
        codigoDeProducto = (codigoDeBarra % 1000000) // 10

        # Calculo del Promedio de Digitos
        sumaDigitos = 0
        while codigoDeProducto != 0:
            digito = codigoDeProducto % 10
            sumaDigitos += digito
            codigoDeProducto //= 10
        promedio = sumaDigitos / 5
            
        # Asignar desceuntos
        if (promedio>=5): 
            contadorVasos15 += 1 
        else: 
            contadorVasos18 += 1

    elif codigoDeBarra == 0:
        banderaDeParada = False

    else:
        print('ERROR: INGRESE UN CODIGO VALIDO')

if contadorVasos != 0:

    # Porcentaje de vasos de Yogurt con 15% de descuento respecto al Total:
    porcentajeVasos15 = (contadorVasos15 * 100 ) / contadorVasos
    # Porcentaje de vasos de Yogurt con 18% de descuento respecto al Total:
    porcentajeVasos18 = (contadorVasos18 * 100 ) / contadorVasos
    # Monto recaudado de la venta total:
    ventaTotal = contadorVasos * precioUnitario
    # Monto destinado a cubrir promocion del 15% de descuento:
    costoPromoVasos15 = (contadorVasos15 * precioUnitario) * 0.15
    # Monto destinado a cubrir promocion del 18% de descuento:
    costoPromoVasos18 = (contadorVasos18 * precioUnitario) * 0.18

    # -------------------- SALIDAS --------------------

    print('\n******************** RESULTADOS ********************\n')
    
    print(f'Se vendieron {contadorVasos15} vasos de yogurt con 15% de descuento')
    print(f'Representan el {porcentajeVasos15}% de la venta total\n')
    print(f'Se vendieron {contadorVasos18} vasos de yogurt con 18% de descuento')
    print(f'Representan el {porcentajeVasos18}% de la venta total\n')
    print(f'La venta total fue de ${ventaTotal}')
    print(f'Se debera reasignar ${costoPromoVasos15 + costoPromoVasos18} para cubrir el coste de las promociones')
else:
    print("No se ingresaron productos")

print('\n******************** FIN DEL PROGRAMA ********************\n')