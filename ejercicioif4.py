num_actual = int(input('Introduce un numero: '))
num_random = int(input('Introduce otro numero cualquiera: '))


if num_actual == 0 or num_random == 0:
  print('No se puede dividir entre cero')

else:

  if num_actual < num_random:
    numero = num_random
    multiplo = num_actual
    calculadora = num_random%num_actual
    if calculadora == 0:
      print(f'{numero} es multiplo de {multiplo}')
    else:
      print(f'{numero} no es multiplo de {multiplo}')
  elif num_actual > num_random:
    numero = num_actual
    multiplo = num_random
    calculadora = num_actual % num_random
    if calculadora == 0:
      print(f'{numero} es multiplo de {multiplo}')
    else:
      print(f'{numero} no es multiplo de {multiplo}')
  else:
    numero = num_random
    multiplo = num_actual
    print(f'{numero} es multiplo de {multiplo}')
