numero1 = int(input(print(f'Introduce un numero entero: ')))
numero2 = int(input(print(f'Introduce un numero entero mayor que {numero1}: ')))

if numero2 <= numero1:
  print(f'¡Te he pedido un numero mayor que {numero1}!')



else:
  suma = 0
  for i in range(numero1, numero2+1):
    suma  = suma + i
    
  print(suma)
  


