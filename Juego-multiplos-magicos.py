"""
Estás desarrollando un pequeño juego. El usuario ingresa un 
número entero y el programa debe evaluar lo siguiente:
Si el número es divisible por 3 y 5, muestra: "¡Número mágico!"
Si solo es divisible por 3, muestra: "Divisible por 3"
Si solo es divisible por 5, muestra: "Divisible por 5"
Si no es divisible por ninguno, muestra: "No es un número mágico"
"""
n=int(input('Ingrese un numero: '))
if n%3==0 and n%5==0:
    print('Numero magico!')
elif n%3==0:
    print('Divisible por 3')
elif n%5==0:
    print('Divisible por 5')
else:
    print('No es un numero magico.')