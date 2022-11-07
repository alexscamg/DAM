# Pide dos numeros y di si los dos son iguales, o cual es menor y mayor

numero2 = float(input('Introduce un numero: '))
numero1 = float(input('Introduce otro numero: '))

if numero1>numero2:
  print('Menor: ',numero2,'Mayor: ',numero1)

elif numero1 == numero2:
  print('Son iguales')

else:
  print('Menor: ',numero1,'Mayor: ',numero2)
