num1 = int(input('Introduce un numero: '))
num2 = int(input('Introduce otro numero cualquiera: '))
num3 = int(input('Introduce otro numero mas: '))


if num1 == num2 == num3:
  print('Ha escrito tres veces el mismo numero')
elif num1 == num2 != num3:
  print('Ha escrito uno de los números dos veces')
elif num1 == num3 != num2:
  print('Ha escrito uno de los números dos veces')
elif num2 == num3 != num1:
  print('Ha escrito uno de los números dos veces')
else:
  print('Los tres números que ha escrito son distintos')
