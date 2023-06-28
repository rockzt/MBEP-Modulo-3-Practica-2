'''
1. Escribe un script que le pregunte al usuario varios nombres hasta que el usuario especifique que ya no desea ingresar más nombres.
Como resultado deberá mostrar al usuario una lista, una tupla y un set con todos los nombres que ingresó el usuario
'''
names = []
morenames = True
es_string  = False
while morenames:
  names.append(input('Ingresa un nombre: '))
  option = input('Quieres agregar mas nombres y/n: ')
  es_string = isinstance(option, str)
  if option == 'y':
    morenames = True
  else:
    morenames = False

tupla = tuple(names)
setnames = set(names)

print(f'Lista:  {names}')
print(f'Tupla:  {tupla}')
print(f'Set:  {setnames}')
print("---------------------")
print(type(names))
print(type(tupla))
print(type(setnames))