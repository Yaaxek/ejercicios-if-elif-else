"""
Bruno gestiona un pequeño comercio y quiere saber qué producto 
tuvo el mejor desempeño de ventas el mes pasado. Registró la 
cantidad vendida de dos productos: manzanas y plátanos. Ahora, 
necesita escribir un programa que identifique y muestre cuál de 
ellos tuvo más ventas.
Crea un programa que reciba el número de ventas de los dos 
productos y muestre un mensaje indicando cuál de ellos vendió
más. Si las cantidades son iguales, muestra un mensaje diciendo 
que hubo un empate.
"""
manzana=int(input('Digite la cantidad de manzanas vendidas: '))
platano=int(input('Digite la cantidad de platanos vendidos: '))
if manzana>platano:
    print('Las manzanas tuvieron mas ventas.')
elif platano>manzana:
    print('Los platanos tuvieron mas ventas.')
else:
    print('Las manzanas y los platanos tuvieron la misma cantidad de ventas.')