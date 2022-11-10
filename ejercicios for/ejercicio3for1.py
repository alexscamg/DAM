

for i in range(11):
   if i > 0:
      print(f'{i}\t', end=' ')
 

print()

for i in range(21):
  if i % 2 ==0:
    valores = i
    if valores > 0:
      print(f'{valores}\t', end=' ')
  
print()

for i in range(49):
  if i % 3 ==0:
    valores = i -1
    if valores >= 20:
      print(f'{valores}\t',end=' ')
 
print()

for i in range(30):
  if i % 4 ==0:
    valores = i + 2
    if valores >=10:
      print(f'{valores}\t',end=' ')

print()

for i in reversed(range(46)):
  if i % 5 ==0: 
    valores = i - 5
    if valores >=0:
      print(f'{valores}\t',end=' ')





