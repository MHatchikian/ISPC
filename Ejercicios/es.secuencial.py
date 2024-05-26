#EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada
#materia y quiere saber cuál es su promedio

"""n1 = float(input("Ingrese la nota de la primera materia: "))
n2 = float(input("Ingrese la nota de la segunda materia: "))
n3 = float(input("Ingrese la nota de la tercera materia: "))
n4 = float(input("Ingrese la nota de la cuarta materia: "))
n5 = float(input("Ingrese la nota de la quinta materia: "))

promedio=(n1+n2+n3+n4+n5)/5

print("El promedio de las notas es:",promedio)
"""




#EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo que cobra se calcula de acuerdo a 
# los metros cuadrados que debe pintar. El cliente le indica que necesita conocer el costo de mano de obra para pintar 
# una pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metrocuadrado. 
# Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.


"""
alto = float(input("Ingrese el alto de la pared en mts: "))
ancho = float(input("Ingrese el ancho de la pared en mts: "))

costo_por_m2 = float(input("Ingrese el costo por m2: "))

area = alto * ancho

costo_total = area * costo_por_m2

print("El costo total de la mano de obra para pintar la pared es: ",costo_total)
"""

# EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que suequipo lleva acumulados en el campeonato, 
# para ello recibe cada semana la información de la cantidad total de partidos, desde el inicio del campeonato, que
# el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado recibe un punto, 
# por cada partido ganado tres puntos y por los perdidos cero puntos.

"""
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados * 1
puntos_perdidos = partidos_perdidos * 0  

puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos

print("Los puntos acumulados en el campeonato son: ",puntos_totales)

"""
