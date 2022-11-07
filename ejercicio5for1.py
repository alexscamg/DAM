num1 = int(input('Dame un numero entero: '))
num2 = int(input('Dame un numero igual o mayor que el anterior: '))

if num2 < num1:
  print(f'Te he dicho que sea mayor o igual')

else: 
  for i in range (num1,num2+1):
    if i % 2 == 0:
      print(f'El numero {i} es par')

    else:
      print(f'El numero {i} es impar')
