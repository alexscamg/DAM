def fib(n):
  resultado = 1
  num1 = 0
  num2 = 1

  for i in range(n):
    resultado = num1 + num2
    num1 = num2
    num2 = resultado

  return resultado


print(fib(6))