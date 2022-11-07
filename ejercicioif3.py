print('Comparador de años')
año_actual = int(input('Introduce el año actual: '))
año_random = int(input('Escribe un año cualquiera: '))


if año_actual < año_random:
  calculadora = año_random - año_actual
  print(f'Para llegar al año {año_random} faltan {calculadora} años')
elif año_actual > año_random:
  calculadora2 = año_actual - año_random
  print(f'Desde el año {año_random} han pasado {calculadora2} años')
elif año_actual == año_random:
  print('¡Son el mismo año!')
else: 
  print('404 NOT FOUND')


