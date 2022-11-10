import math
"""
Escribir una función que reciba dos horas en formate hh:mm:ss
Debe devolver la diferencia entre ellas
"""
def segundos(cadena_hora):
  trozoshora = cadena_hora.split(':')
  valores = []
  for i in trozoshora:
    i = int(i)
    valores.append(i)
  segundoshora= valores[0] * 3600
  segundosminutos= valores[1] * 60
  suma = segundoshora+segundosminutos+valores[2]
  return suma


def dif_horas(inicio,fin):
  diferencia = abs(segundos(fin) - segundos(inicio))
  h = diferencia // 3600
  m = diferencia % 3600 //60
  s = diferencia % 3600 % 60

  return f'{h}:{m}:{s}'

print(dif_horas('20:00:00','19:59:00'))