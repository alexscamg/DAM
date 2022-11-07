numero = int(input('Introduce un numero: '))

if numero < 0:
  print('Introduce un numero mayor que 0')

else:
  resul = 1
  for i in range(numero):
    ope = i * resul
    resul += ope
    
print(f'El factorial de {numero} es: {resul}')