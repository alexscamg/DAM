def solution(number):
  primo5 = number%5 
  primo3 = number%3
  if number < 0:
      return 0
  elif primo5 == 0:
    for i in range(number):
      return i
  elif primo3 ==0:
    for i in range(number):
      return i
    


number = int(input('Introduce un numero: '))
print(solution(number))
