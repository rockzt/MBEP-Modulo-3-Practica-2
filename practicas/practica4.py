'''
4. Escribe un script que calcule cuantas veces se repite un nombre en una lista de nombres determinada por el usuario.
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
  repeated_name.update({ name : names.count(name)})

print("Número de veces que se repite un nombre en la lista")
print(repeated_name)
