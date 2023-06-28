'''
9. Escribe un script que imprima si un string dado por el usuario contiene números o no.
'''

esta_vacio = True
cadena = ""
while esta_vacio:
    cadena = input('Ingresa una cadena de texto: ')

    if cadena == "":
      esta_vacio = True
    else:
      esta_vacio = False

it = 0
for char in cadena:
  if char.isdigit():
    print("Digito encontrado : " + char)
    it += 1
  else:
    it += 0

print("Dentro de la cadena de texto:" + cadena)

if it == 0:
  print("No se encontraron digitos en la cadena de texto:" + cadena)

