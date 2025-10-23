"""
amila está organizando un proyecto y necesita calcular 
el tiempo total necesario para concluir tres actividades: 
A, B y C. Sin embargo, si alguna actividad tiene un número 
de días negativo, el código debe avisar que los valores 
ingresados son inválidos y no calcular el total.
Escribe un programa que reciba el número de días de tres 
actividades y muestre el tiempo total del proyecto. Si algún 
valor es negativo, muestra un mensaje informando el error.
"""
A=int(input('Informe los dias para la actividad A:'))
B=int(input('Informe los dias para la actividad B:'))
C=int(input('Informe los dias para la actividad C:'))
if A and B and C <0:
    print('Error: Los dias no pueden ser negativos.')
else:
    total=A+B+C
    print(f'El tiempo total del proyecto es: {total} dias.')