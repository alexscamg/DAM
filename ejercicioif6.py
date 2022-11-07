año = int(input('Introduce un año: '))

calculadora = año % 4
calculadora2 = año % 400
calculadora3 = año % 100

if calculadora2 == 0:
  print(f'El año {año} es un año bisiesto porque es multiplo de 400')
elif calculadora3 == 0:
  print(f'El año {año} no es un año bisiesto porque es multiplo de 100')
elif calculadora == 0:
  print(f'El año {año} es un año bisiesto porque es multiplo de 4')
else:
  print(f'El año {año} no es un año bisiesto.')
