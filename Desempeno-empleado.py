"""
Una empresa evalúa a sus empleados con base en dos criterios:
Puntuación de desempeño (de 0 a 10)
Años trabajados
Reglas:
Si la puntuación es mayor o igual a 7:
Si trabajó más de 5 años: "Elegible para ascenso"
Si trabajó 5 años o menos: "Buen desempeño, sigue así"
Si la puntuación es menor a 7: "Necesita mejorar"
Crea un programa que reciba la puntuación y los años trabajados, 
y muestre el mensaje adecuado.
"""
puntuacion=float(input('Digite la puntuacion del empleado (0-10): '))
anos=int(input('Digite los años de servicio del empleado: '))
if puntuacion>=7:
    if anos>5:
        print('El empleado es elegible para ascenso.')
    else:
        print('Buen desmpeño,sigue así.')
else:
    print('Necesita mejorar su desempeño.')