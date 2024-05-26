# Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
# Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
# Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
# La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
# Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.


uni_de_leche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente: "))
es_jubilado = int(input("El cliente es jubilado? Ingrese 0 para NO, otro número para SI: "))

monto_parcial = uni_de_leche * 1000

print(f"unidades de leche: {uni_de_leche}, es jubilado: {es_jubilado}")

monto_a_pagar = monto_parcial

# Descuentos según la cantidad de unidades y si es jubilado o no
if (uni_de_leche <= 12 and not es_jubilado):
    print("unidades de leche <= 12 y no es jubilado")
    monto_a_pagar = monto_parcial

elif ((uni_de_leche > 12 and uni_de_leche <= 24) and not es_jubilado):
    print("unidades de leche > 12 y <= 24 y no es jubilado")
    monto_a_pagar = monto_parcial * 0.9

elif (uni_de_leche > 24 and not es_jubilado):
    print("unidades de leche > 24 y no es jubilado")
    monto_a_pagar = monto_parcial * 0.85

if (uni_de_leche <= 12 and es_jubilado):
    print("unidades de leche <= 12 y es jubilado")
    monto_a_pagar = monto_parcial * 0.9

elif((uni_de_leche > 12 and uni_de_leche <= 24) and es_jubilado):
    print("unidades de leche > 12 y <= 24 y es jubilado")
    monto_a_pagar = monto_parcial * 0.8

elif (uni_de_leche > 24 and es_jubilado):
    print("unidades de leche > 24 y es jubilado")
    monto_a_pagar = monto_parcial * 0.75

print(f"El monto sin descuento es: ${monto_parcial:.2f}")
print(f"El monto total a pagar es: ${monto_a_pagar:.2f}")