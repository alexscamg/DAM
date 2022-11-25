import os
def esto_falla():
  try:
    f = open('no_existe2.txt', 'r')   # Intenta esto, si no da el error del except pasa al else
    print('--------try--------')

  except FileNotFoundError as e:
    print(e)
  
  else:
    print('--------------------------else---------------------------')
  
  finally:
    print('------------------------finally--------------------------')     # Pasa siempre por finally

esto_falla()


def genera_error(num):
  if num <10:
    raise Exception('Error de numero demasiado pequeño. ')
  else:
    print('Funciona!!!!!!!!')

try:
  genera_error(9)

except:
  exit()
