""" 
Escriba una funcion que reciba como parametro una cadena de texto y duvuelva una lista con las vocales que haya en dicha cadena
"""
texto = 'La fideua es un plato originario de Gandía que se elabora de forma parecida a la paella. Sus ingredientes principales son: fideos finos o gruesos de pasta, caldo de morralla, pescado'




def cuenta_vocales(cadena):
  vocales = ['a','e','i','o','u']
  salida =[]
  for letra in cadena:
    if letra.lower() in vocales and letra.lower() not in salida:
      salida.append(letra)
  return salida



print(cuenta_vocales('Escribaeia'))





cad= """ 
Funcion que reciba una cadena y devuelve una cadena con los codigos ASCII de las letras
"""

def txt_ascii(cadena):
  salida = []
  for i in cadena:
    salida.append(str(ord(i)))
  
  return ' '.join(salida)


print(txt_ascii(cad))



def ascii_txt(cadena):
  salida = ''
  cadena = cadena.split(' ')
  for c in cadena:
    salida += chr(int(c))
  return salida

print(ascii_txt(txt_ascii(cad)))