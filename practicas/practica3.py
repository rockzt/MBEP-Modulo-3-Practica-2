'''
3. Escribe un script que calcule la suma de 3 números dados por el usuario.
Si los valores son iguales deberá imprimir la suma multiplicada por 3
'''
numeros = []
i = 0
suma = 0
while i < 3:
    numero = input('Ingresa un número: ')
    if numero.isnumeric():
        numeros.append(numero)
        suma += int(numero)
        i += 1
        print(i)
    else:
        print('No es un número válido. Inténtalo de nuevo.')

if([numeros[0]]*len(numeros) == numeros):
    suma = suma  * 3

print('Números ingresados:', numeros)
print('Suma números ingresados:', suma)
