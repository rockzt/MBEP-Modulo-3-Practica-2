'''
5. Escribe un script que determine si una letra es vocal o no
'''
es_numerico = True
letra = ""
while es_numerico:
    letra = input('Ingresa una letra: ')
    es_numerico = letra.isnumeric()


if letra.lower() in ('a', 'e', 'i', 'o', 'u'):
  print("Vocal")

elif letra.upper() in ('A', 'E', 'I', 'O', 'U'):
  print("Vocal")

else:
  print("Consonante")
