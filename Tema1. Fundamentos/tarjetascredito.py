tarjeta = input('Introduce tu tarjeta de credito: ')


def censura(cadena):
  inicio = '*' * (len(cadena) - 4)
  final = cadena[-4:]
  return inicio+final
  




print(censura(tarjeta))