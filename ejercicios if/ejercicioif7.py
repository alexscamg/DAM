valora = float(input('Introduce el valor a: '))
valorb = float(input('Escribe el valor b: '))


if valora == 0 or valorb == 0:
  print('Todos los números son solución')
elif valora == 0:
  print('No tiene solución')
else:
  x = -valorb/valora
  print(x)