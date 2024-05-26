#Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
# Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
# Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
# La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
# Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

uni_de_leche = int(input("Ingrese la cantidad de unidades de leche que compra el cliente: "))
es_jubilado = input("El cliente es jubilado? Ingrese SI o NO segun corresponda: ").strip().upper()


es_jubilado = es_jubilado == "SI"

monto_parcial = uni_de_leche * 1000

monto_a_pagar = monto_parcial

if uni_de_leche <= 12:
    if es_jubilado:
        print("unidades de leche <= 12 y es jubilado")
        monto_a_pagar = monto_parcial * 0.9
    else:
        print("unidades de leche <= 12 y no es jubilado")
        monto_a_pagar = monto_parcial
elif uni_de_leche <= 24:
    if es_jubilado:
        print("unidades de leche > 12 y <= 24 y es jubilado")
        monto_a_pagar = monto_parcial * 0.8
    else:
        print("unidades de leche > 12 y <= 24 y no es jubilado")
        monto_a_pagar = monto_parcial * 0.9
else:
    if es_jubilado:
        print("unidades de leche > 24 y es jubilado")
        monto_a_pagar = monto_parcial * 0.75
    else:
        print("unidades de leche > 24 y no es jubilado")
        monto_a_pagar = monto_parcial * 0.85

print(f"El monto sin descuento es: ${monto_parcial:.2f}")
print(f"El monto total a pagar es: ${monto_a_pagar:.2f}")
