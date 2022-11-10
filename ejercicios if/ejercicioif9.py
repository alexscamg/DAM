import math

triangulo = 'T' or 't'
circulo = 'C' or 'c'

entrada = input(print('¿Que figura quieres carcular? (Escribe T o C): '))

if entrada != triangulo or entrada != circulo:
  print('Valor introducido incorrecto')


  if entrada == triangulo:
    base = float(input(print('Introduce la base: ')))
    altura = float(input(print('Introduce la altura: ')))

    area = (base*altura)/2
    print(f'Un triangulo de base {base} y altura {altura} tien un area {area}.')
  elif entrada == circulo:
    radio = float(input(print('Introduce el radio: ')))

    area = math.pi*radio**2
    print(f'Un circulo de radio {radio} tiene un area de {area}.')

