"""
Una escuela otorga becas según tres criterios:
Ingreso familiar mensual.
Promedio del estudiante.
Asistencia (en porcentaje).
Reglas:
Si el ingreso es menor a $1,500 y el promedio es mayor a 8.0 
y la asistencia es al menos 90% → "Beca completa"
Si el ingreso es menor a $2,500 y promedio mayor a 7.0 y 
asistencia al menos 85% → "Media beca"
En otros casos → "No elegible para beca"
"""

salario=float(input('Cual es el ingreso familiar mensual? '))
promedio=float(input('Cual es el promedio del estudiante? '))
asistencia=float(input('Cual es la asistencia del estudiante (0-100)%? '))

if salario<1500 and promedio>8 and asistencia>=90:
    print('El estudiante tiene derecho a una beca completa.')
elif salario<2500 and promedio>7 and asistencia>=85:
    print('El estudiante tiene derecho a una beca parcial.')
else:
    print('El estudiante no tiene derecho a una beca.')