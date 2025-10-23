"""
Una empresa evalúa su trimestre con base en:
Ingresos totales
Gastos totales
Número de nuevos clientes
Clasificación:
Si ingresos - gastos > $10,000 y más de 50 nuevos clientes → "Trimestre Excelente"
Si ingresos - gastos > $5,000 y al menos 20 clientes → "Trimestre Bueno"
Si ingresos - gastos > 0 → "Trimestre Regular"
Si ingresos - gastos ≤ 0 → "Trimestre Deficitario"
"""
ingreso=float(input('Ingresos totales por trimestre:'))
gastos=float(input('Gastos totales por trimestre:'))
clientes=int(input('Cantidad de clientes nuevos por trimestre:'))
total=ingreso-gastos
if total>10000 and clientes>50:
    print('Trimestre Excelente')
elif total>5000 and clientes>=20:
    print('Trimestre Bueno')
elif total>0:
    print('Trimestre Regular')
else:
    print('Trimestre Deficitario')