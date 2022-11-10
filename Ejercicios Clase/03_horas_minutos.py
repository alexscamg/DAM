"""
Hacer una función que reciba una hora en formato hh:mm:ss.
Debe devolver la cantidad de segundos de dicha hora.
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


# horausuario = input('Introduce una hora: ')
print(segundos('23:24:24'))