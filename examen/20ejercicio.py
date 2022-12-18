cad = input('Dime un texto: ')



def txt_ascii(cadena):
  salida = []
  for i in cadena:
    salida.append(str(ord(i)))
  return ' '.join(salida)

print(txt_ascii(cad))

print()

def ascii_txt(cadena):
  salida = ''
  cadena = cadena.split(' ')
  for c in cadena:
    salida += chr(int(c))
  return salida


print(ascii_txt(txt_ascii(cad)))