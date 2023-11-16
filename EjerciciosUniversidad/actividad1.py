"""
Actividad:
Escribir un programa para calcular la potencia de una bomba (expresada en HP) para transportar agua a través de una tubería cilíndrica horizontal, sabiendo:
	• La longitud ingresada por el usuario es L=270 m.
	• El diámetro de la tubería es D=0,0254 m.
	• La velocidad media a la que corre el agua por la tubería es vz=1.38 m/s.
	• El factor de fricción de Fanning del agua es f=0.00579.
	• La densidad del agua es Ro=1000 kg/m3.
	• 1 kg.m2/s3 = 1 Joule/s = 1 Watts
	• 1_Kwatts = 1000 Watts
	• 1 HP = 1 KWatts/0.7457
Nota: Todos los datos se cargarán en variables, excepto el valor de PI que es constante.
"""

# Datos iniciales:
PI = 3.14159
P = 1000		# Denisdad del agua

# Datos ingresados por usuario:
l= float(input('Ingrese la longitud del tubo: '))
d = float(input("Ingrese diametro: "))
vz = float(input("Ingrese velocidad media del fluido: "))
f = float(input("Ingrese factor de friccion de Fanning: "))

# Calculos
deltaP = f * 0.5 * P * (vz**2) * ((4*l)/d)	# Perdida de presion
q = vz * PI * ((d/2) ** 2)					# Caudal del fluido 
potW = deltaP * q							# Potnecia en Watss
potHP = (potW/1000) / 0.735498				# Potencia en HP

print(f'- Perdida de presion: {deltaP}')
print(f'- Caudal del fluido: {q}')
print(f'- Potencia de la bomba en watss: {potW}')
print(f'- Potencia de la bomba en HP: {potHP}')
