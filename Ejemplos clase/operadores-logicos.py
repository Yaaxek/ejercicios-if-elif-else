"""
Operadores logicos
and: y
verdadero y verdadero = verdadero
verdadero y falso = falso
falso y verdadero = falso
falso y falso = falso   
or: o
verdadero o verdadero = verdadero
verdadero o falso = verdadero
falso o verdadero = verdadero
falso o falso = falso
not: no
no verdadero = falso
no falso = verdadero
"""
numero=13
if numero ==13 and numero>13:
    print('Condicion verdadera',numero)
else:
    print('Condicion falsa',numero)

numero=12
if numero ==12 or numero>13:
    print('Condicion verdadera',numero)
else:
    print('Condicion falsa',numero)

