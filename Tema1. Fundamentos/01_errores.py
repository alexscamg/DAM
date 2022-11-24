"""def division(numerador, denominador):
  while True:
    try:
      rdo = numerador/denominador
      return rdo
    except ZeroDivisionError:
      print('¡¡¡Que fallo!!!')
      return None

print(division(13,0))

numerador = input('Introduce un numerador: ')
denominador = input('Introduce el denominador: ')

print(division(numerador,denominador))"""

def pide_numeros(numero):
  while not isinstance (numero,(int,float)):
    try:
      numero = int(numero)
      return True
    except:
      numero = input('Introduce un numero:')
      return False


numero = input('Introduce un numero:')
print(pide_numeros(numero))