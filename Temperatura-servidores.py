"""
Lucas trabaja en TI y necesita garantizar que la temperatura 
de una sala de servidores no supere los 25°C. Quiere un 
programa que reciba la temperatura actual como entrada y, si 
es necesario, muestre un mensaje de alerta.
"""
temperatura=float(input('Digite la temperatura del servidor: '))
if temperatura>25:
    print('Alerta! Temperatura por encima del limite permitido.')
else:
    print('Temperatura normal.')