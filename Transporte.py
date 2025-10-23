"""
Un sistema de transporte cobra según la edad del pasajero y la distancia recorrida:
Menores de 6 años: Viajan gratis.
De 6 a 18 años:
Hasta 20 km: $1.50
Más de 20 km: $2.50
Mayores de 18:
Hasta 20 km: $2.50
Más de 20 km: $4.00
Crea un programa que reciba la edad y distancia, y muestre el valor a pagar.
"""
edad=int(input('Cual es su edad: '))
distancia=float(input('Cual es la distancia a recorrer en km: '))
if edad<6:
    print('Usted viaja gratis.')
elif 6<=edad<18:
    if distancia>20:
        print('Usted debe pagar $2.50')
    else:
        print('Usted debe pagar $1.50')
else:
    if distancia>20:
        print('Usted debe pagar $4.00')
    else:
        print('Usted debe pagar $2.50')
