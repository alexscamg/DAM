"""
Hacer un programa que pida al usuario una serie de caracteres.
Cuanto termine le debe de mostrar una lista con las vocales y otra con las consonantes,
ademas decirle cuantas hay de cada una.
Los caracteres que no son letras se descartan.
"""

def contador():
  vocales = 'aeiou'
  consonantes = 'BCDFGHJKLMNÑPQRSTVXZWY'
  lista_vocales = []
  lista_consonantes = []
  while True:
    entrada = input('Introduce una letra: ')
    if entrada == '':
      break
    if entrada.lower() in vocales:
      lista_vocales.append(entrada)

    elif entrada.upper() in consonantes:
      lista_consonantes.append(entrada)
    
  
  return lista_vocales , lista_consonantes



print(contador())