'''
6. Escribe un script que detemine si un nombre dado por el usuario se encuentra en una lista de nombres.
La lista puede ser predeterminada o determinada por el usuario
'''

names = []
morenames = True
es_string  = False
repeated_name = {}
while morenames:
  names.append(input('Ingresa un nombre: '))
  option = input('Quieres agregar mas nombres y/n: ')
  es_string = isinstance(option, str)
  if option == 'y':
    morenames = True
  else:
    morenames = False


for name in names:
  print(name)
  if  names.count(name) > 1:
      print('Repetido')
      repeated_name.update({ name : "Repedito"})
  else:
      print('No repetido')
      repeated_name.update({ name : "No repetido"})

print("Status Nombres Ingresados")
print(repeated_name)
