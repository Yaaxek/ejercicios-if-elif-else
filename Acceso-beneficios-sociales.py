"""
Laura está desarrollando un sistema para saber si una persona 
tiene derecho a recibir un beneficio social. Para eso, la 
persona debe cumplir las siguientes condiciones:
Tener ingresos menores o iguales a $2,000.
Tener al menos un hijo o hija.
Crea un programa que reciba los ingresos mensuales y la 
cantidad de hijos de una persona, y diga si tiene derecho al 
beneficio.
"""
salario=float(input('Digite su salario mensual: '))
hijos=int(input('Digite la cantidad de hijos: '))
if salario<=2000 and hijos>=1:
    print('Usted tiene acceso a los beneficios sociales.')
else:
    print('Usted no tiene acceso a los beneficios sociales.')