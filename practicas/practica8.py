'''
8. Escribe un script que convierta una cantidad de segundos dada por el usuario a horas, minutos y segundos.
'''

es_numerico = False
while not es_numerico:
    segundos = input('Ingresa los segundos que deseas convertir: ')
    es_numerico = segundos.isnumeric()

print(segundos)

seconds = int(segundos) % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

output = "%d:%02d:%02d" % (hour, minutes, seconds)
print(output)
