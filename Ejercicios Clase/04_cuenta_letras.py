"""
Hacer un programa que pida al usuario una serie de caracteres.
Cuanto termine le debe de mostrar una lista con las vocales y otra con las consonantes,
ademas decirle cuantas hay de cada una.
Los caracteres que no son letras se descartan.
"""

def contador():
  entrada = input('Introduce una letra: ')
  vocales = 'aeiou'
  consonantes = 'BCDFGHJKLMNÑPQRSTVXZWY'
  lista_vocales = []
  lista_consonantes = []
  while entrada != '':
    if entrada.lower() in vocales:
      lista_vocales.append(entrada)

    elif entrada.upper() in consonantes:
      lista_consonantes.append(entrada)
    entrada = input('Introduce una letra: ')
  
  return lista_vocales , lista_consonantes



print(contador())