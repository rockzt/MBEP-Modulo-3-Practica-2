'''
7. Escribe un script que le pida al usuario un número mínimo y un número máximo de un rango de números.
El script debe imprimir cuales de ellos son divisibles entre 3
'''
es_numerico = False
list_div = []

num_min = int(input('Ingrese el numero minimo: '))
num_max = int(input('Ingrese el numero maximo: '))


if num_min >= num_max:
    print('El rango no es el correcto')
    es_numerico = True
else:
    for num in range(num_min, num_max +1):
        if num % 3 == 0:
          list_div.append(num)
    print("Números divisibles entre 3")
    print(list_div)