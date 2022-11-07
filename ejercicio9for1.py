from operator import neg


cant = int(input('Cuantos valores vas a introducir? '))
if cant < 0:
  print('Eso es imposible')

neg = 0
for i in range(cant):
  valores = float(input(f'Escribe el número {i+1}:'))
  if valores < 0:
    neg += 1


if neg == 1:
  print(f'Ha escrito {neg} número negativo')

else:
  print(f'Ha escrito {neg} números negativos')
