'''
2. Escribe un script que calcule la diferencia entre un número dado y 17 e imprima el resultado.
Si el número es más grande que 17 deberá imprimir el doble de la diferencia entre ambos números
'''
es_numerico = False
num_2 = 17
diff= 0
while not es_numerico:
    numero = input('Ingresa un número: ')
    es_numerico = numero.isnumeric()

numero = int(numero)

if numero > num_2:
    diff = numero - num_2
else:
    diff = num_2 - numero

if numero > 17:
    print(diff**2)
else:
    print(diff)
