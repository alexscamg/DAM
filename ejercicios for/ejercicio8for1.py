cant = int(input('Cuantos valores vas a introducir? '))
if cant < 0:
  print('Eso es imposible')


suma = 0
for i in range(cant):
  valores = float(input(f'Escribe el número {i+1}:' ))
  ope = suma + valores
  suma = ope
  print(f'La suma de los nuemros que has escrito es: {suma}')